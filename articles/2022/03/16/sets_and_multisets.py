from collections import Counter


def main():
    print(f'Hello main from : {__file__}')
    vowels = frozenset({"a", "e", "i", "o", "u"})
    letters = set("alice")
    print(letters.intersection(vowels))


if __name__ == '__main__':
    main()