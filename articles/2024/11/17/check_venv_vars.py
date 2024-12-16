import sys


def main() -> None:
    print(f"Hello main from : {__file__}")
    print(sys.prefix)
    print(sys.base_prefix)
    print(sys.exec_prefix)
    print(sys.base_exec_prefix)

if __name__ == "__main__":
    main()
