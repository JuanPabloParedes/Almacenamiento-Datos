from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuario"

    idUsuario = Column(Integer, primary_key=True, index=True)
    idFacultad = Column(Integer, ForeignKey("facultad.idFacultad"))

    nombreCompleto = Column(String(100))
    correoInstitucional = Column(String(100))

    rol = Column(Enum("Docente", "Secretaria"))
    estado = Column(Enum("Activo", "Inactivo"))