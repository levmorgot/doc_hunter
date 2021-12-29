from typing import List

from fastapi import APIRouter, Depends

from common.endpoits.depends import get_doctors_repository
from doctors.models import Doctor
from doctors.repositories import DoctorsRepository

router = APIRouter()


@router.get("/{filial_id}-{filial_cash_id}-{department_id}", response_model=List[Doctor])
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
