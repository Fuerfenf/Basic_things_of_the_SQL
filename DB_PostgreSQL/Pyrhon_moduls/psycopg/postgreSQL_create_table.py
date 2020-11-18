import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="msige72",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="test")

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE mobile
                            (ID INT PRIMARY KEY     NOT NULL,
                             MODEL     TEXT    NOT NULL,
                             PRICE         REAL); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in DB_PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating DB_PostgreSQL table", error)
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("DB_PostgreSQL connection is closed")