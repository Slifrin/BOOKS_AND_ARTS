"""
    django doc
"""

import django



def main() -> None:
    print(f'Hello main from : {__file__}')
    print("info about django version", django.get_version())

if __name__ == '__main__':
    main()