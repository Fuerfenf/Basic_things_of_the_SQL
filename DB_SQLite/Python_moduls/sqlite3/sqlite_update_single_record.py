"""
Note: If you are doing multiple update operations and wanted to revert your change in case of failure of any of
the operations, use the rollback() function of connection class to revert the changes. Use rollback()
function in except block.
"""
import sqlite3


def updateSqliteTable():
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update SqliteDb_developers set salary = 11000 where id = 4"""
        cursor.execute(sql_update_query)
        db_connect.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("The SQLite connection is closed")

updateSqliteTable()