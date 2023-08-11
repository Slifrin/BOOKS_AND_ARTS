from abc import ABC, abstractmethod
from collections import namedtuple
import typing
from dataclasses import dataclass, field, fields
from datetime import date
from os import getenv
from pathlib import Path
from typing import Any, Optional
from urllib.request import urlretrieve
from unicodedata import normalize

from bs4 import BeautifulSoup as Soup  # type: ignore

from pprint import pprint

TMP = getenv("TMP", "/tmp")
TODAY = date.today()


# different option for NamedTuple


class Candidate(typing.NamedTuple):
    name: str
    votes: int


LeaderBoard = typing.NamedTuple(
    "LeaderBoard",
    [
        ("Candidate", Candidate),
        ("Average", float),
        ("Delegates", int),
        ("Contributions", float),
        ("Coverage", int),
    ],
)
Poll = typing.NamedTuple(
    "Poll",
    [
        ("Poll", str),
        ("Date", str),
        ("Sample", str),
        ("Sanders", float),
        ("Biden", float),
        ("Gabbard", float),
        ("Spread", str),
    ],
)


@dataclass
class File:
    """File represents a filesystem path.

    Variables:
        name: str -- The filename that will be created on the filesystem.
        path: Path -- Path object created from the name passed in.

    Methods:
        [property]
        data: -> Optional[str] -- If the file exists, it returns its contents.
            If it does not exist, it returns None.
    """

    name: str
    path: Path = field(init=False)

    @property
    def data(self) -> Optional[str]:
        if self.path.exists():
            return self.path.read_text()
        return None

    def __post_init__(self):
        self.path = Path(self.name)


@dataclass
class Web:
    """Web object.

    Web is an object that downloads the page from the url that is passed
    to it and stores it in the File instance that is passed to it. If the
    File already exists, it just reads the file, otherwise it downloads it
    and stores it in File.

    Variables:
        url: str -- The url of the web page.
        file: File -- The File object to store the page data into.

    Methods:
        [property]
        data: -> Optional[str] -- Reads the text from File or retrieves it from the
            web if it does not exists.

        [property]
        soup: -> Soup -- Parses the data from File and turns it into a BeautifulSoup
            object.
    """

    url: str
    file: File

    @property
    def data(self) -> Optional[str]:
        """Reads the data from the File object.

        First it checks if the File object has any data. If it doesn't, it retrieves
        it and saves it to the File. It then reads it from the File and returns it.

        Returns:
            Optional[str] -- The string data from the File object.
        """
        if not self.file.path.exists():
            urlretrieve(self.url, self.file.path)
        return self.file.data

    @property
    def soup(self) -> Soup:
        """Converts string data from File into a BeautifulSoup object.

        Returns:
            Soup -- BeautifulSoup object created from the File.
        """
        if (data := self.data) is not None:
            return Soup(data, "html.parser")
        return Soup("", "html.parser")


