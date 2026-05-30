from pydantic import BaseModel
from typing import Optional

class TareaSchema(BaseModel):
    titulo: str
    description: Optional[str] = None
    completed: bool = False 

    class Config:
        from_attributes = True

