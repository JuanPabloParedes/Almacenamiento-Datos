from sqlalchemy import Column, Integer, String
from db.database import Base


class Sala(Base):
    __tablename__ = "salas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    capacidad = Column(Integer)