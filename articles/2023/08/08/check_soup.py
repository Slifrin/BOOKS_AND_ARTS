import requests
from pprint import pprint

from bs4 import BeautifulSoup
from bs4.element import Tag



def soup_check():

    # with open("index.html") as fp:
    #     soup = BeautifulSoup(fp, 'html.parser')

    soup1 = BeautifulSoup("<html>a web page</html>", 'html.parser')
    soup2 = BeautifulSoup("<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser")
    print(soup1)
    print()
    print(soup2)
    pprint(dir(soup2))


def job_printer(job_elements):
    for i, job_element in enumerate(job_elements):
        title = job_element.find("h2", class_="title")
        company = job_element.find("h3", class_="company")
        location = job_element.find("p", class_="location")

        print(f"{i} : {title.text.strip()} -- {company.text.strip()} -- {location.text.strip()}")

def show_all_jobs(results: Tag):
    job_elements = results.find_all("div", class_="card-content")

    job_printer(job_elements)
    print(locals().keys())


def parse_sub_site(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("h1", class_="title")
    subtitle = soup.find("p", class_="subtitle")
    print(f"{title.text.strip()} {'-' * 5} {subtitle.text.strip()}")


def show_python_jobs(results: Tag):
    python_jobs = results.find_all("h2", string="Python")
    print(python_jobs) # man it is not working :(
    python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
    print(len(python_jobs))
    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    job_printer(python_job_elements)

    for python_job in python_job_elements:
        links = python_job.find_all("a")
        for link in links:
            if "apply" in link.text.strip().lower():
                url = link["href"].strip()
                print(url)
                parse_sub_site(url)
                # return


def get_sites():

    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    if isinstance(results, Tag):
        # show_all_jobs(results)
        show_python_jobs(results)


def main() -> None:
    print(f'Hello main from : {__file__}')
    get_sites()
    # soup_check()

if __name__ == '__main__':
    main()