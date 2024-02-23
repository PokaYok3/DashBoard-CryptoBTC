import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS BTC (
                Price FLOAT NOT NULL,
                MarketCap FLOAT,
                Volume FLOAT,
                CirculatingSupply FLOAT,
                TotalSupply FLOAT,
                Timestamp DATETIME
            )
        ''')
        self.conn.commit()
        

    
    def insert_btc_data(self, price, market_cap, volume, circulating_supply, total_supply, timestamp):
        try:
            self.cursor.execute('''
                INSERT INTO BTC (Price, MarketCap, Volume, CirculatingSupply, TotalSupply, Timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (price, market_cap, volume, circulating_supply, total_supply, timestamp))
            self.conn.commit()
            print(f"Datos de BTC insertados correctamente a las {timestamp}")
        except sqlite3.Error as e:
            print(f"Error al insertar datos de BTC: {e}")


    def insert_user(self, username, password):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def verify_credentials(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()
        return user

    def close_connection(self):
        self.conn.close()
