import array
import sys


def basic_example():
    a = array.array("l", [1, 2, 3, 4, 5])
    print(a)
    print(a.tobytes())
    print(a.tolist())

    for i in a:
        print(i.to_bytes())

    mv = memoryview(a)
    print(mv.nbytes)
    mv[-1] = 6
    print(a.tolist())
    for e in mv:
        print(e)

    raw = mv.cast("B")
    raw[-3] = 7
    raw[7] = 1
    print(a.tolist())
    for i, e in enumerate(raw, start=1):
        print(e, end=" ")
        if i % a.itemsize == 0:
            print()



def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    basic_example()


if __name__ == "__main__":
    main()
