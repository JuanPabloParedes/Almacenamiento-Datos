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

@router.get("/")
def listar_salas(db: Session = Depends(get_db)):
    return db.query(Sala).all()