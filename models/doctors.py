from pydantic import BaseModel
from typing import List


class Doctor(BaseModel):
    dcode: int
    name: str


def to_doctor(func):
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        doctors: List[Doctor] = []
        for doctor_json in result:
            doctor = Doctor(
                dcode=doctor_json["dcode"],
                name=doctor_json["name"],
            )
            doctors.append(doctor)
        return doctors

    return wrapper
