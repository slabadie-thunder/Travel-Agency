from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from fastapi import status

from app.cities.repositories.cities_repository import cities_repository
from app.cities.schemas.city_schema import (
    CreateCityRequest,
    CityCreate,
    CityResponse,
)
from app.cities.services.cities_service import CitiesService


class CreateCityUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, create_city_request: CreateCityRequest) -> CityResponse:
        cities_service = CitiesService(self.session, cities_repository)
        if cities_service.get_by_name(create_city_request.name):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="City with that name already registered.",
            )

        created_city = cities_service.create_city(
            CityCreate(
                name=create_city_request.name,
            )
        )

        return CityResponse(
            id=created_city.id,
            name=created_city.name,
        )
