import psycopg2

def deleteInBulk(records):
    try:
        ps_connection = psycopg2.connect(user="postgres",
                                         password="vishal@#29",
                                         host="127.0.0.1",
                                         port="5432",
                                         database="postgres_db")
        cursor = ps_connection.cursor()
        ps_delete_query = """Delete from mobile where id = %s"""
        cursor.executemany(ps_delete_query, records)
        ps_connection.commit()

        row_count = cursor.rowcount
        print(row_count, "Record Deleted")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to DB_PostgreSQL", error)

    finally:
        # closing database connection.
        if (ps_connection):
            cursor.close()
            ps_connection.close()
            print("DB_PostgreSQL connection is closed")

# list of tuples contains database IDs
tuples = [(5, ), (4, ), (3, )]
deleteInBulk(tuples)