from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔹 conexión directa (sin config para evitar errores)
DATABASE_URL = "mysql+pymysql://root:jeipi@localhost:3306/proyecto"

# 🔹 motor de conexión
engine = create_engine(
    DATABASE_URL,
    echo=True  # opcional: muestra queries en consola
)

# 🔹 sesión de base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 🔹 base para modelos
Base = declarative_base()


# 🔹 dependencia para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()