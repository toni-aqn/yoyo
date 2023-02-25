import mysql.connector
from mysql.connector import Error


# Funktion til at oprette forbindelse til MySQL server
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")

    except Error as e:
        print(f"The error '{e}' occurred")
        
    return connection


# Vi kalder create_connection (funktionen vi har lavet ovenover) med parametre som brugeren indtaste til sin egen MySQL server
print("\nVed at køre dette script kan du oprette en ny database ved navn 'gruppe14_yoyoDB' ved blot at logge ind på din MySQL server\n")
bruger = input("Tast dit brugernavn til din server: ")
kode = input("Tast dit kodeord til din server: ")

connection = create_connection("localhost", bruger, kode)

# Funktion til at oprette en database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database 'gruppe14_yoyoDB' created succesfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Query til at oprette en database ved navn 'gruppe14_yoyoDB'
create_database_query = "CREATE DATABASE gruppe14_yoyoDB"

# Funktion create_database kaldes
create_database(connection, create_database_query)

connection.close()