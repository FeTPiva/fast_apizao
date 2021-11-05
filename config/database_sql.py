import mysql.connector


class conf_db():
    def __init__(self):
        pass

    def con_mysql(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="teste"
            )
        
        return mydb





