from pydantic import BaseModel
from typing import List


class Filial(BaseModel):
    id: int
    cashId: int
    name: str
    address: str
    phone: str


def to_filial(func):
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        filials: List[Filial] = []
        for filial_json in result:
            filial = Filial(
                id=filial_json["id"],
                cashId=filial_json["cashId"],
                name=filial_json["name"],
                address=filial_json["address"],
                phone=filial_json["phone"],
            )
            filials.append(filial)
        return filials

    return wrapper
