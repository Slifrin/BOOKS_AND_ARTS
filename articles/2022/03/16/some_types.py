"""
    https://docs.python.org/3/library/typing.html
"""

from typing import NewType


UserId = NewType('UserId', int)

def get_userID(user_id: UserId) -> str:
    print("Some user ID", user_id)
    return str(user_id)

def greeting(name: str) -> str:
    return 'Hello ' + name

def p() -> None:
    print('hello')

def main():
    print(f'Hello main from : {__file__}')
    output = UserId(23413) + UserId(54341)
    print(type(output))
    print(output)
    get_userID(output)
    get_userID('123')
    

    greeting(3)
    greeting(b'Alice')
    a = p()

if __name__ == '__main__':
    main()
