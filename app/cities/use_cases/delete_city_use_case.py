from app.cities.services.cities_service import CitiesService
from app.cities.repositories.cities_repository import cities_repository
from sqlalchemy.orm import Session
from uuid import UUID


class DeleteCityUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, city_id: UUID) -> None:
        CitiesService(self.session, cities_repository).delete(city_id)
