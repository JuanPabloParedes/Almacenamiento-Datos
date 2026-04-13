from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text
from app.db.base import Base


class Sala(Base):
    __tablename__ = "sala"

    idSala = Column(Integer, primary_key=True, index=True)
    idFacultad = Column(Integer, ForeignKey("facultad.idFacultad"))

    codigoSala = Column(String(100))
    nombre = Column(String(100))
    estado = Column(Enum("Habilitada", "Deshabilitada"))
    observaciones = Column(Text)