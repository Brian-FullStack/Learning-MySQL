import os
import pymysql

# Get username from workspace
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password = '',
                            db = 'Chinook')
try:
    # Run a query
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM Artist LIMIT 5;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, whether the above code was sucessful
    connection.close()