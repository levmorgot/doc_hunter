from typing import List

from fastapi import APIRouter, Depends

from endpoits.depends import get_free_times_repository
from repositories.free_times import FreeTimesRepository

router = APIRouter()


@router.get("/dates/{filial_id}-{filial_cash_id}-{department_id}-{doctor_id}", response_model=List[str])
async def get_free_dates_for_doctor(
        filial_id: int,
        filial_cash_id: int,
        department_id: int,
        doctor_id: int,
        start: str = None,
        end: str = None,
        free_times: FreeTimesRepository = Depends(get_free_times_repository)
):
    result = await free_times.get_free_dates_for_doctor(filial_id, filial_cash_id, department_id, doctor_id, start, end)
    return result


@router.get("/times/{filial_id}-{filial_cash_id}-{department_id}-{doctor_id}-{date}", response_model=List[str])
async def get_free_times_for_doctor(
        filial_id: int,
        filial_cash_id: int,
        department_id: int,
        doctor_id: int,
        date: str,
        free_times: FreeTimesRepository = Depends(get_free_times_repository)
):
    result = await free_times.get_free_times_for_doctor(filial_id, filial_cash_id, department_id, doctor_id, date)
    return result

