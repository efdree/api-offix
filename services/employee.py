from models.model import Employee as EmployeeModel
from schemas.employee import Employee

class EmployeeService():

    def __init__(self, db) -> None:
        self.db = db

    def get_employees(self):
        result = self.db.query(EmployeeModel).all()
        return result

    def get_employee(self, id):
        result = self.db.query(EmployeeModel).filter(
            EmployeeModel.id == id).first()
        return result

    def search_employee(self, name: str):
        result = self.db.query(EmployeeModel).filter(EmployeeModel.name == name).all()
        return result

    def get_employee_by_department(self, department_id):
        result = self.db.query(EmployeeModel).filter(
            EmployeeModel.department_id == department_id).all()
        return result

    def create_employee(self, employee: Employee):
        new_employee = EmployeeModel(**employee.dict())
        self.db.add(new_employee)
        self.db.commit()
        return

    def update_employee(self, id: int, data: Employee):
        employee = self.db.query(EmployeeModel).filter(
            EmployeeModel.id == id).first()
        employee.name = data.name
        employee.nationality = data.nationality
        employee.role = data.role
        employee.birth_date = data.birth_date
        employee.avatar = data.avatar
        employee.department_id = data.department_id
        self.db.commit()
        return

    def delete_employee(self, id: int):
        self.db.query(EmployeeModel).filter(
            EmployeeModel.id == id).delete()
        self.db.commit()
        return
