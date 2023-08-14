import unicodedata
import itertools


def main() -> None:
    print(f'Hello main from : {__file__}')
    for i in itertools.count():
        try:
            c = chr(i)
        except UnicodeEncodeError:
            print("Last character ", i)
            break
        try:
            char_name = unicodedata.name(chr(i))
        except ValueError:
            char_name = " -- No name for this char -- "

        try:
            print(f"{c}  {char_name}")
        except UnicodeEncodeError:
            print(f"Can't encode {i}")
            continue
        


if __name__ == '__main__':
    main()