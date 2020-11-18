import sqlite3

def updateMultipleColumns(id, salary, email):
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        sqlite_update_query = """Update SqliteDb_developers set salary = ?, email = ? where id = ?"""
        columnValues = (salary, email, id)
        cursor.execute(sqlite_update_query, columnValues)
        db_connect.commit()
        print("Multiple columns updated successfully")
        db_connect.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update multiple columns of sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("sqlite connection is closed")

updateMultipleColumns(3, 6500, 'ben_stokes@gmail.com')