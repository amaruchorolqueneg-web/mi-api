from fastapi import FastAPI
from app.database.database import engine
from app.models.tarea import Base as TareaBase
from app.models.usuario import Usuario
from app.models.tarea import Tarea
from app.routers import auth, tareas



TareaBase.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(tareas.router)
app.include_router(auth.router)