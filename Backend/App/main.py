from fastapi import FastAPI
from .database import Base, engine
from .routes import usuarios, salas, reservas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Reservas")

app.include_router(usuarios.router)
app.include_router(salas.router)
app.include_router(reservas.router)