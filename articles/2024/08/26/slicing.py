def main() -> None:
    print(f"Hello main from : {__file__}")
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(l[1:5])
    print(l[2:])
    print(l[:7])
    print(l[:])

    print(l[1:8:3])

    print(l[::-1])
    print(l[1::-1])
    print(l[:-3:-1])
    print(l[-3::-1])

if __name__ == "__main__":
    main()
