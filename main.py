from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return{"mensaje": "¡Hola mundo!"}


@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola, {nombre}!"}
