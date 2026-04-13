from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.reserva import Reserva
from app.schemas.reserva_schema import ReservaCreate
from app.services.reserva_service import crear_reserva

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
def crear(data: ReservaCreate, db: Session = Depends(get_db)):
    return crear_reserva(data, db)