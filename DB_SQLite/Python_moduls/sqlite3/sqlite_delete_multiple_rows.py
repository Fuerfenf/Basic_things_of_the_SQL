import sqlite3

def deleteMultipleRecords(idList):
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test(b).db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")
        sqlite_update_query = """DELETE from SqliteDb_developers where id = ?"""

        cursor.executemany(sqlite_update_query, idList)
        db_connect.commit()
        print("Total", cursor.rowcount, "Records deleted successfully")
        db_connect.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete multiple records from sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("sqlite connection is closed")

idsToDelete = [(4,),(3,)]
deleteMultipleRecords(idsToDelete)