from fastapi import FastAPI
from .Routes import usuarios, salas, reservas

app = FastAPI(title="API Reservas")

app.include_router(usuarios.router)
app.include_router(salas.router)
app.include_router(reservas.router)