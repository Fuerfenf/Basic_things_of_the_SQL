import psycopg2
try:
    connection = psycopg2.connect(user="postgres",
                                  password="msige72",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="test")

    cursor = connection.cursor()
    # Print DB_PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print DB_PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error:
    print ("Error while connecting to DB_PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("DB_PostgreSQL connection is closed")