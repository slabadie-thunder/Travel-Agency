from uuid import UUID

from pydantic import BaseModel, ConfigDict

from typing import List
from app.common.schemas.pagination_schema import ListFilter, ListResponse


class CityBase(BaseModel):
    name: str


class CityCreate(CityBase):
    pass


class CityUpdate(BaseModel):
    pass


class CityInDB(CityBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID


class CityResponse(CityInDB):
    pass


class CreateCityRequest(CityBase):
    pass


class ListCitiesRequest(ListFilter):
    name: str | None = None


class ListCitiesResponse(ListResponse[CityResponse]):
    data: List[CityResponse]


class UpdateCityRequest(CityBase):
    pass
