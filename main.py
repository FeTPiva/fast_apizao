from typing import List
from fastapi import FastAPI, Depends
from pydantic.types import StrBytes
from sqlalchemy.orm.session import Session
from config.database import config_sql_do_inferno
from model import model

from model.table_teste import seleciona_tudo

from schemas.schemas import teste_schema

from model.table_teste_alch import listar_tudo

s = config_sql_do_inferno().SessionLocal
e = config_sql_do_inferno().engine

model.base.metadata.create_all(bind=e)

app = FastAPI()

def get_db():
    db = s()
    try:
        yield db
    except:
        db.close()


@app.get("/")
def read_oi():
    return {"hello":"world"}


@app.get("/read", response_model=List[teste_schema])
def read_all(db: Session = Depends(get_db)):
    result = listar_tudo(db)

    #teste_return = teste()
    return result










