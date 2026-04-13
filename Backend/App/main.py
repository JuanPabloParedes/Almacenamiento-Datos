from fastapi import FastAPI

from app.routes.reserva_route import router as reserva_router
from app.routes.usuario_route import router as usuario_router
from app.routes.sala_route import router as sala_router

from db.database import Base, engine

# importar modelos para que SQLAlchemy los registre
from app.models.reserva import Reserva
from app.models.usuario import Usuario
from app.models.sala import Sala

app = FastAPI(title="API Reservas")

# crear tablas en la BD
Base.metadata.create_all(bind=engine)

# incluir rutas
app.include_router(reserva_router)
app.include_router(usuario_router)
app.include_router(sala_router)