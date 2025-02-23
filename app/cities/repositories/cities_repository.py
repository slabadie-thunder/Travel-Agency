from sqlalchemy.orm import Session


from app.common.repositories.base_repository import BaseRepository
from app.cities.models.city import City
from app.cities.schemas.city_schema import CityCreate, CityUpdate


class CitiesRepository(BaseRepository[City, CityCreate, CityUpdate]):
    def get_by_name(self, db: Session, name: str) -> City | None:
        return db.query(self.model).filter(City.name == name).first()


cities_repository = CitiesRepository(City)
