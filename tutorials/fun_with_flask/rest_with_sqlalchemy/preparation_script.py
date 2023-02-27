import sqlite3

from pprint import pformat

from logzero import logger

TABLE_NAME = "person"
GET_TABLE_NAMES = "SELECT name FROM sqlite_master WHERE type = 'table';"


def creation(conn: sqlite3.Connection):
    columns = [
        "id INTEGER PRIMARY KEY",
        "lname VARCHAR UNIQUE",
        "fname VARCHAR",
        "timestamp DATETIME",
    ]
    create_table_cmd = f"CREATE TABLE {TABLE_NAME} ({','.join(columns)})"
    conn.execute(create_table_cmd)


def insert_initial_data(conn: sqlite3.Connection):
    people = [
        "1, 'Fairy', 'Tooth', '2023-02-27 10:15:05'",
        "2, 'Ruprecht', 'Knecht', '2023-02-27 10:15:10'",
        "3, 'Bunny', 'Easter', '2023-02-27 10:15:15'",
    ]
    for person_data in people:
        insert_cmd = f"INSERT INTO person VALUES ({person_data})"
        conn.execute(insert_cmd)
    conn.commit()


def check_people_table_exists(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute(GET_TABLE_NAMES)
    table_names = cur.fetchall()

    for row in table_names:
        if TABLE_NAME in row:
            return True
    return False


def show_table_content(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {TABLE_NAME};")
    table_names = cur.fetchall()
    logger.info(f"Show contetn of table {TABLE_NAME}")
    logger.info(pformat(table_names))


def main() -> None:
    print(f"Hello main from : {__file__}")
    conn = sqlite3.connect("people.db")
    if check_people_table_exists(conn):
        logger.info(f"Table: {TABLE_NAME} already exist")
    else:
        logger.info(f"Creating table: {TABLE_NAME}")
        creation(conn)
        insert_initial_data(conn)

    show_table_content(conn)

if __name__ == "__main__":
    main()
