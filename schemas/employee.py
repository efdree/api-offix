from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Employee(BaseModel):

    id: Optional[int] = None
    name: str
    nationality: str
    role: str
    birth_date: date
    avatar: str
    department_id: int
