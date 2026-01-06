import sqlite3
import sys

import pandas as pd
import faker


def connect_to_db_and_create_tables():
    with sqlite3.connect("first_db.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)"
        )
        cursor.execute(
        "INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('John')"
        )
        connection.commit()


def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')

    connect_to_db_and_create_tables()


if __name__ == '__main__':
    main()