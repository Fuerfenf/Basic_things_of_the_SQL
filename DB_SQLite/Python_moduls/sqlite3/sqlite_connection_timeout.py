import sqlite3


def readSqliteTable():
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db', timeout=20)
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT count(*) from SqliteDb_developers"""
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchone()
        print("Total rows are:  ", totalRows)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("The Sqlite connection is closed")

readSqliteTable()