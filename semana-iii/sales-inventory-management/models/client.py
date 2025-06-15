from models.person import Person

class Client(Person):
    def __init__(self: object, cpf: str, name: str, age: int, address: str, phone: str, email: str) -> None:
        super().__init__(cpf, name, age, address, phone)
        self.email: str = email