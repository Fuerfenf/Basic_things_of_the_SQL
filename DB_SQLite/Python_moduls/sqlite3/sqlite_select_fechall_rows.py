import sqlite3

import sqlite3

def readSqliteTable():
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from SqliteDb_developers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print(row)
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Email: ", row[2])
            print("JoiningDate: ", row[3])
            print("Salary: ", row[4])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("The SQLite connection is closed")

readSqliteTable()