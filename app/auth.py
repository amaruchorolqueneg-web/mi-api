from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext


SECRET_KEY = "mi_clave_secreta_123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", truncate_error=False)

def hashear_password(password: str):
    return pwd_context.hash(password)

def verificar_password(password: str, hash: str):
    return pwd_context.verify(password, hash)

def crear_token(data: dict):
    datos = data.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    datos.update({"exp": expiracion})
    return jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            return None
        return email
    except JWTError:
        return None
    
