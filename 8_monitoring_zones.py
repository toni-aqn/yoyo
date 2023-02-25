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
    zonebud (fk_zone_id, fk_bud_id)
VALUES
    (%s,%s);
"""

# VI SKAL LAVE EN VISNING OVER ZONERNE OG BUDDENE

print("--- Sæt et eksisterende bud på en zone ---")
zone_id = int(input("Tast nummeret på zonen: #"))
leveringsbud_id = int(input("Tast id'et leveringsbuddet: #"))

# Der skal være et userinput, hvor der i baggrunden er en SQL query der vælger SET WHERE ID = userinputtet.
# I den oprindelige oprettelse af tabels eksistere der 4 records i zonebud - der skal være mulighed for et leveringsbud
# at sætte sig på en af de records, vha. en UPDATE SET måske(?)


data = (zone_id, leveringsbud_id)

try:
   # Executing the SQL command
   cursor.execute(insert_ny_zone_values, data)
   
   # Commit your changes in the database
   connection.commit()
   print("Succes")

except:
   # Rolling back in case of error
#    conn.rollback()
    print(f"Failed, der eksistere ikke en zone #{zone_id} eller et bud #{leveringsbud_id}")

connection.close()