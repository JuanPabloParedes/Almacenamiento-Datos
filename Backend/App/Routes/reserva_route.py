from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.reserva_schema import ReservaCreate
from app.services.reserva_service import (
    crear_reserva,
    listar_reservas,
    obtener_reserva,
    eliminar_reserva
)

router = APIRouter(prefix="/reservas", tags=["Reservas"])


# conexión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET - listar
@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_reservas(db)


# GET - por id
@router.get("/{id}")
def obtener(id: int, db: Session = Depends(get_db)):
    return obtener_reserva(id, db)


# 🔥 POST COMPLETO PARA PRUEBAS
@router.post("/crear-completo")
def crear(data: ReservaCreate, db: Session = Depends(get_db)):
    try:
        return crear_reserva(data, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# DELETE
@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    return eliminar_reserva(id, db)