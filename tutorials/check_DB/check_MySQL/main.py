import json
import os
import textwrap

from functools import wraps
from pathlib import Path
from pprint import pprint
from typing import Callable, Optional


from getpass import getpass
from mysql.connector import connect, Error
from mysql.connector.connection_cext import CMySQLConnection, CMySQLCursor

DB_NAME = "online_movie_rating"


def draw_additional_line(_func:Optional[Callable], *, character:str="*", lenght:int=100):
    def decorator_draw_additional_lines(func:Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(character * (lenght // 2), func.__name__, character * (lenght // 2))
            ret_val = func(*args, **kwargs)
            return ret_val
        return wrapper
    if not _func:
        return decorator_draw_additional_lines
    else:
        return decorator_draw_additional_lines(_func)
    

def get_secrets():
    """Not so safe."""
    secrets_f = Path("secrets.json")  # check it little more
    content = secrets_f.read_text()
    secrets = json.loads(content)
    # print(secrets)
    return secrets


def check_connection_to_db() -> bool:
    secrets = get_secrets()
    try:
        with connect(
            host="localhost",
            # user=input("Enter username: "),
            user=secrets["user"],
            # password=getpass("Enter password: "),
            password=secrets["password"],
        ) as connection:
            print(connection)
            print(type(connection))
            existing_dbs = get_available_dbs(connection)
            if DB_NAME not in existing_dbs:
                create_db(connection)
    except Error as e:
        print("Run into problems: ", e)
        return False
    return True


def get_available_dbs(connection_to_engine: CMySQLConnection):
    existing_dbs = []
    with connection_to_engine.cursor() as cursor:
        cursor.execute(f"SHOW DATABASES")
        for db in cursor:
            print(db)
            existing_dbs.append(db[0])
    return existing_dbs


def create_db(connection_to_engine: CMySQLConnection):
    # no semicolon is needed as it is handled by the MySQL python connector
    create_db_query = f"CREATE DATABASE {DB_NAME}"
    with connection_to_engine.cursor() as cursor:
        cursor.execute(create_db_query)


def connect_to_existing_db(db_name: str, tasks: list[Callable]):
    secrets = get_secrets()
    try:
        with connect(
            host="localhost",
            user=secrets["user"],
            password=secrets["password"],
            database=db_name,
        ) as connection:
            print("2", connection)
            for task in tasks:
                task(connection)
    except Exception as e:
        print("Run into problems: ", e)


def create_tables(db_connection: CMySQLConnection):
    create_movies_table_query = """
    CREATE TABLE movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        genre VARCHAR(100),
        collection_in_mil INT
    )
    """
    create_reviewers_table_query = """
    CREATE TABLE reviewers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
    )
    """
    create_ratings_table_query = """
    CREATE TABLE ratings (
        movie_id INT,
        reviewer_id INT,
        rating DECIMAL(2,1),
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
        PRIMARY KEY(movie_id, reviewer_id)
    )
    """
    with db_connection.cursor() as cursor:
        cursor.execute(textwrap.dedent(create_movies_table_query))
        db_connection.commit()
        cursor.execute(textwrap.dedent(create_reviewers_table_query))
        db_connection.commit()
        cursor.execute(textwrap.dedent(create_ratings_table_query))
        db_connection.commit()


def show_table_schema(db_connection: CMySQLConnection):
    tables = [
        "movies",
        "reviewers",
        "ratings",
    ]
    with db_connection.cursor() as cursor:
        for table in tables:
            query = f"DESCRIBE {table}"
            cursor.execute(query)
            # Fetch rows from last executed query
            result = cursor.fetchall()
            print(f"INFO about {table}")
            for row in result:
                print(row)


def modify_column_type(db_connection: CMySQLConnection):
    alter_table_query = """
    ALTER TABLE movies
    MODIFY COLUMN collection_in_mil DECIMAL(4,1)
    """
    show_table_query = "DESCRIBE movies"
    with db_connection.cursor() as cursor:
        cursor.execute(textwrap.dedent(alter_table_query))
        cursor.execute(show_table_query)
        # called only once
        result = cursor.fetchall()
        print("Movie Table Schema after alteration:")
        for row in result:
            print(row)


def delete_table(db_connection: CMySQLConnection):
    drop_ratings_query = "DROP TABLE ratings"
    with db_connection.cursor() as cursor:
        cursor.execute(drop_ratings_query)


def check_if_tables_exist(db_connection: CMySQLConnection):
    tables = [
        "movies",
        "reviewers",
        "ratings",
    ]
    with db_connection.cursor() as cursor:
        for table in tables:
            check_schema_query = textwrap.dedent(
                f"""
            SELECT * 
            FROM information_schema.tables
            WHERE table_schema = '{DB_NAME}' 
                AND table_name = '{table}'
            LIMIT 1;
            """
            )
            # pprint(check_schema_query)
            cursor.execute(check_schema_query)
            result = cursor.fetchall()
            print(f"Does {table} exist? {bool(result)}")
            

def insert_dummy_movie_data(db_connection: CMySQLConnection):
    insert_movies_query = """
    INSERT INTO movies (title, release_year, genre, collection_in_mil)
    VALUES
        ("Forrest Gump", 1994, "Drama", 330.2),
        ("3 Idiots", 2009, "Drama", 2.4),
        ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
        ("Good Will Hunting", 1997, "Drama", 138.1),
        ("Skyfall", 2012, "Action", 304.6),
        ("Gladiator", 2000, "Action", 188.7),
        ("Black", 2005, "Drama", 3.0),
        ("Titanic", 1997, "Romance", 659.2),
        ("The Shawshank Redemption", 1994, "Drama",28.4),
        ("Udaan", 2010, "Drama", 1.5),
        ("Home Alone", 1990, "Comedy", 286.9),
        ("Casablanca", 1942, "Romance", 1.0),
        ("Avengers: Endgame", 2019, "Action", 858.8),
        ("Night of the Living Dead", 1968, "Horror", 2.5),
        ("The Godfather", 1972, "Crime", 135.6),
        ("Haider", 2014, "Action", 4.2),
        ("Inception", 2010, "Adventure", 293.7),
        ("Evil", 2003, "Horror", 1.3),
        ("Toy Story 4", 2019, "Animation", 434.9),
        ("Air Force One", 1997, "Drama", 138.1),
        ("The Dark Knight", 2008, "Action",535.4),
        ("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
        ("The Lion King", 1994, "Animation", 423.6),
        ("Pulp Fiction", 1994, "Crime", 108.8),
        ("Kai Po Che", 2013, "Sport", 6.0),
        ("Beasts of No Nation", 2015, "War", 1.4),
        ("Andadhun", 2018, "Thriller", 2.9),
        ("The Silence of the Lambs", 1991, "Crime", 68.2),
        ("Deadpool", 2016, "Action", 363.6),
        ("Drishyam", 2015, "Mystery", 3.0)
    """
    with db_connection.cursor() as cursor:
        cursor.execute(insert_movies_query)
        db_connection.commit()

def insert_dummy_reviewers_data(db_connection: CMySQLConnection):
    insert_reviewers_query = """
    INSERT INTO reviewers
    (first_name, last_name)
    VALUES ( %s, %s )
    """
    reviewers_records = [
        ("Chaitanya", "Baweja"),
        ("Mary", "Cooper"),
        ("John", "Wayne"),
        ("Thomas", "Stoneman"),
        ("Penny", "Hofstadter"),
        ("Mitchell", "Marsh"),
        ("Wyatt", "Skaggs"),
        ("Andre", "Veiga"),
        ("Sheldon", "Cooper"),
        ("Kimbra", "Masters"),
        ("Kat", "Dennings"),
        ("Bruce", "Wayne"),
        ("Domingo", "Cortes"),
        ("Rajesh", "Koothrappali"),
        ("Ben", "Glocker"),
        ("Mahinder", "Dhoni"),
        ("Akbar", "Khan"),
        ("Howard", "Wolowitz"),
        ("Pinkie", "Petit"),
        ("Gurkaran", "Singh"),
        ("Amy", "Farah Fowler"),
        ("Marlon", "Crafford"),
    ]
    with db_connection.cursor() as cursor:
        cursor.executemany(insert_reviewers_query, reviewers_records)
        db_connection.commit()

def insert_dummy_ratings_data(db_connection: CMySQLConnection):
    insert_ratings_query = """
    INSERT INTO ratings
    (rating, movie_id, reviewer_id)
    VALUES ( %s, %s, %s)
    """
    ratings_records = [
        (6.4, 17, 5), (5.6, 19, 1), (6.3, 22, 14), (5.1, 21, 17),
        (5.0, 5, 5), (6.5, 21, 5), (8.5, 30, 13), (9.7, 6, 4),
        (8.5, 24, 12), (9.9, 14, 9), (8.7, 26, 14), (9.9, 6, 10),
        (5.1, 30, 6), (5.4, 18, 16), (6.2, 6, 20), (7.3, 21, 19),
        (8.1, 17, 18), (5.0, 7, 2), (9.8, 23, 3), (8.0, 22, 9),
        (8.5, 11, 13), (5.0, 5, 11), (5.7, 8, 2), (7.6, 25, 19),
        (5.2, 18, 15), (9.7, 13, 3), (5.8, 18, 8), (5.8, 30, 15),
        (8.4, 21, 18), (6.2, 23, 16), (7.0, 10, 18), (9.5, 30, 20),
        (8.9, 3, 19), (6.4, 12, 2), (7.8, 12, 22), (9.9, 15, 13),
        (7.5, 20, 17), (9.0, 25, 6), (8.5, 23, 2), (5.3, 30, 17),
        (6.4, 5, 10), (8.1, 5, 21), (5.7, 22, 1), (6.3, 28, 4),
        (9.8, 13, 1)
    ]
    with db_connection.cursor() as cursor:
        cursor.executemany(insert_ratings_query, ratings_records)
        db_connection.commit()


def insert_dummy_data(db_connection: CMySQLConnection):
    insert_dummy_movie_data(db_connection)
    insert_dummy_reviewers_data(db_connection)
    insert_dummy_ratings_data(db_connection)
    
    
def read_data(db_connection: CMySQLConnection):
    select_movies_query = "SELECT * FROM movies LIMIT 5"
    other_movies_query = "SELECT * FROM movies LIMIT 2,5"
    filtered_movie_query = """
        SELECT title, collection_in_mil
        FROM movies
        WHERE collection_in_mil > 300
        ORDER BY collection_in_mil DESC
    """
    filtered_movie_query2 = """
        SELECT CONCAT(title, " (", release_year, ")"), collection_in_mil
        FROM movies 
        ORDER BY collection_in_mil DESC
        LIMIT 5;
    """
    with db_connection.cursor() as cursor:
        cursor.execute(select_movies_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        print("*" * 100)
        cursor.execute(other_movies_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        print("*" * 100)
        cursor.execute(textwrap.dedent(filtered_movie_query))
        result = cursor.fetchall()
        for row in result:
            print(row)
        print("*" * 100)
        cursor.execute(textwrap.dedent(filtered_movie_query2))
        result = cursor.fetchall()
        for row in result:
            print(row)

@draw_additional_line
def read_data_with_different_fetch(db_connection: CMySQLConnection):
    filtered_movie_query = """
        SELECT CONCAT(title, " (", release_year, ")"), collection_in_mil
        FROM movies 
        ORDER BY collection_in_mil DESC
    """
    with db_connection.cursor() as cursor:
        cursor.execute(filtered_movie_query)
        result = cursor.fetchmany(size=5)
        for row in result:
            print(row)

        # Clean all the remaining results that weren’t read by .fetchmany().
        # It’s necessary to clean all unread results before executing any other
        # statements on the same connection. Otherwise, an 
        # InternalError: Unread result found exception will be raised.

        rest_of_results = cursor.fetchall()
        print(len(rest_of_results))

@draw_additional_line
def some_joins(db_connection: CMySQLConnection):
    join_query = """
        SELECT title, AVG(rating) as average_rating
        FROM ratings
        INNER JOIN movies
            ON movies.id = ratings.movie_id
        GROUP BY movie_id
        ORDER BY average_rating DESC
        LIMIT 5
    """
    select_movies_query = """
        SELECT CONCAT(first_name, " ", last_name), COUNT(*) as num
        FROM reviewers
        INNER JOIN ratings
            ON reviewers.id = ratings.reviewer_id
        GROUP BY reviewer_id
        ORDER BY num DESC
        LIMIT 1
    """
    with db_connection.cursor() as cursor:
        cursor.execute(join_query)
        for movie in cursor.fetchall():
            print(movie)
        cursor.execute(select_movies_query)
        for reviewer in cursor.fetchall():
            print(reviewer)

@draw_additional_line
def update_data(db_connection: CMySQLConnection):
    update_query = """
        UPDATE
            reviewers
        SET
            last_name = "Cooper"
        WHERE
            first_name = "Amy"
    """
    with db_connection.cursor() as cursor:
        cursor.execute(update_query)
        db_connection.commit()

@draw_additional_line
def other_update_data_with_SQL_injection_threat(db_connection: CMySQLConnection):
    movie_id = input("Enter movie id: ")
    reviewer_id = input("Enter reviewer id: ")
    new_raiting = input("Enter new raiting: ")
    update_query = """
    UPDATE
        ratings
    SET
        rating = "%s"
    WHERE
        movie_id = "%s" AND reviewer_id = "%s";
    
    SELECT *
    FROM ratings
    WHERE
        movie_id = "%s" AND reviewer_id = "%s";
    """ % (new_raiting, movie_id, reviewer_id, movie_id, reviewer_id)
    
    with db_connection.cursor() as cursor:
        # to execute multiple querys in singe execute :) -- multi -- argument needs to be passed
        # If multi is True, then cursor.execute() returns an iterator.
        # Each item in the iterator corresponds to a cursor object that
        # executes a statement passed in the query. 
        for result in cursor.execute(update_query, multi=True):
            if result.with_rows:
                # Running .fetchall() on all cursor objects is important. To execute a new
                # statement on the same connection, you must ensure that there are no unread
                # results from previous executions. If there are unread results, then
                # you’ll receive an exception.
                print(result.fetchall())
        db_connection.commit()


@draw_additional_line
def other_update_data_with_some_mitigation_of_SQL_injection(db_connection: CMySQLConnection):
    movie_id = input("Enter movie id: ")
    reviewer_id = input("Enter reviewer id: ")
    new_raiting = input("Enter new raiting: ")

    # no quotes for %s placeholders !!!

    update_query = """
    UPDATE
        ratings
    SET
        rating = %s
    WHERE
        movie_id = %s AND reviewer_id = %s;
    
    SELECT *
    FROM ratings
    WHERE
        movie_id = %s AND reviewer_id = %s;
    """
    var_tuple = (
        new_raiting,
        movie_id,
        reviewer_id,
        movie_id,
        reviewer_id,
    )
    
    with db_connection.cursor() as cursor:
        # to execute multiple querys in singe execute :) -- multi -- argument needs to be passed
        # If multi is True, then cursor.execute() returns an iterator.
        # Each item in the iterator corresponds to a cursor object that
        # executes a statement passed in the query. 
        for result in cursor.execute(update_query, var_tuple, multi=True):
            if result.with_rows:
                # Running .fetchall() on all cursor objects is important. To execute a new
                # statement on the same connection, you must ensure that there are no unread
                # results from previous executions. If there are unread results, then
                # you’ll receive an exception.
                print(result.fetchall())
        db_connection.commit()


@draw_additional_line
def removal_of_data(db_connection: CMySQLConnection):
    select_movies_query = """
        SELECT reviewer_id, movie_id FROM ratings
        WHERE reviewer_id = 2
    """
    def _view_movies(cursor: CMySQLCursor):
        cursor.execute(select_movies_query)
        for movie in cursor.fetchall():
            print(movie)
    
    delete_query = "DELETE FROM ratings WHERE reviewer_id = 2"
    
    with db_connection.cursor() as cursor:
        _view_movies(cursor)
        
        # cursor.execute(delete_query)
        # db_connection.commit()
    
        _view_movies(cursor)


def main():
    print(f"Hello there from main {__file__}")
    if check_connection_to_db():
        connect_to_existing_db(
            DB_NAME,
            [
                # create_tables,
                # show_table_schema,
                # modify_column_type,
                # check_if_tables_exist,
                # insert_dummy_data,
                # read_data,
                # read_data_with_different_fetch,
                # some_joins,
                # update_data,
                # other_update_data_with_some_mitigation_of_SQL_injection,
                # removal_of_data,
            ],
        )


if __name__ == "__main__":
    main()
