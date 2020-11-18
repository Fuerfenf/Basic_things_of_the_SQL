import sqlite3


def lower(string):
    return str(string).lower()


def getDeveloperName(id):
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        db_connect.create_function("lower", 1, lower)
        select_query = "SELECT lower(name) FROM SqliteDb_developers where id = ?"
        cursor.execute(select_query, (id,))
        name = cursor.fetchone()
        print("Developer Name is", name)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("sqlite connection is closed")


getDeveloperName(1)