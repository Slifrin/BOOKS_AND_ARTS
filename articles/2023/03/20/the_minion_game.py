import itertools
import operator
import re

VOWELS = ["A", "E", "I", "O", "U"]

def is_vowel(c):
    if c in VOWELS:
        return True
    return False


def firs_letter_is_vovel(s: str):
    return is_vowel(s[0])


def my_count(s:str, ss:str):
    s_len = len(s)
    ss_len = len(ss)
    counter = 0
    i = s.find(ss)
    while i > -1 and (s_len - i - ss_len) >= 0:
        i = s.find(ss, i + 1)
        counter += 1
    return counter

def minion_game(s: str):
    checked_sub_str = set()
    counter_v = 0
    counter_c = 0
    s_len = len(s)
    for i, c in enumerate(s):
        for j in range(i + 1, s_len + 1):
            if s[i:j] not in checked_sub_str:
                number = s.count(s[i:j])
                if firs_letter_is_vovel(s[i:j]):
                    counter_v += number
                else:
                    counter_c += number
                checked_sub_str.add(s[i:j])
    if counter_v > counter_c:
        print(f"Kevin {counter_v}")
    elif counter_v < counter_c:
        print(f"Stuart {counter_c}")
    else:
        print("Draw")

def minion_game2(s: str):
    vowels = "AEIOU"
    checked_sub_str = set()
    counter_v = 0
    counter_c = 0
    s_len = len(s)
    for i, c in enumerate(s):
        for j in range(i + 1, s_len + 1):
            ss = s[i:j]
            if ss not in checked_sub_str:
                if ss[0] in vowels:
                    counter_v += my_count(s, ss)
                else:
                    counter_c += my_count(s, ss)
                checked_sub_str.add(ss)

    if counter_v > counter_c:
        print(f"Kevin {counter_v}")
    elif counter_v < counter_c:
        print(f"Stuart {counter_c}")
    else:
        print("Draw")

def subslices(seq):

    slices = itertools.starmap(slice, itertools.combinations(range(len(seq) + 1), 2))
    return map(operator.getitem, itertools.repeat(seq), slices)


def minion_game3(s: str):
    vowels = "AEIOU"
    counter_v = 0
    counter_c = 0
    possible_str = set(subslices(s))
    for ss in possible_str:
        # print(ss)
        if ss[0] in vowels:
            counter_v += my_count(s, ss)
        else:
            counter_c += my_count(s, ss)
    if counter_v > counter_c:
        print(f"Kevin {counter_v}")
    elif counter_v < counter_c:
        print(f"Stuart {counter_c}")
    else:
        print("Draw")

def minion_game4(s: str):
    """ there are n+(n-1)+(n-2)+...+2+1=n(n+1)/2 substrings in a word of length n. Therefore,
        since any substring starts exclusively with either a vowel or a consonant, we only
        need to count the number of substrings starting with a vowel and subtract from the total
        number of substrings to get the number of substrings starting with a consonant, or vice versa.
    """
    vowels = "AEIOU"
    counter_v = 0
    counter_c = 0
    for i in range(len(s)):
        if s[i] in vowels:
            counter_v += len(s) - i
        else:
            counter_c += len(s) - i
    if counter_v > counter_c:
        print(f"Kevin {counter_v}")
    elif counter_v < counter_c:
        print(f"Stuart {counter_c}")
    else:
        print("Draw")

def main() -> None:
    print(f'Hello main from : {__file__}')
    # minion_game2("BANANA")
    minion_game2("BAANANAS")
    # minion_game2("")
    # minion_game2("A")
    # minion_game2("B")
    minion_game4("BAANANAS")



if __name__ == '__main__':
    main()