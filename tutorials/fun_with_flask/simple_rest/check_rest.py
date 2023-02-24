
from datetime import datetime, timezone

from flask import Flask, request, jsonify
from dotenv import load_dotenv, dotenv_values
import psycopg2


app = Flask(__name__)

config = dotenv_values()

connection = psycopg2.connect(
    host=config['HOST'],
    database=config['DATABASE'],
    user=config['USER'],
    password=config['PASSWORD'],
)


CREATE_ROOM_TABLE = "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"
INSERT_ROOM_DATA = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"

CREATE_TEMPERATURES_TABLE = """CREATE TABLE IF NOT EXISTS temperatures (room_id INTEGER, temperature REAL, 
date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"""
INSERT_TEPMERATURE = "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);"


@app.route("/")
def hello_there():
    with connection:
        with connection.cursor() as cur:
            cur.execute('SELECT version()')

            db_version = cur.fetchone()

    return f"Hello there posgres {db_version}\n"


@app.post("/api/room")
def create_room():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cur:
            cur.execute(CREATE_ROOM_TABLE)

            cur.execute(INSERT_ROOM_DATA, (name, ))
            try:
                room_id = cur.fetchone()[0]
            except TypeError:
                return "tarapaty", 500
            return jsonify({"id": room_id, "message": f"Room {name} created."}), 201


@app.post("/api/temperature")
def add_temp():
    data = request.get_json()
    temperature = data["temperature"]
    room_id = data["room"]
    try:
        date = datetime.strptime(data["date"], "%m-%d-%Y %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)
    with connection:
        with connection.cursor() as cur:
            cur.execute(CREATE_TEMPERATURES_TABLE)
            cur.execute(INSERT_TEPMERATURE, (room_id, temperature, date))
            
            return jsonify({"message": "Temperature added."}), 201


@app.route("/api/rooms/all")
def show_all_rooms():
    with connection:
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM rooms;")
            for row in cur.fetchall():
                print(row)
        return "Ok I think", 201


@app.get("/api/average")
def get_global_avg():
    GLOBAL_NUMBER_OF_DAYS = """SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures;"""
    GLOBAL_AVG = """SELECT AVG(temperature) as average FROM temperatures;"""
    with connection:
        with connection.cursor() as cur:
            cur.execute(GLOBAL_AVG)
            average = cur.fetchone()[0]
            cur.execute(GLOBAL_NUMBER_OF_DAYS)
            days = cur.fetchone()[0]
        return jsonify({"average": round(average, 2), "days": days})


def get_rom_term(room_id, term, room_id_query):
    ROOM_TERM = """SELECT
        DATE(temperatures.date) as reading_date, AVG(temperatures.temperature)
        FROM temperatures
        WHERE temperatures.room_id = (%s)
        GROUP BY reading_date
        HAVING DATE(temperatures.date) > (SELECT MAX(DATE(temperatures.date))-(%s) FROM temperatures);
    """
    terms = {"week": 7, "month": 30}
    with connection:
        with connection.cursor() as cur:
            cur.execute(room_id_query, (room_id,))
            room_name = cur.fetchone()[0]
            cur.execute(ROOM_TERM, (room_id, terms[term]))
            dates_temperature = cur.fetchall()

            average = sum(day[1] for day in dates_temperature) / len(dates_temperature)
        return jsonify({
            "name": room_name,
            "temperatures": dates_temperature,
            "average": round(average, 2)
        })


@app.get("/api/room/<int:room_id>")
def get_room_all(room_id):
    ROOM_NAME = """SELECT name FROM rooms WHERE id = (%s)"""
    ROOM_NUMBER_OF_DAYS = """SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures WHERE room_id = (%s);"""
    ROOM_ALL_TIME_AVG = "SELECT AVG(temperature) as average FROM temperatures WHERE room_id = (%s);"

    term = request.args.get("term", None)
    if term is not None:
        return get_room_all(room_id, ROOM_NAME)

    with connection:
        with connection.cursor() as cur:
            cur.execute(ROOM_NAME, (room_id,))
            name = cur.fetchone()[0]

            cur.execute(ROOM_ALL_TIME_AVG, (room_id,))
            average = cur.fetchone()[0]

            cur.execute(ROOM_NUMBER_OF_DAYS, (room_id,))
            days = cur.fetchone()[0]

        return jsonify({"name": name, "average": round(average, 2), "days": days})


def main() -> None:
    print(f'Hello main from : {__file__}')
    app.run(debug=True)

if __name__ == '__main__':
    main()