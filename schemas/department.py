from pydantic import BaseModel
from typing import Optional


class Department(BaseModel):

    id: Optional[int] = None
    name: str
    description: str
    cover: str
    employee_count: Optional[int] = 0
