from models.model import Department as DepartmentModel
from schemas.department import Department


class DepartmentService():

    def __init__(self, db) -> None:
        self.db = db

    def get_departments(self):
        result = self.db.query(DepartmentModel).all()
        return result

    def get_department(self, id):
        result = self.db.query(DepartmentModel).filter(
            DepartmentModel.id == id).first()
        return result

    def create_department(self, department: Department):
        new_department = DepartmentModel(**department.dict())
        self.db.add(new_department)
        self.db.commit()
        return

    def update_department(self, id: int, data: Department):
        department = self.db.query(DepartmentModel).filter(
            DepartmentModel.id == id).first()
        department.name = data.name
        department.description = data.description
        department.cover = data.cover
        department.employee_count = data.employee_count
        self.db.commit()
        return

    def delete_department(self, id: int):
        self.db.query(DepartmentModel).filter(
            DepartmentModel.id == id).delete()
        self.db.commit()
        return
