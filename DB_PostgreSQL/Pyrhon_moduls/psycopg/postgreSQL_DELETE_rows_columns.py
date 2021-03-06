import psycopg2

def deleteData(mobileId):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="msige72",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test")

        cursor = connection.cursor()

        # Update single record now
        sql_delete_query = """Delete from mobile where id = %s"""
        cursor.execute(sql_delete_query, (mobileId, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("DB_PostgreSQL connection is closed")

deleteData(4)
deleteData(5)