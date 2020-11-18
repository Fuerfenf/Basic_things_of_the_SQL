import sqlite3


def deleteRecord():
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test(b).db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        # Deleting single record now
        sql_delete_query = """DELETE from SqliteDb_developers where id = 1212"""
        cursor.execute(sql_delete_query)
        db_connect.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("the sqlite connection is closed")

deleteRecord()