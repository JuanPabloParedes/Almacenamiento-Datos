from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    correo = Column(String(100))
    rol = Column(String(20))

class Sala(Base):
    __tablename__ = "salas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    facultad = Column(String(100))
    estado = Column(String(20))

class Reserva(Base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    sala_id = Column(Integer, ForeignKey("salas.id"))
    fecha = Column(String(20))
    hora_inicio = Column(String(10))
    hora_fin = Column(String(10))