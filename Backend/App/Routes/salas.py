from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Sala

router = APIRouter(prefix="/salas", tags=["Salas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def crear_sala(nombre: str, facultad: str, estado: str, db: Session = Depends(get_db)):
    nueva = Sala(nombre=nombre, facultad=facultad, estado=estado)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/")
def listar_salas(db: Session = Depends(get_db)):
    return db.query(Sala).all()