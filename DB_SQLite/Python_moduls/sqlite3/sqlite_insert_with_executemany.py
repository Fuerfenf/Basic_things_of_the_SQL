import sqlite3


def insertMultipleRecords(recordList):
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          VALUES (?, ?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, recordList)
        db_connect.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into SqliteDb_developers table")
        db_connect.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("The SQLite connection is closed")


recordsToInsert = [(5, 'Jose', 'jose@gmail.com', '2022-01-14', 9111),
                   (6, 'Chris', 'chris@gmail.com', '2019-05-15',7600),
                   (7, 'Jonny', 'jonny@gmail.com', '2019-03-27', 8400)]

insertMultipleRecords(recordsToInsert)