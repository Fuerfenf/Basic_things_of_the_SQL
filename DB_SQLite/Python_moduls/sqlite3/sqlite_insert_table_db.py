import sqlite3

try:
    db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
    sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                joining_date datetime,
                                salary REAL NOT NULL);'''

    cursor = db_connect.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    db_connect.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (db_connect):
        db_connect.close()
        print("sqlite connection is closed")