@dataclass
class Site(ABC):
    """Site Abstract Base Class.

    Defines the structure for the objects based on this class and defines the interfaces
    that should be implemented in order to work properly.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        [abstractmethod]
        parse_rows: -> Union[List[LeaderBoard], List[Poll]] -- Parses a BeautifulSoup
            table element and returns the text found in the td elements as
            namedtuples.

        [abstractmethod]
        polls: -> Union[List[LeaderBoard], List[Poll]] -- Does the parsing of the table
            and rows for you. It takes the table index number if given, otherwise
            parses table 0.

        [abstractmethod]
        stats: -- Formats the results from polls into a more user friendly
            representation.
    """

    web: Web

    def find_table(self, loc: int = 0) -> Soup:
        """Finds the table elements from the Soup object

        Keyword Arguments:
            loc {int} -- Parses the Web object for table elements and
                returns the first one that it finds unless an integer representing
                the required table is passed. (default: {0})

        Returns:
            str -- The html table
        """
        return self.web.soup.find_all("table")[loc]

    @abstractmethod
    def parse_rows(self, table: Soup) -> list[Any]:
        """Abstract Method

        Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as NamedTuple.

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        pass

    @abstractmethod
    def polls(self, table: int = 0) -> list[Any]:
        """Abstract Method

        Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        pass

    @abstractmethod
    def stats(self, loc: int = 0):
        """Abstract Method

        Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        pass


@dataclass
class RealClearPolitics(Site):
    """RealClearPolitics object.

    RealClearPolitics is a custom class to parse a Web instance from the
    realclearpolitics website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[Poll] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as Poll namedtuples.

        polls: -> List[Poll] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            RealClearPolitics
            =================
                Biden: 214.0
              Sanders: 142.0
              Gabbard: 6.0

    """

    def parse_rows(self, table: Soup) -> Optional[Poll]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as Poll namedtuples.

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        td_s = table.find_all("td")
        if len(td_s) == 7:
            poll_name = normalize("NFKD", td_s[0].text.strip())
            date_span = normalize("NFKD", td_s[1].text.strip())
            sample = normalize("NFKD", td_s[2].text.strip())
            sanders = float(td_s[3].text) if td_s[3].text.isdigit() else 0.0
            biden = float(td_s[4].text) if td_s[4].text.isdigit() else 0.0
            gabbard = float(td_s[5].text) if td_s[5].text.isdigit() else 0.0
            spread = normalize("NFKD", td_s[6].text.strip())

            return Poll(poll_name, date_span, sample, sanders, biden, gabbard, spread)
        return None

    def polls(self, table: Soup) -> list[Poll]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        elemts = table.find_all("tr")
        new_polls = []
        for tr in elemts:
            if tr["class"] == ["header"] or tr["class"] == ["rcpAvg"]:
                continue
            if (new_poll := self.parse_rows(tr)) is not None:
                new_polls.append(new_poll)
        return new_polls

    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.

        """
        polls_data = self.polls(self.find_table(loc))
        biden = sum(data.Biden for data in polls_data)
        sanders = sum(data.Sanders for data in polls_data)
        gabbard = sum(data.Gabbard for data in polls_data)
        results = f"\n{self.__class__.__name__}\n"
        max_column_width = max(len(name) for name in ['biden', 'sanders', 'gabbard'])
        title_lenght = len(results.strip())
        results += f"{'=' * title_lenght}\n"
        results += f"{'biden':>{max_column_width}} | {biden}\n"
        results += f"{'sanders':>{max_column_width}} | {sanders}\n"
        results += f"{'gabbard':>{max_column_width}} | {gabbard}\n"

        print(results)


@dataclass
class NYTimes(Site):
    """NYTimes object.

    NYTimes is a custom class to parse a Web instance from the nytimes website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[LeaderBoard] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as LeaderBoard namedtuples.

        polls: -> List[LeaderBoard] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            NYTimes
            =================================

                               Pete Buttigieg
            ---------------------------------
            National Polling Average: 10%
                   Pledged Delegates: 25
            Individual Contributions: $76.2m
                Weekly News Coverage: 3

    """

    web: Web

    def parse_rows(self, table: Soup) -> list[LeaderBoard]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as LeaderBoard namedtuples.

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
            the table data.
        """
        pass

    def polls(self, table: int = 0) -> list[LeaderBoard]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
                the table data.
        """
        pass

    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        pass


def gather_data():
    rcp_file = File("realclearpolitics.html")
    rcp_url = "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_realclearpolitics.html"
    rcp_web = Web(rcp_url, rcp_file)
    rcp = RealClearPolitics(rcp_web)
    rcp.stats(3)

    # nyt_file = File("nytimes.html")
    # nyt_url = "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_nytimes.html"
    # nyt_web = Web(nyt_url, nyt_file)
    # nyt = NYTimes(nyt_web)
    # nyt.stats()


if __name__ == "__main__":
    gather_data()
