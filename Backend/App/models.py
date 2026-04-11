from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, DateTime, Enum, Text
from .database import Base


class Facultad(Base):
    __tablename__ = "Facultad"

    idFacultad = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    descripciones = Column(Text)


class Usuario(Base):
    __tablename__ = "Usuario"

    idUsuario = Column(Integer, primary_key=True, index=True)
    idFacultad = Column(Integer, ForeignKey("Facultad.idFacultad"))
    nombre_completo = Column(String(100))
    correo_institucional = Column(String(255), unique=True)
    rol = Column(Enum('Docente', 'Secretaria'))
    estado = Column(Enum('Activo', 'Inactivo'))


class Sala(Base):
    __tablename__ = "Sala"

    idSala = Column(Integer, primary_key=True, index=True)
    idFacultad = Column(Integer, ForeignKey("Facultad.idFacultad"))
    codigo_sala = Column(String(100))
    nombre = Column(String(100))
    estado = Column(Enum('Habilitada', 'Deshabilitada'))
    observaciones = Column(Text)


class Reserva(Base):
    __tablename__ = "Reserva"

    idReserva = Column(Integer, primary_key=True, index=True)
    idSala = Column(Integer, ForeignKey("Sala.idSala"))
    idUsuario = Column(Integer, ForeignKey("Usuario.idUsuario"))

    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)

    estado = Column(Enum('Activa', 'Cancelada', 'Ajustada'))
    fecha_creacion = Column(DateTime)

    tipo_evento = Column(Enum('Academica', 'Administrativa'))
    descripcion = Column(Text)