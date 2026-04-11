from pydantic import BaseModel
from datetime import date, time

class ReservaCreate(BaseModel):
    idUsuario: int
    idSala: int
    fecha: date
    hora_inicio: time
    hora_fin: time
    tipo_evento: str
    descripcion: str