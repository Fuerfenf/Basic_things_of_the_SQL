import sqlite3

try:
    db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
    cursor = db_connect.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (db_connect):
        db_connect.close()
        print("The SQLite connection is closed")