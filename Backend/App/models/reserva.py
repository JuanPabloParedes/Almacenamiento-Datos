from sqlalchemy import Column, Integer, Date, Time, DateTime, Enum, ForeignKey, Text
from app.db.base import Base


class Reserva(Base):
    __tablename__ = "reserva"

    idReserva = Column(Integer, primary_key=True, index=True)

    idSala = Column(Integer, ForeignKey("sala.idSala"))
    idUsuario = Column(Integer, ForeignKey("usuario.idUsuario"))

    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)

    estado = Column(Enum("Activa", "Cancelada", "Ajustada"))

    fecha_creacion = Column(DateTime)

    tipo_evento = Column(Enum("Académica", "Administrativa"))
    descripcion = Column(Text)