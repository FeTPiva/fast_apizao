from sqlalchemy.orm import Session
from model.model import table_teste
from schemas.schemas import teste_schema


def listar_tudo(db:Session):
    return db.query(table_teste).all()





