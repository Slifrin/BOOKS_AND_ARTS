import resource

from a_pythonic_object import Vector2d, Vector2d_with_slots

NUM_VECTORS = 10**7


def main():
    fmt = 'Selected Vector2d type: {.__name__}'
    
    for vector in (Vector2d, Vector2d_with_slots):
        print()
        print(fmt.format(vector))

        mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        print('Creating {:,} Vector2d instances'.format(NUM_VECTORS))

        vectors = [vector(3.0, 4.0) for i in range(NUM_VECTORS)]

        mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        print('Initial RAM usage: {:14,}'.format(mem_init))
        print('Final RAM usage: {:14,}'.format(mem_final))
        print('Diff in mem usage {:14,}'.format(mem_final - mem_init))


if __name__ == '__main__':
    main()