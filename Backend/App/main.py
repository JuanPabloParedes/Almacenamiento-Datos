from fastapi import FastAPI
from app.routes import reserva_route

app = FastAPI()

app.include_router(reserva_route.router)