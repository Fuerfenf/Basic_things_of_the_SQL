import sqlite3
import traceback
import sys

try:
    db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
    cursor = db_connect.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO unknown_table_1
                          (id, text)  VALUES  (1, 'Demo Text')"""

    count = cursor.execute(sqlite_insert_query)
    db_connect.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table")
    print("Exception class is: ", error.__class__)
    print("Exception is", error.args)
    print('Printing detailed SQLite exception traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (db_connect):
        db_connect.close()
        print("The SQLite connection is closed")