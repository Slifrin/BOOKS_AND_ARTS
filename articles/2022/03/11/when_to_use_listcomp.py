"""
    https://realpython.com/list-comprehension-python/
"""

import random

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

def some_conditions():
    sentence = 'the rocket came back from mars'
    vowels = [i for i in sentence if i in 'aeiou']
    print(vowels)

    original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
    prices = [i if i > 0 else 0 for i in original_prices]
    print(prices)


def set_comprahension():
    quote = "life, uh, finds a way"
    uniq_vowels = {i for i in quote if i in 'aeiou'}
    print(uniq_vowels)

def dic_comprehension():
    squares = {i : i*i for i in range(10)}
    print(squares)

def using_walrus_operator():
    def get_weather_data():
        return random.randrange(90, 110)
    hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
    print(hot_temps)


def main():
    print(f'Hello main from : {__file__}')
    numbers = [(x, y) for x in range(5) for y in range(4)]
    for pair in numbers:
        print(pair)
    
    some_conditions()

    set_comprahension()
    dic_comprehension()

    using_walrus_operator()

if __name__ == '__main__':
    main()