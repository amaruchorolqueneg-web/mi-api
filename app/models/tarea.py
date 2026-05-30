from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base

class Tarea(Base):
    __tablename__ = "tareas"


    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completada = Column(Boolean, default=False)

