from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioSchema, TokenSchema
from app.auth import hashear_password, verificar_password, crear_token

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=TokenSchema)
def register(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    existe = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="El email ya esta registrado")
    nuevo_usuario = Usuario(
        email=usuario.email,
        password=hashear_password(usuario.password)
    )
    db.add(nuevo_usuario)
    db.commit()
    token = crear_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=TokenSchema)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.email == form_data.username).first()
    if not usuario_db:
        raise HTTPException(status_code=401, detail="Email o password incorrectos")
    if not verificar_password(form_data.password, usuario_db.password):
        raise HTTPException(status_code=401, detail="Email o password incorrectos")
    token = crear_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}
