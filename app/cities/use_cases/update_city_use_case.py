from app.cities.schemas.city_schema import CityUpdate, CityResponse, UpdateCityRequest  
from app.cities.services.cities_service import CitiesService
from app.cities.repositories.cities_repository import cities_repository
from sqlalchemy.orm import Session
from uuid import UUID
from app.common.exceptions.model_not_found_exception import ModelNotFoundException


class UpdateCityUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, city_id: UUID, data: UpdateCityRequest) -> CityResponse:
        cities_service = CitiesService(self.session, cities_repository)
        
        city = cities_service.get_by_id(city_id)
        if city is None:
            raise ModelNotFoundException(f"City with id {city_id} not found")

        if data.name is not None:
            cities_service.update(
                city_id,
                CityUpdate(name=data.name)
            )
        
        self.session.commit()

        updated_city = cities_service.get_by_id(city_id)
        
        return CityResponse.model_validate(updated_city)
