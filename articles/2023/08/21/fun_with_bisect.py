import bisect
from typing import NamedTuple
from operator import attrgetter
from pprint import pprint


def simple_example():
    def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
        i = bisect.bisect(breakpoints, score)
        print(f"Grading score {score}, {i}")
        return grades[i]

    grades = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    print(grades)


def list_of_tuples():
    class Movie(NamedTuple):
        name: str
        released: int
        director: str

    movies = [
        Movie("Jaws", 1975, "Spielberg"),
        Movie("Titanic", 1997, "Cameron"),
        Movie("The Birds", 1963, "Hitchcock"),
        Movie("Aliens", 1986, "Cameron"),
    ]

    by_year = attrgetter("released")
    movies.sort(key=by_year)

    first_movie_after_1960 = movies[bisect.bisect(movies, 1960, key=by_year)]
    print(first_movie_after_1960, end="\n\n")

    # Insert a movie while maintaining sort order
    romance = Movie('Love Story', 1970, 'Hiller')
    bisect.insort(movies, romance, key=by_year)
    pprint(movies)


def main() -> None:
    print(f"Hello main from : {__file__}")
    simple_example()
    list_of_tuples()


if __name__ == "__main__":
    main()
