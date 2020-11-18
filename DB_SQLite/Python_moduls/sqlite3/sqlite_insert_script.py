import sqlite3

try:
    db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
    cursor = db_connect.cursor()
    print("Successfully Connected to SQLite")

    with open(r'F:\Python\git\Gitlab\SQlite_pattern\SQLite_db\sql_commnds\mySQLiteScript.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()

    cursor.executescript(sql_script)    # method to execute all SQL statements in one call
    print("SQLite script executed successfully")
    cursor.close()

except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if (db_connect):
        db_connect.close()
        print("sqlite connection is closed")
