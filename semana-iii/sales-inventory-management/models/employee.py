from models.person import Person

class Employee(Person):
    def __init__(self: object, cpf: str, name: str, age: int, address: str, phone: str, email: str, salary: float, position: str) -> None:
        super().__init__(cpf, name, age, address, phone)
        self.salary: float = salary
        self.position: str = position
        self.email: str = email
        self.sales_made: list = []

    def add_sale(self: object, sale: float) -> None:
        self.sales_made.append(sale)