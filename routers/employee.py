from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from services.employee import EmployeeService
from schemas.employee import Employee

employee_router = APIRouter()


@employee_router.get('/employees', tags=['employee'], response_model=List[Employee], status_code=200)
def get_employee() -> List[Employee]:
    db = Session()
    result = EmployeeService(db).get_employees()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@employee_router.get('/employee/{id}', tags=['employee'], response_model=Employee)
def get_employee(id: int) -> Employee:
    db = Session()
    result = EmployeeService(db).get_employee(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@employee_router.post('/employees', tags=['employee'], response_model=dict, status_code=201)
def create_employee(employee: Employee) -> dict:
    db = Session()
    EmployeeService(db).create_employee(employee)
    return JSONResponse(status_code=201, content={"message": "Created"})


@employee_router.put('/employee/{id}', tags=['employee'], response_model=dict, status_code=200)
def update_employee(id: int, employee: Employee) -> List:
    db = Session()
    result = EmployeeService(db).get_employee(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    EmployeeService(db).update_employee(id, employee)
    return JSONResponse(status_code=200, content={"message": "Updated"})


@employee_router.delete('/employee/{id}', tags=['employee'], response_model=dict, status_code=200)
def delete_employee(id: int) -> dict:
    db = Session()
    result = EmployeeService(db).get_employee(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    EmployeeService(db).delete_employee(id)
    return JSONResponse(status_code=200, content={"message": "Deleted"})
