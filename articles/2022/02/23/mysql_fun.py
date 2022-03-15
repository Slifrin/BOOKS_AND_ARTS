from mysql.connector import connect, Error
from getpass import getpass

import sys
print(sys.executable)


def connect_db():
    try:
        with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password"),
        ) as connection:
            print(connection)
            with connection.cursor(buffered=True) as cursor:
                create_db_query = "CREATE DATABASE online_movie_rating"
                show_db_query = "SHOW DATABASES"
                
                print(cursor.execute(show_db_query))
                # cursor.execute(create_db_query)

    except Error as e:
        print(e)


def main():
    print('Hello main')
    connect_db()

if __name__ == '__main__':
    main()


