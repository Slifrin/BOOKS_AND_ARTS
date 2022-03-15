import pickle

from datetime import datetime


class Ride:
    def __init__(self, start, end, distance, numpassengers):
        self.start = start
        self.end = end
        self.distance = distance
        self.numpassengers = numpassengers

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"{cls}({self.start!r}, {self.end!r}, {self.distance!r}, {self.numpassengers!r})"




def main():
    print('Hello main')
    with open('rides.pkl', 'rb') as fp:
        while True:
            try:
                ride = pickle.load(fp)
                print(ride)
            except EOFError:
                break


if __name__ == '__main__':
    main()
