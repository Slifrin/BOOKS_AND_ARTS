import re


def from_question():
    text = "bob sue jon richard harry"
    pat = re.compile(r"(?P<name>[a-z]+)\s+(?P<name2>[a-z]+)")
    print(re.findall(pat, text))


def from_answer():
    text = "bob sue jon richard harry"
    pat = re.compile(r"(?P<name>[a-z]+)\s+(?P<name2>[a-z]+)")

    print([m for m in pat.finditer(text)])
    print([m.groupdict() for m in pat.finditer(text)])


def main() -> None:
    print(f"Hello main from : {__file__}")
    from_question()
    from_answer()


if __name__ == "__main__":
    main()
