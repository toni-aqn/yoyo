import mysql.connector
from mysql.connector import Error

print('Andreas Kahle / Toni Nguyen / Zacharias Nicolaisen')

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

bruger = input("\nTast dit brugernavn til din server: ")
kode = input("Tast dit kodeord til din server: ")

# Kald funktionen
connection = create_connection("localhost", bruger, kode, "gruppe14_yoyoDB")
cursor = connection.cursor()

# Funktion til at lave single queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


menu = [
    '\n*---MENU----*',
    '[1]   -   [Show Tables]',
    '[2]   -   [Opret nyt leveringsbud]',
    '[3]   -   [Opret ny zone]',
    '[4]   -   [Tilknyt et leveringsbud til en zone]',
    '[Q]   -   [For at afslutte programmet]',
    '-------------'
]

def show_menu():
    for x in menu:
        print(x)




loop_active = True
while (loop_active):

    show_menu()
    option = input("> ").lower()
    
    if option == '1':
        cursor.execute("Show tables;")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

    elif option == '2':
        
        insert_ny_leveringsbud_values = """
        INSERT INTO
            leveringsbud (bFornavn, bEfternavn)
        VALUES
            (%s,%s);
        """
        print("\n---Opret dig som leveringsbud---\n")
        
        bud_fornavn = input("Tast dit fornavn: ").title()
        bud_efternavn = input("Tast dit efternavn: ").title()
        
        data = (bud_fornavn, bud_efternavn)
        cursor.execute(insert_ny_leveringsbud_values, data)
        
        connection.commit()
        
        sql_select_Query = "select * from Leveringsbud"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("Id = ", row[0], )
            print("Fornavn = ", row[1])
            print("Efternavn  = ", row[2],"\n")
        
        
    elif option == '3':
        insert_ny_zone_values = """
        INSERT INTO
            zone (zNavn, postnummer)
        VALUES
            (%s,%s);
        """

        print("\n---Opret en ny zone---\n")
        zone_navn = input("Indtast navnet på zonen: ").title()
        zone_postnummer = int(input("Indtast postnummer: "))
        data = (zone_navn, zone_postnummer)
        cursor.execute(insert_ny_zone_values, data)
        connection.commit()
        print("Du har oprettet en ny zone")
        
        sql_select_Query = "select * from Zone"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("Id = ", row[0], )
            print("Navn = ", row[1])
            print("Postnummer  = ", row[2],"\n")

    
    elif option == '4':
        
        insert_ny_zone_values = """
        INSERT INTO
            zonebud (fk_zone_id, fk_bud_id)
        VALUES
            (%s,%s);
        """
        print("--- Sæt et eksisterende bud på en zone ---")
        zone_id = int(input("Tast id'et på zonen: "))
        leveringsbud_id = int(input("Tast id'et leveringsbuddet: "))

        data = (zone_id, leveringsbud_id)
        cursor.execute(insert_ny_zone_values, data)
        connection.commit()
        print(f"Du har tilføjet bud #{leveringsbud_id} til zone #{zone_id}")
        
        sql_select_Query = "select * from zonebud"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("Id = ", row[0], )
            print("zone_id = ", row[1])
            print("leveringsbud_id  = ", row[2],"\n")
        
    elif option == 'q':
        print("\n[PROGRAM AFSLUTTET]\n")
        loop_active = False
        print('Gruppe 14 - OrderYOYO')
        print('Andreas Kahle / Toni Nguyen / Zacharias Nicolaisen\n')
        
    else:
        print(f"\n'{option}' er ikke en valgmulighed, prøv igen!")




