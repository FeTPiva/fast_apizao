from typing import List, Optional

from pydantic import BaseModel


class teste_schema(BaseModel):
    nome: str 
    qqlr_coisa:str
    
    class Config:
        orm_mode = True
