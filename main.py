from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Tarea(BaseModel):
    titulo: str
    description: Optional[str] = None
    completada: bool = False


tareas = {}
contador = 0 

@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    global contador
    contador += 1
    tareas[contador] = tarea
    return {"id": contador, "tarea": tarea}

@app.get("/tareas")
def listar_tareas():
    return tareas

@app.get("/tareas/{id}")
def obtener_tarea(id: int):
    if id not in tareas:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tareas[id]

@app.put("/tareas/{id}")
def actualizar_tarea(id: int, tarea: Tarea):
    if id not in tareas:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tareas[id] = tarea
    return tareas[id]

@app.delete("/tareas/{id}")
def borrar_tarea(id: int):
    if id not in tareas:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    del tareas[id]
    return {"mensaje": "Tarea borrada"}
