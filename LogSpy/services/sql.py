import pyodbc
import configparser

settings = configparser.ConfigParser()
settings.read('settings\config.ini')
driver = settings["SQL server"]["Driver"]
server = settings["SQL server"]["Server"]
database = settings["SQL server"]["Database"]
userid = settings["SQL server"]["Userid"]
password = settings["SQL server"]["Password"]

def insert_data(table_name, column_names, data):
    print("connecting...")
    connection = pyodbc.connect(
        (f"Driver={driver};"
        f"Server={server};"
        f"Database={database};"
        f"UID={userid};"
        f"PWD={password};")
    )
    print("connected")

    # Create a cursor
    cursor = connection.cursor()
    print("cursor connected")

    # Create the SQL query dynamically
    query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join('?' * len(column_names))})"

    # Execute the SQL query for each row of data
    for row in data:
        cursor.execute(query, row)

    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()