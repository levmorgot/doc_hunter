import httpx
from typing import List

from common.utils.cache import redis_cache
from common.utils.speed_test import speed_test
from core.config import BASE_URL
from models.departments import to_department, Department


class DepartmentsRepository:

    @speed_test
    @to_department
    @redis_cache("departments", 60*60*12)
    async def get_all_departments_in_filial(self, filial_id, filial_cash_id):
        url = f"{BASE_URL}api/reservation/departments?f={filial_id}&s={filial_cash_id}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
        data = response.json()["data"]

        return data

    @speed_test
    async def search_departments_in_filial(
            self,
            filial_id,
            filial_cash_id,
            search_string: str = "",
            limit: int = 15,
            skip: int = 0
    ) -> List[Department]:
        all_departments = await self.get_all_departments_in_filial(filial_id, filial_cash_id)
        return [department for department in all_departments if search_string in department.name.lower()][
               skip: skip + limit]
