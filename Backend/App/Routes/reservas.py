from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Reserva
from ..schemas import ReservaCreate

router = APIRouter(prefix="/reservas", tags=["Reservas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def crear_reserva(data: ReservaCreate, db: Session = Depends(get_db)):

    if data.hora_inicio >= data.hora_fin:
        raise HTTPException(400, "Hora inválida")

    if data.hora_inicio < "07:00" or data.hora_fin > "21:30":
        raise HTTPException(400, "Fuera de horario")

    existe = db.query(Reserva).filter(
        Reserva.sala_id == data.sala_id,
        Reserva.fecha == data.fecha,
        Reserva.hora_inicio < data.hora_fin,
        Reserva.hora_fin > data.hora_inicio
    ).first()

    if existe:
        raise HTTPException(400, "Reserva solapada")

    nueva = Reserva(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva