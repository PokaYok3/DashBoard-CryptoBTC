'''
Script para capturar los datos de diferentes cryptos.

'''

#Imports

import pyodbc
from datetime import datetime

class ScrappingCrypto(object):

    #Configuration of the server
    def __init__(self,servername,database,driver):

        self.server_name=servername
        self.database=database
        self.driver=driver
        self.con_string=f"""
        DRIVER={self.driver};
        SERVER={self.server_name};
        DATABASE={self.database};
        UID=sa;
        PWD=1234;
        Trust_Connection=yes;

        """   
        self.conexion = pyodbc.connect(self.con_string)
        self.cursor = self.conexion.cursor()

    def insertar_en_sql_server(self,datos, cursor,reset):
        if(reset):
            cursor.execute('DELETE FROM dbo.BTC')

        query = f"INSERT INTO dbo.BTC (Price, MarketCap, Volume, CirculatingSupply, TotalSupply, TimeStamp) VALUES ({datos['Price']}, {datos['MarketCap']}, {datos['Volume']}, {datos['CirculatingSupply']}, {datos['TotalSupply']}, GETDATE())"
        cursor.execute(query)
        cursor.commit()
