
from mysql.connector import connection
from config.database_sql import conf_db
from schemas.schemas import teste_schema
import json

def seleciona_tudo():
    objeto = conf_db()
    connection = objeto.con_mysql()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM table_teste")
    myresult = cursor.fetchall()

    print(json.dumps(myresult))

    return myresult

    
    