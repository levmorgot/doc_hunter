import httpx
from typing import List

from common.utils.cache import redis_cache
from common.utils.speed_test import speed_test
from core.config import BASE_URL
from doctors.models import Doctor, to_doctor


class DoctorsRepository:

    @speed_test
    @to_doctor
    @redis_cache("doctors", 60*60*12)
    async def get_all_doctors_in_department(self, filial_id, filial_cash_id, department_id):
        url = f"{BASE_URL}api/reservation/doctors?f={filial_id}&s={filial_cash_id}&d={department_id}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
        data = response.json()["data"]

        return data

    @speed_test
    async def search_doctors_in_department(
            self,
            filial_id,
            filial_cash_id,
            department_id,
            search_string: str = "",
            limit: int = 15,
            skip: int = 0
    ) -> List[Doctor]:
        all_doctors = await self.get_all_doctors_in_department(filial_id, filial_cash_id, department_id)
        return [doctor for doctor in all_doctors if search_string in doctor.name.lower()][skip: skip + limit]
