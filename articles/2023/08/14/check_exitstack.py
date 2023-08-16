import contextlib


def power_of_exitstack(file_names: list[str]):
    with contextlib.ExitStack() as stack:
        files = [stack.enter_context(open(file_name)) for file_name in file_names]



def main() -> None:
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()