from app.cities.schemas.city_schema import CityResponse
from app.cities.services.cities_service import CitiesService
from app.cities.repositories.cities_repository import cities_repository
from sqlalchemy.orm import Session
from uuid import UUID


class GetCityUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, city_id: UUID) -> CityResponse:
        city = CitiesService(self.session, cities_repository).get_by_id(
            city_id
        )
        return CityResponse.model_validate(city)
