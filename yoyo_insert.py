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
connection = create_connection("localhost", "root", "1234","yoyoDB")


# Funktion til at lave queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Insert query // Zone
insert_zone_values = """
INSERT INTO
    zone (zNavn, postnummer)
VALUES
    ('Valby', 2500),
    ('Frederiksberg', 2000),
    ('Nørrebro', 2200),
    ('Nordvest', 2400);
"""

insert_leveringsbud_values = """
INSERT INTO
    leveringsbud (bNavn)
VALUES
    ('Toni'),
    ('Daniela'),
    ('Mikkel'),
    ('Oliver');
"""

insert_zonebud_values = """
INSERT INTO
    zonebud (fk_zone_id, fk_bud_id)
VALUES
    ('1', null),
    ('1', null),
    ('1', null),
    ('1', null);
"""

# drop_table = """
# TRUNCATE zonebud;
# """

# execute_query(connection, insert_zone_values)
# execute_query(connection, insert_leveringsbud_values)
# execute_query(connection, insert_zonebud_values)
# execute_query(connection, drop_table)