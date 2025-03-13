import contextlib


@contextlib.contextmanager
def dummy_resource(n):

    print(f"befor yield {n=}")
    try:
        yield n
    finally:
        print(f"after yield {n=}")


def fun_with_contexts():
    with dummy_resource(1) as r1:
        print(r1)

    



def main() -> None:
    print(f"Hello main from : {__file__}")
    fun_with_contexts()


if __name__ == "__main__":
    main()
