from pydantic import BaseModel
from datetime import date, time, datetime

class ReservaBase(BaseModel):
    idSala: int
    idUsuario: int
    fecha: date
    hora_inicio: time
    hora_fin: time
    tipo_evento: str
    descripcion: str

class ReservaCreate(ReservaBase):
    pass

class ReservaUpdate(BaseModel):
    hora_inicio: time | None = None
    hora_fin: time | None = None
    tipo_evento: str | None = None
    descripcion: str | None = None
    estado: str | None = None

class ReservaResponse(ReservaBase):
    idReserva: int
    estado: str
    fecha_creacion: datetime

    class Config:
        from_attributes = True