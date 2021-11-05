from config.database import config_sql_do_inferno
from sqlalchemy import Column, Integer, String

objetoooo = config_sql_do_inferno()
base = objetoooo.return_base()

class table_teste(base):
    __tablename__ = "table_teste"

    id = Column(Integer, nullable=True, primary_key = True)
    nome = Column(String(45), nullable=False )
    qqlr_coisa = Column(String(45), nullable=False )