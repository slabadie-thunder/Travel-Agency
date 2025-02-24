from uuid import UUID

from pydantic import BaseModel, ConfigDict

from typing import List
from app.common.schemas.pagination_schema import ListFilter, ListResponse

class CityBase(BaseModel):
    name: str


class CityCreate(BaseModel):
    name: str


class CityUpdate(BaseModel):
    name: str | None = None


class CityInDB(CityBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID


class CityResponse(CityInDB):
    pass


class CreateCityRequest(BaseModel):
    name: str


class ListCitiesRequest(ListFilter):
    name: str | None = None


class ListCitiesResponse(ListResponse[CityResponse]):
    data: List[CityResponse]
