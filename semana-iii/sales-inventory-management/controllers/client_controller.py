from database.database import connect
from models.client import Client
class ClientController:
    def add_client(self: object, client: object = Client) -> None:
        conn = connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO clients (cpf, name_client, age_client, address_client, phone_client, email_client)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (client.cpf, client.name, client.age, client.address, client.phone, client.email))
            conn.commit()
            print("Cliente cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar o cliente: {e}")
        finally:
            cursor.close()
            conn.close()
    def find_for_cpf(self: object, cpf: str) -> object:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM clients WHERE cpf = ?""", (cpf,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if not row:
            return None
        return Client(*row)
    def list_clients(self: object) -> list:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Client(*row) for row in rows]