from pydantic import BaseModel

class ReservaCreate(BaseModel):
    usuario_id: int
    sala_id: int
    fecha: str
    hora_inicio: str
    hora_fin: str