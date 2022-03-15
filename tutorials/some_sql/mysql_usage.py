
import os 

import mysql.connector as mysql




def main():
    print('Hello main')
    passwd = os.environ.get('PASSSQL')

    db = mysql.connect(
        host='localhost',
        user='root',
        passwd=passwd,
    )

    print(db)

if __name__ == '__main__':
    main()