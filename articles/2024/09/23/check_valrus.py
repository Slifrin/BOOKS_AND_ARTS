from itertools import pairwise

def simple_generatro():
    for i, j in pairwise(range(9)):
        yield i, j

def main() -> None:
    print(f'Hello main from : {__file__}')
    gen = simple_generatro()
    for data in gen:
        print(data)

if __name__ == '__main__':
    main()