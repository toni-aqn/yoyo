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


bruger = input("Tast dit brugernavn (root): ")
kode = input("Tast dit kodeord: ")
db_navn = input("Skriv navnet på databasen du vil connecte til (yoyoDB): ")

# Kald funktionen
connection = create_connection("localhost", bruger, kode, db_navn)
