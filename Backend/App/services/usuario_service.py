from sqlalchemy.orm import Session
from app.models.usuario import Usuario


def crear_usuario(data, db: Session):
    nuevo = Usuario(
        nombre=data.nombre,
        correo=data.correo
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo