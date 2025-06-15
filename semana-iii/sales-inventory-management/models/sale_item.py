class SaleItem:
    def __init__(self: object, product: object, quantity: int) -> None:
        self.product: object = product
        self.quantity: int = quantity
        self.unit_price: float = product.price_product
        self.subtotal: float = self.unit_price * self.quantity