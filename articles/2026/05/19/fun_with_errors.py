import sys


def f_with_exception():
    try:
        raise RuntimeError("Tarapaty")
    except Exception:
        print(f"Handling exception ")
        raise
    finally:
        print("Here is finally block")

def f_with_strange_raising_of_exceptions():
    try:
        raise RuntimeError("Tarapaty")
    except RuntimeError:
        print(f"Handling exception ")
        raise ValueError('Ajjjj')
    except Exception:
        print("Handling of base exception")
    finally:
        print("Here is finally block")


def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    f_with_strange_raising_of_exceptions()


if __name__ == '__main__':
    main()