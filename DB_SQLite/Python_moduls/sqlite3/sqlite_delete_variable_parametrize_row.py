import sqlite3


def deleteSqliteRecord(id):
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test(b).db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        sql_update_query = """DELETE from SqliteDb_developers where id = ?"""
        cursor.execute(sql_update_query, (id, ))
        db_connect.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("sqlite connection is closed")

deleteSqliteRecord(9)