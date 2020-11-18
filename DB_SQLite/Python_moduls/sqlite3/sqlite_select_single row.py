import sqlite3


def readSingleRow(developerId):
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from SqliteDb_developers where id = ?"""
        cursor.execute(sqlite_select_query, (developerId, ))
        print("Reading single row \n")
        record = cursor.fetchone()
        print("Id: ", record[0])
        print("Name: ", record[1])
        print("Email: ", record[2])
        print("JoiningDate: ", record[3])
        print("Salary: ", record[4])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("The SQLite connection is closed")

readSingleRow(2) # take id witch row chosen
