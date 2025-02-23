from sqlalchemy import Column, String

from app.common.models.base_class import Base


class City(Base):
    __tablename__ = "cities"
    name = Column(String(100), unique=True, nullable=False)
