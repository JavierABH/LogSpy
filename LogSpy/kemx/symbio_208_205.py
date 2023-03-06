import pandas as pd
import clr
from datetime import datetime
import configparser
import csv
from typing import List, Tuple

settings = configparser.ConfigParser()
settings.read('settings\config.ini')
# Paths to external DLL files
newtonsoftjson_path = settings["WSConnector"]["Newtonsoft.Json.Dll"]
wsconnector_path = settings["WSConnector"]["WSConnector.Dll"]\
# Adding references to the external DLL files
clr.AddReference(newtonsoftjson_path)
clr.AddReference(wsconnector_path)
# Importing the Connector class from the WSConnector module
from WSConnector import Connector
# Instance of the Connector class
connector = Connector()

class CsvModifier():
    def __init__(self, path):
        self.path = path
    
    def read_csv(self) -> List[List[str]]:
        """
        Reads a CSV file and returns a list of rows.
        """ 
        try:
            with open(self.path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                rows = [row for row in reader]
                return rows
        except Exception as e:
            raise Exception("Error reading csv file: " + str(e))

    def process_csv(self, rows: List[List[str]]) -> List[List[str]]:
        """
        Processes a list of rows and returns a modified list of rows.
        """
        try:
            csv_header1 = rows[0][6:]
            for i, row in enumerate(rows):
                if i in [3, 4] and "SN" in row:
                    row += csv_header1
                    break
            return rows
        except Exception as e:
            raise Exception("Error processing csv file: " + str(e))
        
    def write_csv(self, rows: List[List[str]]) -> str:
        """
        Writes a list of rows to a CSV file and returns a success message.
        """
        try:
            with open(self.path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(rows)
            return f"Successfully modified CSV: {self.path}"
        except FileNotFoundError:
            return f"CSV file not found: {self.path}"
        except Exception as e:
            return f"CSV modification failed: {e}"

    def modify_csv(self) -> str:
        """
        Modifies a CSV file and returns a success message.
        """
        try:
            rows = self.read_csv()
            modified_rows = self.process_csv(rows)
            self.write_csv(modified_rows)
            return "Successfully modified csv file: " + self.path
        except Exception as e:
            raise Exception("Error modifying csv file: " + str(e))

        
    