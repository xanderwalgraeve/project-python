
# user_interface.py

import csv
from openpyxl import Workbook
from database import ProductDatabase

def display_menu():
    print("1. Voeg een nieuw product toe")
    print("2. Zoek producten")
    print("3. Wijzig productgegevens")
    print("4. Genereer een rapport")
    print("5. Genereer een CSV-rapport")
    print("6. Genereer een Excel-rapport")
    print("7. Sluit de applicatie")

def get_user_choice():
    choice = input("Voer het nummer van de gewenste optie in: ")
    return choice

def add_product():
    name = input("Voer de naam van het product in: ")
    price = float(input("Voer de prijs van het product in: "))
    description = input("Voer de beschrijving van het product in: ")
    stock = int(input("Voer de voorraad van het product in: "))
    
    product_db = ProductDatabase()
    product_db.insert_product(name, price, description, stock)
    print(f"{name} is toegevoegd aan de database.")

def search_products():
    product_db = ProductDatabase()
    products = product_db.fetch_all_products()

    if not products:
        print("Geen producten gevonden.")
    else:
        print("Alle producten:")
        for product in products:
            print(product)

def modify_product():
    # Implementeer logica om productgegevens te wijzigen
    pass

def generate_report():
    # Implementeer logica om een rapport te genereren
    pass

def generate_csv_report():
    product_db = ProductDatabase()
    products = product_db.fetch_all_products()

    if not products:
        print("Geen producten gevonden voor het rapport.")
        return

    header = ["ID", "Naam", "Prijs", "Beschrijving", "Voorraad"]
    rows = [(product[0], product[1], product[2], product[3], product[4]) for product in products]

    with open("product_report.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    print("CSV-rapport is gegenereerd: product_report.csv")

def generate_excel_report():
    product_db = ProductDatabase()
    products = product_db.fetch_all_products()

    if not products:
        print("Geen producten gevonden voor het rapport.")
        return

    wb = Workbook()
    ws = wb.active

    header = ["ID", "Naam", "Prijs", "Beschrijving", "Voorraad"]
    ws.append(header)

    for product in products:
        ws.append(product)

    wb.save("product_report.xlsx")
    print("Excel-rapport is gegenereerd: product_report.xlsx")

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            add_product()
        elif choice == '2':
            search_products()
        elif choice == '3':
            modify_product()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            generate_csv_report()
        elif choice == '6':
            generate_excel_report()
        elif choice == '7':
            print("Bedankt voor het gebruik van de applicatie. Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == "__main__":
    main()
