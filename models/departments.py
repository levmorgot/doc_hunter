from pydantic import BaseModel
from typing import List


class Department(BaseModel):
    id: int
    name: str


def to_department(func):
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        filials: List[Department] = []
        for filial_json in result:
            filial = Department(
                id=filial_json["id"],
                name=filial_json["name"],
            )
            filials.append(filial)
        return filials

    return wrapper
