from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query


from app.common.repositories.base_repository import BaseRepository
from app.cities.models.city import City
from app.cities.schemas.city_schema import CityCreate, CityUpdate
from app.common.schemas.pagination_schema import ListFilter, ListResponse


class CitiesRepository(BaseRepository[City, CityCreate, CityUpdate]):
    def get_by_name(self, db: Session, name: str) -> City | None:
        return db.query(self.model).filter(City.name == name).first()

    def list(
        self, db: Session, list_options: ListFilter, query: Query | None = None
    ) -> ListResponse:
        query = db.query(self.model)
        if list_options.name:
            query = query.filter_by(name=list_options.name)
        return super().list(db, list_options, query)


cities_repository = CitiesRepository(City)
