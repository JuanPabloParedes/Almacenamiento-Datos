from pydantic import BaseModel, Field
from datetime import date, time
from typing import Optional


class ReservaCreate(BaseModel):
    idUsuario: int = Field(..., example=1)
    idSala: int = Field(..., example=1)

    fecha: date = Field(..., example="2026-04-20")

    hora_inicio: time = Field(..., example="08:00:00")
    hora_fin: time = Field(..., example="10:00:00")

    tipo_evento: str = Field(..., example="Academica")
    descripcion: Optional[str] = Field(None, example="Clase de bases de datos")

    estado: Optional[str] = Field("Activa", example="Activa")