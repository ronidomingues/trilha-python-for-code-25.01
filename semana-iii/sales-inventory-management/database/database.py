import sqlite3
import os

# Caminho absoluto para onde o script está localizado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho completo para o arquivo do banco dentro da pasta database
DB_PATH = os.path.join(BASE_DIR, "sales_system.db")

def connect():
    return sqlite3.connect(DB_PATH)
def cretae_tables():
    conn = connect()
    cursor = conn.cursor()

    # Products table:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id_product TEXT PRIMARY KEY NOT NULL,
            name_product TEXT NOT NULL,
            price_product REAL NOT NULL,
            amount_product INTEGER NOT NULL,
            category_product TEXT NOT NULL
        )
    """)
    # Clients table:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            cpf TEXT PRIMARY KEY NOT NULL,
            name_client TEXT NOT NULL,
            age_client INTEGER NOT NULL,
            address_client TEXT NOT NULL,
            phone_client TEXT NOT NULL,
            email_client TEXT NOT NULL
        )
    """)
    # Employees table:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            cpf TEXT PRIMARY KEY NOT NULL,
            name_employee TEXT NOT NULL,
            age_employee INTEGER NOT NULL,
            address_employee TEXT NOT NULL,
            phone_employee TEXT NOT NULL,
            email_employee TEXT NOT NULL,
            position_employee TEXT NOT NULL,
            salary_employee REAL NOT NULL
        )
    """)
    # Sales table:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id_sale INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf_client TEXT NOT NULL,
            cpf_employee TEXT NOT NULL,
            date_sale TEXT NOT NULL,
            total_sale REAL NOT NULL,
            FOREIGN KEY (cpf_client) REFERENCES clients (cpf),
            FOREIGN KEY (cpf_employee) REFERENCES employees (cpf)
        )
    """)
    # SaleItems table:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sale_items (
            id_sale_item INTEGER PRIMARY KEY AUTOINCREMENT,
            id_sale TEXT NOT NULL,
            id_product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (id_sale) REFERENCES sales (id_sale),
            FOREIGN KEY (id_product) REFERENCES products (id_product)
        )
    """)
    conn.commit()
    conn.close()