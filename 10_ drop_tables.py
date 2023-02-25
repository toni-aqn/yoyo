import mysql.connector
from mysql.connector import Error

# Opret forbindelse til databasen
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")

    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

# Kald funktionen
connection = create_connection("localhost", "root", "1234","gruppe14_yoyoDB")


# Funktion til at lave queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Table dropped succesfully")
    except Error as e:
        print(f"The error '{e}' occurred")


drop_zonebud = """
DROP TABLE zonebud;
"""

drop_leveringsbud = """
DROP TABLE leveringsbud;
"""

drop_zone = """
DROP TABLE zone;
"""

drop_restaurant = """
DROP TABLE restaurant;
"""

drop_kunde = """
DROP TABLE kunde;
"""

execute_query(connection, drop_zonebud)
execute_query(connection, drop_leveringsbud)
execute_query(connection, drop_restaurant)
execute_query(connection, drop_kunde)
execute_query(connection, drop_zone)

connection.close()