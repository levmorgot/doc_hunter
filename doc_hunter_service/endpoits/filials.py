from typing import List

from fastapi import APIRouter, Depends

from endpoits.depends import get_filial_repository
from models.filials import Filial
from repositories.filials import FilialsRepository

router = APIRouter()


@router.get("/", response_model=List[Filial])
async def get_all_filials(filials: FilialsRepository = Depends(get_filial_repository)):
    return await filials.get_all_filials()


@router.get("/search/{search_string}", response_model=List[Filial])
async def search_filial(
        search_string: str = "",
        filials: FilialsRepository = Depends(get_filial_repository),
        limit: int = 15,
        skip: int = 0,
):
    return await filials.search_filial(search_string.lower(), limit, skip)
