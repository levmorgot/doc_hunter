from typing import List
import datetime
from fastapi import APIRouter, Depends

from endpoits.depends import get_doctors_repository
from models.doctors import Doctor
from repositories.doctors import DoctorsRepository

router = APIRouter()


@router.get("/{filial_id}-{filial_cash_id}-{department_id}", response_model=List[Doctor])
async def get_all_doctors_in_department(
        filial_id: int,
        filial_cash_id: int,
        department_id: int,
        departments: DoctorsRepository = Depends(get_doctors_repository)
):
    start = datetime.datetime.now()
    result = await departments.get_all_doctors_in_department(filial_id, filial_cash_id, department_id)
    end = datetime.datetime.now()
    print(end - start)
    return result


@router.get("/{filial_id}-{filial_cash_id}-{department_id}/search/{search_string}", response_model=List[Doctor])
async def search_doctors_in_department(
        filial_id: int,
        filial_cash_id: int,
        department_id: int,
        search_string: str = "",
        departments: DoctorsRepository = Depends(get_doctors_repository),
        limit: int = 15,
        skip: int = 0,
):
    return await departments.search_doctors_in_department(filial_id, filial_cash_id, department_id,
                                                          search_string.lower(), limit, skip)
