from abc import ABC, abstractmethod

class FilterStrategy(ABC):

    @abstractmethod
    def remove_value(self, value):
        pass

class RemoveNegativeStrategy(FilterStrategy):
    def remove_value(self, value):
        return value < 0

class RemoveOddStrategy(FilterStrategy):
    def remove_value(self, value):
        return abs(value) % 2
    

class Values:
    def __init__(self, values):
        self.values = values


    def filter(self, strategy: FilterStrategy):
        rets = []
        for n in self.values:
            if not strategy.remove_value(n):
                rets.append(n)
        return rets


def show_strategy():
    from os.path import basename

    print()
    print(f"{basename(__file__):_^80}")

    values = Values([-5, -3, -2, 0, 1, 4, 6, 9])
    print(values.filter(RemoveNegativeStrategy()))
    print(values.filter(RemoveOddStrategy()))
    