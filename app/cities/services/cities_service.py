from uuid import UUID

from sqlalchemy.orm import Session

from app.common.schemas.pagination_schema import ListFilter, ListResponse
from app.cities.repositories.cities_repository import CitiesRepository
from app.cities.schemas.city_schema import CityCreate, CityInDB, CityUpdate
from app.common.exceptions.model_not_found_exception import ModelNotFoundException


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

    def delete(self, city_id: UUID) -> None:
        city = self.repository.get(self.session, city_id)
        if not city:
            raise ModelNotFoundException(f"City with id {city_id} not found")
        
        self.repository.delete(self.session, city_id)

    def update(self, city_id: UUID, data: CityUpdate) -> CityInDB:
        city = self.repository.get(self.session, city_id)
        if not city:
            raise ModelNotFoundException(f"City with id {city_id} not found")
        
        city = self.repository.update(self.session, city, data)

        self.session.commit()
        return CityInDB.model_validate(city)
