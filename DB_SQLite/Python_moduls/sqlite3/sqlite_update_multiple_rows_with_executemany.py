import sqlite3


def updateMultipleRecords(recordList):
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        sqlite_update_query = """Update SqliteDb_developers set salary = ? where id = ?"""
        cursor.executemany(sqlite_update_query, recordList)
        db_connect.commit()
        print("Total", cursor.rowcount, "Records updated successfully")
        db_connect.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update multiple records of sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("The SQLite connection is closed")

records_to_update = [ (9700, 4), (7800, 5), (8400, 6) ]
updateMultipleRecords(records_to_update)