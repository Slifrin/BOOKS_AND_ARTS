import pathlib
import string


def main() -> None:
    print(f"Hello main from : {__file__}")
    chars = string.ascii_uppercase
    data = [c1 + c2 for c1, c2 in zip(chars[:13], chars[13:])]
    pathlib.Path("rot13.txt").write_text("\n".join(data))

    pathlib.Path("empty_file.txt").touch()

    bbj = [98, 108, 229, 98, 230, 114, 115, 121, 108, 116, 101, 116, 248, 121]

    pathlib.Path("not_utf8.txt").write_bytes(bytes(bbj))


if __name__ == "__main__":
    main()
