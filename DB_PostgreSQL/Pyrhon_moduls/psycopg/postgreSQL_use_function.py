import psycopg2


try:
    ps_connection = psycopg2.connect(user="postgres",
                                      password="msige72",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test")

    cursor = ps_connection.cursor()

    # call stored procedure  cursor.callproc('Function_or_procedure_name',[IN and OUT parameters,])
    # IN and OUT parameters must be separated by commas.
    cursor.callproc('get_production_Deployment', [72, ])

    print("fechting Employee details who pushed changes to the production from function")
    result = cursor.fetchall()
    for row in result:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Designation  = ", row[2])

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to DB_PostgreSQL", error)

finally:
    # closing database connection.
    if (ps_connection):
        cursor.close()
        ps_connection.close()
        print("DB_PostgreSQL connection is closed")