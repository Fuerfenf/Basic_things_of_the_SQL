import psycopg2

def bulkInsert(records):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="msige72",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test")
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO mobile (id, model, price) 
                           VALUES (%s,%s,%s) """

        # executemany() to insert multiple rows rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into mobile table {}".format(error))

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("DB_PostgreSQL connection is closed")

records_to_insert = [ (7,'LG G2', 200) , (8,'One Plus 7', 1250)]
bulkInsert(records_to_insert)