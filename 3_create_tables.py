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

connection = create_connection("localhost", "root", "1234","yoyoDB")

#------------------------------------------------------#


# Funktion til at lave queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        

create_zone_table = """
CREATE TABLE IF NOT EXISTS zone(
    id INT PRIMARY KEY AUTO_INCREMENT,
    zNavn VARCHAR(255) UNIQUE NOT NULL,
    postnummer INT NOT NULL
);
"""

create_leveringsbud_table = """
CREATE TABLE IF NOT EXISTS leveringsbud(
    id INT PRIMARY KEY AUTO_INCREMENT,
    bFornavn VARCHAR(255) NOT NULL,
    bEfternavn VARCHAR(255) NOT NULL
);
"""

create_zonebud_table = """
CREATE TABLE IF NOT EXISTS zonebud(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    fk_zone_id INT NOT NULL,
    fk_bud_id INT UNIQUE,
    FOREIGN KEY (fk_zone_id) REFERENCES zone(id),
    FOREIGN KEY (fk_bud_id) REFERENCES leveringsbud(id)
);
"""


execute_query(connection, create_zone_table)
execute_query(connection, create_leveringsbud_table) 
execute_query(connection, create_zonebud_table) 
