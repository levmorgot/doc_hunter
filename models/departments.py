from pydantic import BaseModel
from typing import List


class Department(BaseModel):
    id: int
    name: str


def to_department(func):
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        departments: List[Department] = []
        for department_json in result:
            department = Department(
                id=department_json["id"],
                name=department_json["name"],
            )
            departments.append(department)
        return departments

    return wrapper
