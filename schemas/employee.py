from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Employee(BaseModel):

    id: Optional[int] = None
    name: str = Field(min_length=3)
    nationality: str
    role: str
    birth_date: date
    avatar: str
    department_id: int

    class Config:
        schema_extra = {
            "example": {
                "name":"Juan",
                "nationality":"Peruano",
                "role":"Admin",
                "birth_date":"2020-02-02",
                "avatar":"Upload your avatar",
                "department_id": 0
            }
        }
