import requests
import datetime
import pyodbc
import time
from Scripts.Scraping import ScrappingCrypto
#Obtain data.
def obtener_datos_cripto(nombre_cripto):
    url = f'https://api.coingecko.com/api/v3/coins/{nombre_cripto}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        market_cap = round(data['market_data']['market_cap']['usd'], 2)  
        volume = round(data['market_data']['total_volume']['usd'], 2)  
        circulating_supply = round(data['market_data']['circulating_supply'], 2)  
        total_supply = round(data['market_data']['total_supply'], 2)  
        price = round(data['market_data']['current_price']['usd'], 2)  
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        return {
            'Price': price,
            'MarketCap': market_cap,
            'Volume': volume,
            'CirculatingSupply': circulating_supply,
            'TotalSupply': total_supply,
            'TimeStamp': timestamp
        }
    else:
        print(f'Error al obtener datos: {response.status_code}')
        return None


#Inset into the SQL server
def insertar_en_sql_server(datos, cursor,reset):
    if(reset):
        cursor.execute('DELETE FROM dbo.BTC')

    query = f"INSERT INTO dbo.BTC (Price, MarketCap, Volume, CirculatingSupply, TotalSupply, TimeStamp) VALUES ({datos['Price']}, {datos['MarketCap']}, {datos['Volume']}, {datos['CirculatingSupply']}, {datos['TotalSupply']}, GETDATE())"
    cursor.execute(query)
    cursor.commit()

####MAIN#######

#Configure the conexion
    
DRIVER_NAME='SQL Server'
SERVER_NAME='DESKTOP-661VEOS'
DATABASE_NAME='Crypto'
scrap=ScrappingCrypto(SERVER_NAME,DATABASE_NAME,DRIVER_NAME)

#Secondary configuration
nombre_cripto = 'bitcoin'  # Reemplaza con el nombre de la criptomoneda que deseas seguir

reset_table = False
minutos_refresh=5

#Establish any condition to stop. (Default --> No stop)
while True:
    datos_cripto = obtener_datos_cripto(nombre_cripto)

    if datos_cripto is not None:
        # Insert values into dataset_server
        if reset_table:
            insertar_en_sql_server(datos_cripto, scrap.cursor,reset_table)
            reset_table =False
        else:
            insertar_en_sql_server(datos_cripto, scrap.cursor,reset_table)

        

        # Print values
        for clave, valor in datos_cripto.items():
            print(f'{clave}: {valor}')

    # wait time
    time.sleep(60*minutos_refresh)  # Modify time 60*min (time.sleep(60)-->60 seconds)
scrap.conexion.close()