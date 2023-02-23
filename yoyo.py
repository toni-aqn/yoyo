import mysql.connector
from mysql.connector import Error

# Opret forbindelse til databasen
def create_connection(host_name, user_name, user_password,db_name):
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
connection = create_connection("localhost", "root", "timeleft","yoyoDB")


# Funktion til at lave queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Insert query
create_zone = """
INSERT INTO
  zone (zNavn, postnummer, aktiv)
VALUES
  ('Valby', 2500),
  ('Frederiksberg', 2000),
  ('Noerrebro', 2200),
  ('Nordvest', 2400, 0);
"""

execute_query(connection, create_zone)