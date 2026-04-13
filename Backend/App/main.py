from fastapi import FastAPI

from app.routes.reserva_route import router as reserva_router
from app.routes.usuario_route import router as usuario_router
from app.routes.sala_route import router as sala_router

app = FastAPI(title="API Reservas")

app.include_router(reserva_router)
app.include_router(usuario_router)
app.include_router(sala_router)