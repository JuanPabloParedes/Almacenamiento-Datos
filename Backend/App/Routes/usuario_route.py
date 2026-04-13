from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.usuario_schema import UsuarioCreate
from app.services.usuario_service import crear_usuario
from db.database import get_db

router = APIRouter()


@router.post("/usuarios")
def crear(data: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario(data, db)