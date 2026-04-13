from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.services.reserva_service import (
    crear_reserva,
    listar_reservas,
    obtener_reserva,
    eliminar_reserva
)

router = APIRouter(prefix="/reservas", tags=["Reservas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_reservas(db)


@router.get("/{id}")
def obtener(id: int, db: Session = Depends(get_db)):
    return obtener_reserva(id, db)


@router.post("/")
def crear(data, db: Session = Depends(get_db)):
    return crear_reserva(data, db)


@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    return eliminar_reserva(id, db)