from datetime import datetime, time
from fastapi import HTTPException
from app.models.reserva import Reserva


def crear_reserva(data, db):

    if data.hora_inicio >= data.hora_fin:
        raise HTTPException(status_code=400, detail="Hora inválida")

    if data.hora_inicio < time(7, 0) or data.hora_fin > time(21, 30):
        raise HTTPException(status_code=400, detail="Fuera de horario")

    existe = db.query(Reserva).filter(
        Reserva.idSala == data.idSala,
        Reserva.fecha == data.fecha,
        Reserva.estado == "Activa",
        Reserva.hora_inicio < data.hora_fin,
        Reserva.hora_fin > data.hora_inicio
    ).first()

    if existe:
        raise HTTPException(status_code=400, detail="Reserva solapada")

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