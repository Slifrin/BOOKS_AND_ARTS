
import psycopg2
import requests

from dotenv import dotenv_values


CONFIG = dotenv_values()


def main() -> None:
    print(f'Hello main from : {__file__}')
    connection = psycopg2.connect(
        host=CONFIG['HOST'],
        database=CONFIG['DATABASE'],
        user=CONFIG['USER'],
        password=CONFIG['PASSWORD'],
    )
    inster_to_db = "INSERT INTO transactions (txid, uid, amount) VALUES (%s, %s, %s)"
    with connection:
        with connection.cursor() as cur:
            with requests.get('http://127.0.0.1:5000/very_large_request/1000000', stream=True) as r:
                buffer = ""
                for chunk in r.iter_content(chunk_size=1):
                    if chunk.endswith(b"\n"):
                        t = eval(buffer)
                        print(t)
                        if t[2] > 900:
                            # for align, text in zip('<^>', ['left', 'center', 'right']):
                            #     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
                            print("{0:*^40}".format(" A LOT OF MONEY "))
                        cur.execute(inster_to_db, (t[0], t[1], t[2]))
                        connection.commit()
                        buffer = ""
                    else:
                        buffer += chunk.decode()


if __name__ == '__main__':
    main()