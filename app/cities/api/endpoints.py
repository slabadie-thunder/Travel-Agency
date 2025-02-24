from fastapi import APIRouter, Depends

from app.common.api.dependencies.get_db import SessionDependency
from app.cities.schemas.city_schema import ListCitiesRequest, ListCitiesResponse
from app.cities.use_cases.list_cities_use_case import ListCitiesUseCase


router = APIRouter()

@router.get("")
def list_cities(
    session: SessionDependency,
    list_filters: ListCitiesRequest = Depends(),
) -> ListCitiesResponse:
    return ListCitiesUseCase(session).execute(
        ListCitiesRequest(**list_filters.model_dump())
    )