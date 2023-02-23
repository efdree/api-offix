from config.database import Base
from sqlalchemy import ForeignKey, Column, Integer, String, Date
from sqlalchemy.orm import relationship


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    cover = Column(String)
    employee_count = Column(Integer)

    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    nationality = Column(String)
    role = Column(String)
    birth_date = Column(Date)
    avatar = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="employees")
