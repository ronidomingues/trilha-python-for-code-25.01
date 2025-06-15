import os

from models.product import Product
from models.sale import Sale
from models.client import Client
from models.employee import Employee
from models.sale_item import SaleItem
from models.person import Person

from controllers.product_controller import ProductController
from controllers.sale_controller import SaleController
from controllers.employee_controller import EmployeeController
from controllers.client_controller import ClientController

from database.database import cretae_tables

cretae_tables()

products = ProductController()
sales = SaleController()
employees = EmployeeController()
clients = ClientController()

def menu():
    clear_screen()
    try:
        while True:
            print("\n==== Sistema de Gestão de Vendas ====")
            print("1. Cadastrar Produto")
            print("2. Cadastrar Cliente")
            print("3. Cadastrar Funcionário")
            print("4. Registrar Venda")
            print("5. Relatórios")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                register_product()
            elif opcao == '2':
                register_client()
            elif opcao == '3':
                register_employee()
            elif opcao == '4':
                register_sale()
            elif opcao == '5':
                show_reports()
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
    except KeyboardInterrupt:
        print("\nSaindo...")
def register_product():
    clear_screen()
    id_product = input("Digite o id do produto: ")
    name_product = input("Digite o nome do produto: ")
    price_product = float(input("Digite o preco do produto: "))
    amount_product = int(input("Digite a quantidade do produto: "))
    category_product = input("Digite a categoria do produto: ")
    try:
        product = Product(id_product, name_product, price_product, amount_product, category_product)
        products.add_product(product)
        print("Produto cadastrado com sucesso!")
    except ValueError as e:
        print(f"Erro ao cadastrar o produto: {e}")

def register_client():
    clear_screen()
    cpf = input("Digite o CPF do cliente: ")
    name = input("Digite o nome do cliente: ")
    age = int(input("Digite a idade do cliente: "))
    address = input("Digite o endereço do cliente: ")
    phone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")
    try:
        client = Client(cpf, name, age, address, phone, email)
        clients.add_client(client)
        print("Cliente cadastrado com sucesso!")
    except ValueError as e:
        print(f"Erro ao cadastrar o cliente: {e}")

def register_employee():
    clear_screen()
    cpf = input("Digite o CPF do funcionário: ")
    name = input("Digite o nome do funcionário: ")
    age = int(input("Digite a idade do funcionário: "))
    address = input("Digite o endereço do funcionário: ")
    phone = input("Digite o telefone do funcionário: ")
    salary = float(input("Digite o salario do funcionário: "))
    position = input("Digite a cargo do funcionário: ")
    email = input("Digite o email do funcionário: ")
    try:
        employee = Employee(cpf, name, age, address, phone, email, salary, position)
        employees.add_employee(employee)
        print("Funcionário cadastrado com sucesso!")
    except ValueError as e:
        print(f"Erro ao cadastrar o funcionário: {e}")

def register_sale():
    clear_screen()
    cpf_client = input("Digite o CPF do cliente: ")
    cpf_employee = input("Digite o CPF do funcionário: ")
    if cpf_client == cpf_employee:
        print("O funcionário não pode vender para si mesmo.")
        return
    client = clients.find_for_cpf(cpf_client)
    employee = employees.find_for_cpf(cpf_employee)
    if not client or not employee:
        print("Cliente ou funcionário não encontrado.")
        return
    sale = Sale(client, employee)
    while True:
        id_product = input("Digite o código do produto (ou fim para sair): ")
        if id_product.lower() == 'fim':
            break
        product = products.find_for_id(id_product)
        if not product:
            print("Produto nao encontrado.")
            continue
        amount_product = int(input("Digite a quantidade do produto: "))
        try:
            item = SaleItem(product, amount_product)
            sale.add_item(item)
        except ValueError as e:
            print(f"Erro ao adicionar o item: {e}")
    sales.register_sale(sale)
    print(f"Venda registrada com sucesso! Total: R${sale.total_value:.2f}")
def show_reports():
    clear_screen()
    print("=== Relatórios ===")
    print("1. Total de Vendas")
    print("2. Produtos com Estoque Baixo")
    print("3. Histórico de Compras por Cliente")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        total = sales.total_sales()
        print(f"Total de Vendas: R${total:.2f}")
    elif opcao == '2':
        limit = int(input("Informe o limite de estoque: "))
        in_low = products.low_stock_products(limit)
        print("Produtos com estoque baixo:")
        for product in in_low:
            print(f"ID: {product.id_product}, Nome: {product.name_product}, Estoque: {product.amount_product}")
    elif opcao == '3':
        cpf = input("CPF do cliente: ")
        historic = sales.history_by_client(cpf)
        if not historic:
            print("Nenhuma compra encontrada para esse cliente.")
        else:
            print(f"Histórico de compras do CPF {cpf}:")
            for sale in historic:
                print(f"ID: {sale.id}, Cliente: {sale.client.name}, Total: R${sale.total_value:.2f}")
    else:
        print("Opção inválida.")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    clear_screen()
    menu()
