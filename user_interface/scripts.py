
from database import ProductDatabase

def main():
   
    product_db = ProductDatabase()

    # Insert sample data
    product_db.insert_product('Boek', 25.00, 'Een boek over Python', 100)
    product_db.insert_product('Computer', 1000.00, 'Een computer met Windows 11', 50)
    product_db.insert_product('Telefoon', 500.00, 'Een telefoon met Android 13', 200)

   
    products = product_db.fetch_all_products()
    for product in products:
        print(product)

    
    product_db.close_connection()

if __name__ == "__main__":
    main()
# scripts.py

from user_interface import main as user_interface_main

if __name__ == "__main__":
    user_interface_main()
