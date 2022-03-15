import datetime
import heapq


def infinit_generator_producing_task():
    """https://realpython.com/python-heapq-module/#a-high-level-operation"""
    def email(frequency, details):
        current = datetime.datetime.now()
        while True:
            current += frequency
            yield current, details

    fast_email = email(datetime.timedelta(minutes=15), "fast email")
    slow_email = email(datetime.timedelta(minutes=40), "slow email")

    unified = heapq.merge(fast_email, slow_email)

    for _ in range(10):
        print(next(unified))


def medal_problems():
    results = """   Christania Williams      11.80
                    Marie-Josee Ta Lou       10.86
                    Elaine Thompson          10.71
                    Tori Bowie               10.83
                    Shelly-Ann Fraser-Pryce  10.86
                    English Gardner          10.94
                    Michelle-Lee Ahye        10.92
                    Dafne Schippers          10.90"""
    top_3 = heapq.nsmallest(3, results.splitlines(), key=lambda x: float(x.split()[-1]))
    print("\n".join(top_3))


"""
A heap, as an implementation of a priority queue, is a good tool for solving
problems that involve extremes, like the most or least of a given metric.

There are other words that indicate a heap might be useful:

    Largest
    Smallest
    Biggest
    Smallest
    Best
    Worst
    Top
    Bottom
    Maximum
    Minimum
    Optimal

"""