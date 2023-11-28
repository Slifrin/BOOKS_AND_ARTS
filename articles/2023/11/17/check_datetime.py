import datetime

import pendulum


DATE_FORMAT = "%m-%d-%Y"

def main() -> None:
    print(f'Hello main from : {__file__}')
    now = datetime.datetime.now()
    weeks_ago = now - datetime.timedelta(weeks=8)
    print(weeks_ago)

    now2 = pendulum.now()
    print(now2.subtract(months=2).strftime(DATE_FORMAT))

if __name__ == '__main__':
    main()