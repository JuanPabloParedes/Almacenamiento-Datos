from datetime import datetime, time
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.reserva import Reserva


def crear_reserva(data, db: Session):

    if data.hora_inicio >= data.hora_fin:
        raise HTTPException(400, "Hora inválida")

    if data.hora_inicio < time(7, 0) or data.hora_fin > time(21, 30):
        raise HTTPException(400, "Fuera de horario")

    existe = db.query(Reserva).filter(
        Reserva.idSala == data.idSala,
        Reserva.fecha == data.fecha,
        Reserva.estado == "Activa",
        Reserva.hora_inicio < data.hora_fin,
        Reserva.hora_fin > data.hora_inicio
    ).first()

    if existe:
        raise HTTPException(400, "Reserva solapada")

    nueva = Reserva(
        idSala=data.idSala,
        idUsuario=data.idUsuario,
        fecha=data.fecha,
        hora_inicio=data.hora_inicio,
        hora_fin=data.hora_fin,
        estado="Activa",
        fecha_creacion=datetime.now(),
        tipo_evento=data.tipo_evento,
        descripcion=data.descripcion
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


def listar_reservas(db: Session):
    return db.query(Reserva).all()


def obtener_reserva(id: int, db: Session):
    reserva = db.query(Reserva).filter(Reserva.idReserva == id).first()
    if not reserva:
        raise HTTPException(404, "No encontrada")
    return reserva


def eliminar_reserva(id: int, db: Session):
    reserva = db.query(Reserva).filter(Reserva.idReserva == id).first()
    if not reserva:
        raise HTTPException(404, "No encontrada")

    db.delete(reserva)
    db.commit()

    return {"mensaje": "Eliminada"}