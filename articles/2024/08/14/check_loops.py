def check_loop(l):
    for x, y in zip(l[1:], l[:-1]):
        print(x, y)
    else:
        if x and y: 
            print(x, y)


def main() -> None:
    print(f"Hello main from : {__file__}")

    check_loop([1, 2, 3, 4])
    check_loop([]) # tarapaty


if __name__ == "__main__":
    main()
