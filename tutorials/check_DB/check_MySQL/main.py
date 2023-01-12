from getpass import getpass
from mysql.connector import connect, Error


def check_connection_to_db():
    try:
        with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
        ) as connection:
            print(connection)
    except Error as e:
        print("Run into problems: ", e)

def main():
    print(f"Hello there from main {__file__}")
    check_connection_to_db()

if __name__ == "__main__":
    main()