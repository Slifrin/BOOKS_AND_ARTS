import functools
import sys

def cache_examples():
    @functools.cache
    def factorial(n):
        print(f"call {n=}")
        return n * factorial(n - 1) if n else 1

    print(factorial(11))
    print("-" * 10)
    print(factorial(5))

    @functools.lru_cache(maxsize=50)
    def count_vowels(sentence: str):
        print(f"Executing count for {sentence}")
        return sum(sentence.count(vowel) for vowel in "AEIOUaeiou")

    print(count_vowels("Hello there"))
    print(count_vowels("Hello there"))

def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    cache_examples()

if __name__ == '__main__':
    main()