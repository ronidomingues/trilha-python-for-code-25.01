class Person:
    def __init__(self: object, cpf: str, name: str, age: int, address: str, phone: str) -> None:
        self.cpf: str = cpf
        self.name: str = name
        self.age: int = age
        self.address: str = address
        self.phone: str = phone