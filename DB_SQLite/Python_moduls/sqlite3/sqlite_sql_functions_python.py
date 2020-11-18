"""
This function accepts three arguments.
name is the function name.
num_params is the number of parameters the function accepts.
func is a Python callable that is called as the SQL function within a query.
This function creates a new user-defined function that we can use from within SQL
statements under the function name.
Note: if num_params is -1, the function may take any number of arguments.
connection.create_function() can return any of the types supported by SQLite for
example, bytes, str, int, float and None.

Next, we called create_fundction of a connection class and passed three
arguments function name, the number of parameters the _toTitleCase accepts and
Python callable that is called as the SQL function within a query.
Next, we called TOTILECASE function in SQLite SELECT query to get the developer name in title case.
"""
import sqlite3


def _toTileCase(string):
    return str(string).title()


def getDeveloperName(id):
    try:
        db_connect = sqlite3.connect('C:\sqlite\database\Egor_test.db')
        cursor = db_connect.cursor()
        print("Connected to SQLite")

        db_connect.create_function("TOTILECASE", 1, _toTileCase)
        select_query = "SELECT TOTILECASE(name) FROM SqliteDb_developers where id = ?"
        cursor.execute(select_query, (id,))
        name = cursor.fetchone()
        print("Developer Name is", name)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (db_connect):
            db_connect.close()
            print("sqlite connection is closed")


getDeveloperName(1)
