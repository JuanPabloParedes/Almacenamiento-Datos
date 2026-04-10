from pydantic import BaseModel
from datetime import date, time

class ReservaCreate(BaseModel):
    idUsuario: int
    idSala: int
    idUsuarioResponsable: int
    fecha: date
    horaInicio: time
    horaFin: time