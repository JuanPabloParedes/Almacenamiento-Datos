from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, time

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

@router.get("/")
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(Reserva).all()

@router.post("/")
def crear_reserva(data: ReservaCreate, db: Session = Depends(get_db)):

    if data.horaInicio >= data.horaFin:
        raise HTTPException(400, "Hora inválida")

    if data.horaInicio < time(7, 0) or data.horaFin > time(21, 30):
        raise HTTPException(400, "Fuera de horario")

    existe = db.query(Reserva).filter(
        Reserva.idSala == data.idSala,
        Reserva.fecha == data.fecha,
        Reserva.horaInicio < data.horaFin,
        Reserva.horaFin > data.horaInicio
    ).first()

    if existe:
        raise HTTPException(400, "Reserva solapada")

    nueva = Reserva(
        fecha=data.fecha,
        horaInicio=data.horaInicio,
        horaFin=data.horaFin,
        estado="Activa",
        fechaYHoraCreacion=datetime.now(),
        idUsuario=data.idUsuario,
        idSala=data.idSala,
        idUsuarioResponsable=data.idUsuarioResponsable
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva