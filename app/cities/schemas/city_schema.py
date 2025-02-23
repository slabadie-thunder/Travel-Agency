from uuid import UUID

from pydantic import BaseModel, ConfigDict


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
