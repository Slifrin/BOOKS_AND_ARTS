def main() -> None:
    print(f"Hello main from : {__file__}")
    s = slice(1, 3, 1)
    container = [1,2,3,4,5,6,7,8]

    print(container[s])

    s2 = slice(2, 6, 2)
    print(container[s2])


if __name__ == "__main__":
    main()
