import httpx
from typing import List

from common.utils.cache import redis_cache
from common.utils.speed_test import speed_test

from core.config import BASE_URL
from models.filials import Filial, to_filial


class FilialsRepository:

    @speed_test
    @to_filial
    @redis_cache("filials", 60)
    async def get_all_filials(self):

        url = f"{BASE_URL}filial"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()

        return self._filter_bad_items(response.json()["data"])

    @speed_test
    async def search_filial(
            self,
            search_string: str = "",
            limit: int = 15,
            skip: int = 0
    ) -> List[Filial]:

        all_filials = await self.get_all_filials()
        return [filial for filial in all_filials if
                search_string in filial.name.lower() or search_string in filial.address.lower()][skip: skip + limit]

    def _filter_bad_items(self, data):
        filtered_filials = []
        for filial in data:
            if "cashId" in filial:
                if "address" not in filial:
                    filial["address"] = ""
                if "phone" not in filial:
                    filial["phone"] = ""
                filtered_filials.append(filial)
        return filtered_filials
