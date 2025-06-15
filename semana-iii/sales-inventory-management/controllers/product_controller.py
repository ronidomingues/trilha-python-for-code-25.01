from database.database import connect
from models.product import Product

class ProductController:
    def add_product(self: object, product: object) -> None:
        conn = connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO products (id_product, name_product, price_product, amount_product, category_product)
                VALUES (?, ?, ?, ?, ?)
            """, (product.id_product, product.name_product, product.price_product, product.amount_product, product.category_product))
            conn.commit()
            print("Produto cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar o produto: {e}")
        finally:
            cursor.close()
            conn.close()
    def find_for_id(self: object, id_product: str) -> object:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM products WHERE id_product = ?""", (id_product,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if not row:
            return None
        return Product(*row)
    def list_products(self: object) -> list:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Product(*row) for row in rows]
    def low_stock_products(self: object, limit: int = 5) -> list:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE amount_product <= ?", (limit,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Product(*row) for row in rows]