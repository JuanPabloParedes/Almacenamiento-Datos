from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, DateTime, Enum, Text
from .database import Base


class Facultad(Base):
    __tablename__ = "facultad"

    idFacultad = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))


class Usuario(Base):
    __tablename__ = "usuario"

    idUsuario = Column(Integer, primary_key=True, index=True)
    codigoUsuario = Column(String(20), unique=True)
    nombreCompleto = Column(String(50))
    email = Column(String(50), unique=True)
    rol = Column(Enum('Docente', 'Secretaria'))
    estado = Column(Enum('Activo', 'Inactivo'))
    idFacultad = Column(Integer, ForeignKey("facultad.idFacultad"))


class Sala(Base):
    __tablename__ = "sala"

    idSala = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    estado = Column(Enum('Habilitada', 'Inhabilitada'))
    observaciones = Column(Text)
    idFacultad = Column(Integer, ForeignKey("facultad.idFacultad"))


class Reserva(Base):
    __tablename__ = "reserva"

    idReserva = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    horaInicio = Column(Time)
    horaFin = Column(Time)
    estado = Column(Enum('Activa', 'Cancelada', 'Ajustada'))
    fechaYHoraCreacion = Column(DateTime)
    fechaYHoraModificacion = Column(DateTime)
    idUsuario = Column(Integer, ForeignKey("usuario.idUsuario"))
    idSala = Column(Integer, ForeignKey("sala.idSala"))
    idUsuarioResponsable = Column(Integer, ForeignKey("usuario.idUsuario"))


class RecursoDisponible(Base):
    __tablename__ = "recursoDisponible"

    idRecurso = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum('Mobiliario', 'Audiovisual'))
    nombre = Column(String(50))
    idSala = Column(Integer, ForeignKey("sala.idSala"))


class RegistroModificacion(Base):
    __tablename__ = "registroModificacion"

    idModificacion = Column(Integer, primary_key=True, index=True)
    idEntidadModificada = Column(Integer)
    entidad = Column(Enum('Sala', 'Reserva'))
    tipo = Column(Text)
    fecha = Column(Date)
    hora = Column(Time)
    descripcion = Column(Text)
    idUsuario = Column(Integer, ForeignKey("usuario.idUsuario"))