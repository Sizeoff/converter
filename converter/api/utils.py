import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

TABLE = os.environ.get('TABLE')

dsn = {
    'dbname': os.environ.get('DBNAME'),
    'user': os.environ.get('USER'),
    'password': os.environ.get('PASSWORD'),
    'host': '127.0.0.1',
    'port': 5432,
    'options': '-c search_path=content'
}


def psql_save(currency):
    try:
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
            s_string = ', '.join(['%s'] * len(currency))
            cols = cursor.mogrify(s_string, list(currency.keys())).decode()
            cols = cols.replace("'", "")

            values = cursor.mogrify(s_string,
                                    list(currency.values())).decode()
            values = values.replace("\n", "")

            query = "INSERT INTO {} ({}) VALUES ({});".format(
                TABLE, cols, values)

            cursor.execute(query)

    except Exception as e:
        print(e)


def check_existance(currency, merge):
    name_from = currency['name_from']
    name_to = currency['name_to']

    try:
        with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:

            query = f'''SELECT EXISTS (SELECT * FROM {TABLE} 
            WHERE name_from='{name_from}' AND name_to='{name_to}');'''

            cursor.execute(query)
            existance = cursor.fetchall()

            if not existance[0][0]:
                psql_save(currency)
            else:
                if merge:
                    amount = currency['amount']
                    value = currency['value']
                    query = f'''UPDATE {TABLE} SET amount = {amount}, 
                    value = {value} WHERE name_from='{name_from}'
                    AND name_to='{name_to}';'''

                    cursor.execute(query)

    except Exception as e:
        print(e)
