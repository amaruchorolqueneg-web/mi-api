from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    email: str
    password: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    