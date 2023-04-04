import pyodbc
import configparser

def read_config() -> configparser.ConfigParser:
    """
    Lee el archivo de configuración 'config.ini' y devuelve un objeto ConfigParser.

    Returns:
        configparser.ConfigParser: Objeto ConfigParser que contiene la configuración leída desde el archivo.
    """
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    return config

def connect_to_database() -> pyodbc.Connection:
    """
    Establece una conexión con la base de datos especificada en el archivo de configuración.

    Returns:
        pyodbc.Connection: Objeto Connection que representa la conexión establecida.
    """
    config = read_config()
    server = config['SQL server']['Server']
    database = config['SQL server']['Database']
    username = config['SQL server']['Userid']
    password = config['SQL server']['Password']

    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(connection_string)
    return conn

def insert_data(connection: pyodbc.Connection, data: tuple) -> None:
    """
    Inserta un registro en la tabla 'TestRecords' de la base de datos especificada.

    Args:
        connection (pyodbc.Connection): Objeto Connection que representa la conexión con la base de datos.
        data (tuple): Una tupla que contiene los valores a insertar en la tabla.
    """
    cursor = connection.cursor()
    insert_query = '''
        INSERT INTO [TestRecords] (StationName, SerialNumber, Date, TimeStamp, CycleTime, Status, PartNumber, FailDataType, FailName, Measurement, FailString)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_query, data)
    connection.commit()

def update_data(connection: pyodbc.Connection, data: tuple) -> None:
    """
    Actualiza un registro en la tabla 'TestRecords' de la base de datos especificada.

    Args:
        connection (pyodbc.Connection): Objeto Connection que representa la conexión con la base de datos.
        data (tuple): Una tupla que contiene los valores a actualizar en la tabla, así como la clave de registro (SerialNumber).
    """
    cursor = connection.cursor()
    update_query = '''
        UPDATE [TestRecords]
        SET StationName = ?, SerialNumber = ?, Date = ?, TimeStamp = ?, CycleTime = ?, Status = ?, PartNumber = ?, FailDataType = ?, FailName = ?, Measurement = ?, FailString = ?
        WHERE SerialNumber = ?
    '''
    cursor.execute(update_query, data)
    connection.commit()

def close_connection(connection: pyodbc.Connection) -> None:
    """
    Cierra la conexión con la base de datos especificada.

    Args:
        connection (pyodbc.Connection): Objeto Connection que representa la conexión a cerrar.
    """
    connection.close()
