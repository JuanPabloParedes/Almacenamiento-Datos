from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, time

from ..database import SessionLocal
from ..models import Reserva, Sala
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

    # Validación básica
    if data.hora_inicio >= data.hora_fin:
        raise HTTPException(400, "Hora inválida")

    # Validación horario (igual que trigger)
    if data.hora_inicio < time(7, 0) or data.hora_fin > time(21, 30):
        raise HTTPException(400, "Fuera de horario")

    # Validar sala habilitada
    sala = db.query(Sala).filter(Sala.idSala == data.idSala).first()

    if not sala:
        raise HTTPException(404, "Sala no existe")

    if sala.estado == "Deshabilitada":
        raise HTTPException(400, "Sala deshabilitada")

    # Validar solapamiento
    existe = db.query(Reserva).filter(
        Reserva.idSala == data.idSala,
        Reserva.fecha == data.fecha,
        Reserva.estado == "Activa",
        Reserva.hora_inicio < data.hora_fin,
        Reserva.hora_fin > data.hora_inicio
    ).first()

    if existe:
        raise HTTPException(400, "Reserva solapada")

    # Crear reserva
    nueva = Reserva(
        fecha=data.fecha,
        hora_inicio=data.hora_inicio,
        hora_fin=data.hora_fin,
        estado="Activa",
        fecha_creacion=datetime.now(),
        idUsuario=data.idUsuario,
        idSala=data.idSala,
        tipo_evento=data.tipo_evento,
        descripcion=data.descripcion
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva