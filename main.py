from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from app.database.database import Base, SessionLocal, engine
from app.models.tarea import Tarea

Base.metadata.create_all(bind=engine)


app = FastAPI()


class TareaSchema(BaseModel):
    titulo: str
    description: Optional[str] = None
    completada: bool = False

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/tareas")
def crear_tarea(tarea: TareaSchema, db: Session = Depends(get_db)):
    nueva_tarea = Tarea(**tarea.model_dump())
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea


@app.get("/tareas")
def listar_tareas(db: Session = Depends(get_db)):
    return db.query(Tarea).all()



@app.get("/tareas/{id}")
def obtener_tarea(id: int, db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea



@app.put("/tareas/{id}")
def actualizar_tarea(id: int, tarea: TareaSchema, db: Session = Depends(get_db)):
    tarea_db = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    for key, value in tarea.model_dump().items():
        setattr(tarea_db, key, value)
    db.commit
    db.refresh(tarea_db)



@app.delete("/tareas/{id}")
def borrar_tarea(id: int, db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(tarea)
    db.commit()
    return {"mensaje": "Tarea borrada "}

