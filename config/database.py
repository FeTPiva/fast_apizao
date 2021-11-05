from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class config_sql_do_inferno():
    def __init__(self):
        self.host = 'localhost'
        self.db = 'teste'
        self.username = 'root'
        self.passw = '12345678'

        self.engine = create_engine(f"mysql+pymysql://{self.username}:{self.passw}@{self.host}/{self.db}?charset=utf8mb4")

        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=self.engine)
        self.Base = declarative_base()
        pass


    def return_base(self):
        return self.Base
