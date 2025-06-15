class Product:
    def __init__(self: object, id_product: str, name_product: str, price_product: float, amount_product: int, category_product: str) -> None:
        self.id_product: str = id_product
        self.name_product: str = name_product
        self.price_product: float = price_product
        self.amount_product: int = amount_product
        self.category_product: str = category_product
    def __update_stock(self, quantity_sold: int) -> None:
        if quantity_sold > self.amount_product:
            raise ValueError("Quantidade vendida maior que a quantidade em estoque")
        self.amount_product -= quantity_sold
        return
