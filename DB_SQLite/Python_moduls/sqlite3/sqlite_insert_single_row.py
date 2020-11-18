import sqlite3


try:
    db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
    cursor = db_connect.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                           VALUES 
                          (9,'James','jame2s@pynative.com','2019-03-17',8000)"""

    count = cursor.execute(sqlite_insert_query)
    db_connect.commit() # Nesesary to make our changes persistent in the database.
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (db_connect):
        db_connect.close()
        print("The SQLite connection is closed")