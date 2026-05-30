from fastapi import FastAPI
from app.database.database import engine
from app.models.tarea import Base 
from app.routers import tareas

Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(tareas.router)