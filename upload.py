import csv
import pyodbc

# Parámetros de conexión a la base de datos
server_name = '095DESIGN3D,1433'
database_name = 'FCT DATA'
username = 'sa'
password = 'T3stPa$$word'

# Nombre de la tabla
table_name = 'TestRecord1'

# Ruta del archivo CSV
csv_path = r'C:\Users\k90011729\OneDrive - Kimball Electronics\Desktop\Proyecto Estaciones\results.csv'

# Leer el archivo CSV y almacenar los datos en una lista de tuplas
with open(csv_path, newline='') as f:
    reader = csv.reader(f)
    next(reader)  # Saltar la primera fila (encabezados de columna)
    rows = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]) for row in reader]

# Conectar a la base de datos y crear la tabla
conn_str = f"DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};UID={username};PWD={password}"
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute(f"""
    CREATE TABLE {table_name} (
        station VARCHAR(50),
        serial VARCHAR(50),
        date DATE,
        date_time DATETIME,
        cycle_time FLOAT,
        status BIT,
        partnumber VARCHAR(50),
        failure VARCHAR(50),
        measurement VARCHAR(50)
    )
""")

# Cargar los datos en la tabla
cursor.executemany(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)
conn.commit()

# Cerrar la conexión
conn.close()
