from datetime import datetime

class Sale:
    _count_id = 1

    def __init__(self: object, client: object, employee: object) -> None:
        self.id: int = Sale._count_id
        Sale._count_id += 1
        self.client: object = client
        self.employee: object = employee
        self.items: list = []
        self.data: datetime = datetime.now()
        self.total_value: float = 0.0
    def add_item(self: object, item_sale: object) -> None:
        if item_sale.quantity > item_sale.product.amount_product:
            raise ValueError("Quantidade vendida maior que a quantidade em estoque")
        self.items.append(item_sale)
        self.total_value += item_sale.subtotal