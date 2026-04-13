from sqlalchemy.orm import Session
from app.models.sala import Sala


def crear_sala(data, db: Session):
    nueva = Sala(
        nombre=data.nombre,
        capacidad=data.capacidad
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva