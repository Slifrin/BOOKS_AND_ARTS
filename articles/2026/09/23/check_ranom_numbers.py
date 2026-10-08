import sys
import random


def basic_random_operations():
    state = random.getstate()
    # print(state)
    print(random.randrange(0, 100, 1))

    print(random.choice([1, 3, 5, 6]))
    x = [1, 2, 3, 4]
    random.shuffle(x)
    print(x)

    print(random.sample(["red", "blue"], counts=[4, 2], k=5))
    print(random.sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5))

    print(random.random())


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    basic_random_operations()


if __name__ == "__main__":
    main()
