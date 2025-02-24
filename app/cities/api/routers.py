from fastapi import APIRouter

from app.cities.api import endpoints

api_router = APIRouter()
api_router.include_router(endpoints.router, prefix="/cities", tags=["cities"])
