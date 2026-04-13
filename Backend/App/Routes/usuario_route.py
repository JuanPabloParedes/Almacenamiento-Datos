from fastapi import APIRouter

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/")
def listar_usuarios():
    return {"msg": "Lista de usuarios"}