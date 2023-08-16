
def execution_time_var():
    print("EXECUTION time")
    numbers = 'one', 'two', 'three'
    funcs = []
    for n in numbers:
        funcs.append(lambda: print(n))

    for f in funcs:
        f()


def definition_time_var():
    print("DEFINITION time")
    numbers = 'one', 'two', 'three'
    funcs = []
    for n in numbers:
        funcs.append(lambda n=n: print(n))

    for f in funcs:
        f()


def abuse_lambda():
    class Car:
        def __init__(self, brand, year):
            self._brand = brand
            self._year = year

        brand = property(lambda self: getattr(self, "_brand"),
                         lambda self, value: setattr(self, "_brand", value))
                         
        year = property(lambda self: getattr(self, "_year"),
                         lambda self, value: setattr(self, "_year", value))
    
        __str__ = lambda self: f"{self.brand}, {self.year}"

        honk = lambda self: print("Honk")

def usage_of_lambdas_for_functional_programming():
    import functools

    elements = list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
    print(elements)
    elements = list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))
    print(elements)
    elements = functools.reduce(lambda acc, x: f"{acc} | {x}", ['cat', 'dog', 'cow'])
    print(elements)

def as_key_function():
    ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
    print(sorted(ids))
    sorted_ids = sorted(ids, key=lambda x: int(x[2:]))
    print(sorted_ids)


def main() -> None:
    print(f'Hello main from : {__file__}')
    execution_time_var()
    definition_time_var()

    usage_of_lambdas_for_functional_programming()


if __name__ == '__main__':
    main()