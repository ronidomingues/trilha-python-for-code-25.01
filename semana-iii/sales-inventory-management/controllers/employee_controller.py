from database.database import connect
from models.employee import Employee

class EmployeeController:
    def add_employee(self: object, employee: object = Employee) -> None:
        conn = connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO employees (cpf, name_employee, age_employee, address_employee, phone_employee, email_employee, salary_employee, position_employee)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (employee.cpf, employee.name, employee.age, employee.address, employee.phone, employee.email, employee.salary, employee.position))
            conn.commit()
            print("Funcionário cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar o funcionário: {e}")
        finally:
            cursor.close()
            conn.close()
    def find_for_cpf(self: object, cpf: str) -> object:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM employees WHERE cpf = ?""", (cpf,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if not row:
            return None
        return Employee(*row)
    def list_employees(self: object) -> dict:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Employee(*row) for row in rows]