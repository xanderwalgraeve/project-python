
Mijn Project
Dit is een command line applicatie voor het beheren van producten.

Functionaliteiten
Toevoegen van producten aan de database
Zoeken naar producten
Genereren van rapporten in CSV of Excel
Installatie
Clone de repository: git clone https://github.com/xanderwalgraeve/project-python.git

Ga naar de projectmap: cd project-python

Voer de applicatie uit:

bash
Copy code
python scripts.py
Database
database.py
De module voor het beheren van de database. Hier wordt een SQLite-database gebruikt met een tabel voor producten.

Functies
__init__(self): Initialiseert de databaseverbinding en creëert de tabel indien nodig.
create_table(self): Creëert de tabel products als deze nog niet bestaat.
insert_product(self, name, price, description, stock): Voegt een nieuw product toe aan de database.
fetch_all_products(self): Haalt alle producten op uit de database.
close_connection(self): Sluit de databaseverbinding.
Voorbeeldgebruik
python
Copy code
from database import ProductDatabase

# Maak een instantie van de databaseklasse
product_db = ProductDatabase()

# Voeg nieuwe producten toe aan de database
product_db.insert_product('Boek', 25.00, 'Een boek over Python', 100)
product_db.insert_product('Computer', 1000.00, 'Een computer met Windows 11', 50)
product_db.insert_product('Telefoon', 500.00, 'Een telefoon met Android 13', 200)

# Haal alle producten op en druk ze af
products = product_db.fetch_all_products()
for product in products:
    print(product)

# Sluit de databaseverbinding
product_db.close_connection()
Bijdragen
Bijdragen zijn welkom! Open een probleem of stuur een pull-verzoek.

