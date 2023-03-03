from pydantic import BaseModel, Field
from typing import Optional


class Department(BaseModel):

    id: Optional[int] = None
    name: str = Field(min_length=3)
    description: str 
    cover: str
    employee_count: Optional[int] = 0

    class Config:
        schema_extra = {
            "example": {
                "name":"Department",
                "description": "Department Description",
                "cover": "Choose a picture"
            }
        }