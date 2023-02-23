from pydantic import BaseModel, Field
from typing import Optional


class Department(BaseModel):

    id: int
    name: str
    description: str
    cover: str
    employee_count: int
