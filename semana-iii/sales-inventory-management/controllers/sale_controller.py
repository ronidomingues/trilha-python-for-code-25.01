from database.database import connect

from models.sale import Sale
from models.sale_item import SaleItem
from models.product import Product
from models.client import Client
from models.employee import Employee

class SaleController:
    def register_sale(self: object, sale: object = Sale) -> None:
        conn = connect()
        cursor = conn.cursor()
        try:
            # Inserindo a venda
            cursor.execute("""
                INSERT INTO sales (cpf_client, cpf_employee, date_sale, total_sale)
                VALUES (?, ?, ?, ?)
            """, (sale.client.cpf, sale.employee.cpf, sale.data, sale.total_value))
            sale.id = cursor.lastrowid
            # Inserindo os itens da venda
            for item in sale.items:
                cursor.execute("""
                    INSERT INTO sale_items (id_sale, id_product, quantity)
                    VALUES (?, ?, ?)
                """, (sale.id, item.product.id_product, item.quantity))
                # Atualizar o estoque do produto
                cursor.execute("""
                    UPDATE products
                    SET amount_product = amount_product - ?
                    WHERE id_product = ?
                """, (item.quantity, item.product.id_product))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Erro ao registrar venda: {e}")
        finally:
            cursor.close()
            conn.close()
    def total_sales(self: object) -> float:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(total_sale) FROM sales")
        rows = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return rows if rows else 0.0
    def history_by_client(self: object, cpf: str) -> list:
        conn = connect()
        cursor = conn.cursor()
        # Buscar vendas pelo CPF do cliente
        cursor.execute("SELECT * FROM sales WHERE cpf_client = ?", (cpf,))
        sales_rows = cursor.fetchall()
        sales_result = []
        for id_sale, cpf_client, cpf_employee, date_sale, total_sale in sales_rows:
            # Busca os itens da venda
            cursor.execute("SELECT id_product, quantity FROM sale_items WHERE id_sale = ?", (id_sale,))
            items_rows = cursor.fetchall()
            items = []
            for id_product, quantity in items_rows:
                cursor.execute("SELECT * FROM products WHERE id_product = ?", (id_product,))
                row = cursor.fetchone()
                if row:
                    product = Product(*row)
                    items.append(SaleItem(product, quantity))
            # Criar objetos fake do cliente e funcionário só para estrutura
            name_fake_client = cursor.execute("SELECT name_client FROM clients WHERE cpf = ?", (cpf_client,)).fetchone()[0]
            cliente_fake = Client(cpf_client, name_fake_client, 0, "N/A", "N/A", "N/A")
            funcionario_fake = Employee(cpf_employee, "N/A", 0, "N/A", "N/A", "N/A", 0.0, "N/A")
            sale = Sale(cliente_fake, funcionario_fake)
            sale.id = id_sale
            sale.data = date_sale
            sale.total_value = total_sale
            sale.items = items

            sales_result.append(sale)

        cursor.close()
        conn.close()
        return sales_result