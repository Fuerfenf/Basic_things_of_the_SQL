import sqlite3


def updateSqliteTable(id, salary):
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update SqliteDb_developers set salary = ? where id = ?"""
        data = (salary, id)
        cursor.execute(sql_update_query, data)
        db_connect.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("The sqlite connection is closed")

updateSqliteTable(3, 7500)