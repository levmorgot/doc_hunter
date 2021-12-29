from typing import List

from fastapi import APIRouter, Depends

from common.endpoits.depends import get_filial_repository
from filials.models import Filial
from filials.repositories import FilialsRepository

router = APIRouter()


@router.get("/", response_model=List[Filial])
async def search_filial(
        search_string: str = "",
        filials: FilialsRepository = Depends(get_filial_repository),
        limit: int = 15,
        skip: int = 0,
):
    return await filials.search_filial(search_string.lower(), limit, skip)
