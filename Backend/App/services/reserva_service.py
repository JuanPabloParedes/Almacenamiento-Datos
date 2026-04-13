from sqlalchemy.orm import Session
from datetime import datetime, time

from app.models.reserva import Reserva


# CREAR RESERVA
def crear_reserva(data, db: Session):

    # Validación horas
    if data.hora_inicio >= data.hora_fin:
        raise Exception("Hora inválida")

    if data.hora_inicio < time(7, 0) or data.hora_fin > time(21, 30):
        raise Exception("Fuera de horario")

    # Validar solapamiento
    existe = db.query(Reserva).filter(
        Reserva.idSala == data.idSala,
        Reserva.fecha == data.fecha,
        Reserva.estado == "Activa",
        Reserva.hora_inicio < data.hora_fin,
        Reserva.hora_fin > data.hora_inicio
    ).first()

    if existe:
        raise Exception("Reserva solapada")

    # Crear reserva
    nueva = Reserva(
        idUsuario=data.idUsuario,
        idSala=data.idSala,
        fecha=data.fecha,
        hora_inicio=data.hora_inicio,
        hora_fin=data.hora_fin,
        estado=data.estado if data.estado else "Activa",
        fecha_creacion=datetime.now(),
        tipo_evento=data.tipo_evento,
        descripcion=data.descripcion
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


# LISTAR
def listar_reservas(db: Session):
    return db.query(Reserva).all()


# OBTENER
def obtener_reserva(id: int, db: Session):
    return db.query(Reserva).filter(Reserva.idReserva == id).first()


# ELIMINAR
def eliminar_reserva(id: int, db: Session):
    reserva = db.query(Reserva).filter(Reserva.idReserva == id).first()
    
    if not reserva:
        raise Exception("Reserva no encontrada")

    db.delete(reserva)
    db.commit()

    return {"mensaje": "Reserva eliminada"}