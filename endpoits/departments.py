from typing import List
import datetime
from fastapi import APIRouter, Depends

from endpoits.depends import get_departments_repository
from models.departments import Department
from repositories.departments import DepartmentsRepository

router = APIRouter()


@router.get("/{filial_id}-{filial_cash_id}", response_model=List[Department])
async def get_all_departments_in_filial(
        filial_id: int,
        filial_cash_id: int,
        departments: DepartmentsRepository = Depends(get_departments_repository)
):
    start = datetime.datetime.now()
    result = await departments.get_all_departments_in_filial(filial_id, filial_cash_id)
    end = datetime.datetime.now()
    print(end - start)
    return result


@router.get("/{filial_id}-{filial_cash_id}/search/{search_string}", response_model=List[Department])
async def search_departments_in_filial(
        filial_id: int,
        filial_cash_id: int,
        search_string: str = "",
        departments: DepartmentsRepository = Depends(get_departments_repository),
        limit: int = 15,
        skip: int = 0,
):
    return await departments.search_departments_in_filial(filial_id, filial_cash_id, search_string.lower(), limit, skip)