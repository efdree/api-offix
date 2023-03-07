from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List, Dict
from config.database import Session
from fastapi import APIRouter
from services.department import DepartmentService
from schemas.department import Department
from fastapi.encoders import jsonable_encoder

from services.employee import EmployeeService
from schemas.employee import Employee

department_router = APIRouter()


@department_router.get('/departments', tags=['department'], response_model=List[Department], status_code=200)
def get_department() -> List[Department]:
    db = Session()
    result = DepartmentService(db).get_departments()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@department_router.get('/department/{id}', tags=['department'], response_model=Dict[Department, Employee], status_code=200)
def get_department(id: int = Path(ge=1)) -> Dict[Department, Employee]:
    db = Session()
    result_department = DepartmentService(db).get_department(id)
    if not result_department:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    result_employees = EmployeeService(db).get_employee_by_department(id)
    return JSONResponse(status_code=200, content=jsonable_encoder([result_department, result_employees]))

@department_router.post('/departments', tags=['department'], response_model=dict, status_code=201)
def create_department(department: Department) -> dict:
    db = Session()
    DepartmentService(db).create_department(department)
    return JSONResponse(status_code=201, content={"message": "Created"})


@department_router.put('/department/{id}', tags=['department'], response_model=dict, status_code=200)
def update_department(id: int, department: Department) -> List:
    db = Session()
    result = DepartmentService(db).get_department(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    DepartmentService(db).update_department(id, department)
    return JSONResponse(status_code=200, content={"message": "Updated"})


@department_router.delete('/department/{id}', tags=['department'], response_model=dict, status_code=200)
def delete_department(id: int) -> dict:
    db = Session()
    result = DepartmentService(db).get_department(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    result_employees = EmployeeService(db).get_employee_by_department(id)
    for employee in result_employees:
        employee.department_id = 0
        EmployeeService(db).update_employee(employee.id, employee)
    DepartmentService(db).delete_department(id)
    return JSONResponse(status_code=200, content={"message": "Deleted"})
