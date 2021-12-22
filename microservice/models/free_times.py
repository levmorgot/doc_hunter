from pydantic import BaseModel
from typing import List


class FreeDate(BaseModel):
    date: str
    times: List[str]


class FreeTime(BaseModel):
    doctor_name: str
    free_times: List[FreeDate]
