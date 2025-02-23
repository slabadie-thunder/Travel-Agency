from uuid import UUID

from sqlalchemy.orm import Session

from app.common.schemas.pagination_schema import ListFilter, ListResponse
from app.cities.repositories.cities_repository import CitiesRepository
from app.cities.schemas.city_schema import CityCreate, CityInDB


class CitiesService:
    def __init__(self, session: Session, repository: CitiesRepository):
        self.session = session
        self.repository = repository

    def get_by_name(self, name: str) -> CityInDB | None:
        city = self.repository.get_by_name(self.session, name)
        if not city:
            return None
        return CityInDB.model_validate(city)

    def get_by_id(self, city_id: UUID) -> CityInDB | None:
        city = self.repository.get(self.session, city_id)
        if not city:
            return None
        return CityInDB.model_validate(city)

    def create_city(self, city: CityCreate) -> CityInDB:
        created_city = self.repository.create(self.session, city)
        return CityInDB.model_validate(created_city)

    def list(self, list_options: ListFilter) -> ListResponse:
        return self.repository.list(self.session, list_options)
