

import sqlite3

class ProductDatabase:
    def __init__(self):
        self.dbname = "C:/Users/Gebruiker/Documents/Python/boeken/product_database.db"
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                description TEXT,
                stock INTEGER
            )
        """)
        self.conn.commit()

    def insert_product(self, name, price, description, stock):
        self.cursor.execute("INSERT INTO products (name, price, description, stock) VALUES (?, ?, ?, ?)",
                            (name, price, description, stock))
        self.conn.commit()

    def fetch_all_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
