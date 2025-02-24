from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from fastapi import status

from app.cities.repositories.cities_repository import cities_repository
from app.cities.schemas.city_schema import (
    CityCreate,
    CityResponse,
    ListCitiesRequest,
    ListCitiesResponse,
)
from app.cities.services.cities_service import CitiesService


class ListCitiesUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, list_cities_request: ListCitiesRequest) -> ListCitiesResponse:
        return CitiesService(self.session, cities_repository).list(
            list_cities_request
        )
