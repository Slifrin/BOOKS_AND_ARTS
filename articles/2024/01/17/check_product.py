from itertools import product

def get_search_criteria():
    COURT_TYPES = [
        'State', 'Magistrate', 'Superior',
    ]
    CASE_TYPES = [
        'Court',
        'Criminal',
    ]
    print("part1  ", *map('-'.join, product(COURT_TYPES, CASE_TYPES)))
    print("part2  ", *[map('-'.join, product(COURT_TYPES, CASE_TYPES))] * len(CASE_TYPES))

    maped_objects = [map('-'.join, product(COURT_TYPES, CASE_TYPES))] * len(CASE_TYPES)
    print(maped_objects)
    print(*maped_objects)

    for object in maped_objects:
        print(*object)

    # the tric is to use same map object twice (check the id) and consecutive calls of next on it will
    # expire the generator, nice thing to know
    courts = zip(*[map(' '.join, product(COURT_TYPES, CASE_TYPES))] * len(CASE_TYPES))
    for court in courts:
        print(court)

def main() -> None:
    print(f'Hello main from : {__file__}')
    get_search_criteria()

if __name__ == '__main__':
    main()