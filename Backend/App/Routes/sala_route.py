from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.sala_schema import SalaCreate
from app.services.sala_service import crear_sala
from db.database import get_db

router = APIRouter()


@router.post("/salas")
def crear(data: SalaCreate, db: Session = Depends(get_db)):
    return crear_sala(data, db)