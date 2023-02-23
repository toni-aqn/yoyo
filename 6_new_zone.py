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
connection = create_connection("localhost", "root", "1234","yoyoDB")
cursor = connection.cursor()

# Funktion til at lave queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")



insert_ny_zone_values = """
INSERT INTO
    zone (zNavn, postnummer)
VALUES
    (%s,%s);
"""

print("---Opret en ny zone---")
zone_navn = input("Indtast navnet på zonen: ").title()
zone_postnummer = int(input("Indtast postnummer: "))

data = (zone_navn, zone_postnummer)

try:
   # Executing the SQL command
   cursor.execute(insert_ny_zone_values, data)
   
   # Commit your changes in the database
   connection.commit()
   print("Succes")

except:
   # Rolling back in case of error
#    conn.rollback()
    print("Failed")

connection.close()