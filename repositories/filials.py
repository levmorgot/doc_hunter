import httpx
from typing import List

from common.utils.cache import redis_cache
from core.config import BASE_URL
from models.filials import Filial, to_filial


class FilialsRepository:

    @to_filial
    @redis_cache("filials", 60)
    async def get_all_filials(self):

        url = f"{BASE_URL}filial"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()

        data = response.json()["data"]
        filials_json = []
        for filial_json in data:
            if "cashId" in filial_json:
                if "address" not in filial_json:
                    filial_json["address"] = ""
                if "phone" not in filial_json:
                    filial_json["phone"] = ""
                filials_json.append(filial_json)

        return filials_json

    async def search_filial(self, search_string: str = "", limit: int = 15, skip: int = 0) -> List[Filial]:
        all_filials = await self.get_all_filials()
        return [filial for filial in all_filials if
                search_string in filial.name.lower() or search_string in filial.address.lower()][skip: skip + limit]
