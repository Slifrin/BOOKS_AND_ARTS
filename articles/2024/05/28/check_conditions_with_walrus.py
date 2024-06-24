def f(x, y):
    if y > (value := x if x > 5 else 5):
        print(f"{y=} {value=} {x=}")

def f2():
    counter = 0
    while captcha := True:
        counter += 1
        print(counter)
        if counter == 5:
            captcha = False


def main() -> None:
    print(f"Hello main from : {__file__}")
    f(6, 7)
    f(3, 9)
    f2()


if __name__ == "__main__":
    main()
