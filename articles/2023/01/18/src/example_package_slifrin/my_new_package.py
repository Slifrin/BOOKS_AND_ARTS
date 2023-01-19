"""
    https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
"""


DAYS = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thrusday",
    5: "Friday",
    6: "Saturday",
}

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False


def get_month_offset(month, is_leap_year):
    normal_year = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    leap_yer = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
    if is_leap_year:
        return leap_yer[month - 1]
    return normal_year[month - 1]


def gregorian_gauss_day_of_the_week(year, month, day):
    # determine day of the week of 1 January
    # wiki has some problem :(
    first_january = (1 + 5 * ((year - 1) % 4) + 4 * ((year - 1) % 100) + 6 * ((year - 1) % 400)) % 7
    print(first_january)
    month_offset = get_month_offset(month, is_leap_year(year))
    week_day = (first_january + month_offset + day - 1) % 7
    day_name = DAYS[week_day]
    print(f"{year=}::{month=}::{day=} ---> {day_name}")



def main() -> None:
    print(f'Hello main from : {__file__}')
    gregorian_gauss_day_of_the_week(2000, 1, 1)
    gregorian_gauss_day_of_the_week(2023, 1, 15)
    gregorian_gauss_day_of_the_week(1777, 4, 30)
    gregorian_gauss_day_of_the_week(1855, 2, 23)

    print(1992, is_leap_year(1992))
    print(2000, is_leap_year(2000))
    print(1900, is_leap_year(1900))

if __name__ == '__main__':
    main()