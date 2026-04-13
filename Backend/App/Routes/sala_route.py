from fastapi import APIRouter

router = APIRouter(prefix="/salas", tags=["Salas"])

@router.get("/")
def listar_salas():
    return {"msg": "Lista de salas"}