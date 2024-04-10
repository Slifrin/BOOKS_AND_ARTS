from statistics import mode




def main() -> None:
    print(f'Hello main from : {__file__}')
    items = [
        {"a": "aa", "b": "bb"},
        {"a": "a", "b": "bb"},
        {"a": "aaa", "b": "bb"},
        {"a": "aaa", "b": "bb"},
        {"a": "aaa", "b": "bb"},
    ]

    print(mode([item["a"] for item in items]))

if __name__ == '__main__':
    main()