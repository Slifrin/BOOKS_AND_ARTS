
import sqlite3

conn = sqlite3.connect('check_fun.db')

class Field:
    def __set_name__(self, owner, name):
        self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key}=?;'
        self.store = f'UPDATE {owner.table} SET {name}=? WHERE {owner.key}=?'

    def __get__(self, obj, objtype=None):
        return conn.execute(self.fetch, [obj.key]).fetchall()[0]

    def __set__(self, obj, value):
        """ Options for checking if data exists in DB """
        conn.execute(self.store, [value, obj.key])
        conn.commit()

class Movie:
    table = 'Movies'
    key = 'title'
    director = Field()
    year = Field()

    def __init__(self, key) -> None:
        self.key = key

class Song:
    table = 'Music'
    key = 'title'
    artist = Field()
    year = Field()
    genre = Field()

    def __init__(self, key) -> None:
        self.key = key


def main() -> None:
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()