from fastapi import APIRouter, Depends
from uuid import UUID

from app.common.api.dependencies.get_db import SessionDependency
from app.cities.schemas.city_schema import (
    ListCitiesRequest,
    ListCitiesResponse,
    CityResponse,
)
from app.cities.use_cases.list_cities_use_case import ListCitiesUseCase
from app.cities.use_cases.get_city_use_case import GetCityUseCase
from app.cities.use_cases.delete_city_use_case import DeleteCityUseCase
from fastapi import HTTPException, status
from app.common.exceptions.model_not_found_exception import (
    ModelNotFoundException,
)
from app.cities.use_cases.update_city_use_case import UpdateCityUseCase
from app.cities.schemas.city_schema import UpdateCityRequest
from app.cities.use_cases.create_city_use_case import CreateCityUseCase
from app.cities.schemas.city_schema import CreateCityRequest

router = APIRouter()


@router.get("")
def list_cities(
    session: SessionDependency,
    list_filters: ListCitiesRequest = Depends(),
) -> ListCitiesResponse:
    return ListCitiesUseCase(session).execute(
        ListCitiesRequest(**list_filters.model_dump())
    )


@router.get("/{city_id}")
def get_city(
    session: SessionDependency,
    city_id: UUID,
) -> CityResponse:
    try:
        return GetCityUseCase(session).execute(city_id)
    except ModelNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=e.message
        )


@router.delete("/{city_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_city(
    session: SessionDependency,
    city_id: UUID,
) -> None:
    try:
        return DeleteCityUseCase(session).execute(city_id)
    except ModelNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=e.message
        )


@router.post("")
def create_city(
    session: SessionDependency,
    data: CreateCityRequest,
) -> CityResponse:
    return CreateCityUseCase(session).execute(data)


@router.put("/{city_id}")
def update_city(
    session: SessionDependency,
    city_id: UUID,
    data: UpdateCityRequest,
) -> CityResponse:
    try:
        return UpdateCityUseCase(session).execute(city_id, data)
    except ModelNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=e.message
        )
