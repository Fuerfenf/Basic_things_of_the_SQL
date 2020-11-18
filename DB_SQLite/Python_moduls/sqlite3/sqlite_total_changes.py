import sqlite3

try:
    db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
    cursor = db_connect.cursor()
    print("Connected to SQLite")

    sqlite_insert_query = """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          VALUES (4, 'Jos', 'jos@gmail.com', '2019-01-14', 9500);"""
    cursor.execute(sqlite_insert_query)

    sql_update_query = """Update SqliteDb_developers set salary = 10000 where id = 4"""
    cursor.execute(sql_update_query)

    sql_delete_query = """DELETE from SqliteDb_developers where id = 4"""
    cursor.execute(sql_delete_query)

    db_connect.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Error while working with SQLite", error)
finally:
    if (db_connect):
        # Identify total changes since the SQLite database connection was opened
        print("Total Rows affected since the database connection was opened: ", db_connect.total_changes)
        db_connect.close()
        print("sqlite connection is closed")