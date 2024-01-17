

def main() -> None:
    print(f'Hello main from : {__file__}')

    with open("day1.txt", "r") as input_f:
        ssum_of_numbers = 0
        for line in input_f.readlines():
            first_digit = None
            second_digit = None
            for char in line:
                if char.isdigit():
                    first_digit = int(char) * 10
                    break
            for char in reversed(line):
                if char.isdigit():
                    second_digit = int(char)
                    break
            ssum_of_numbers += first_digit + second_digit
        print(ssum_of_numbers)

if __name__ == '__main__':
    main()