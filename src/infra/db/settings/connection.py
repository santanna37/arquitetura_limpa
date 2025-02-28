from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__(self)-> None:
        """Variavel de ambiente para conectar com o banco de dados """
        self.__connection_string = "mysql+pymysql://root:senha@localhost/clean_database"
        #                          "tipo do banco://usuario:senha@ip de conexão/database "
        

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine 

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind = self.__engine)
        self.session = session_make()
        return self.session 

    def __exit__(self,exc_type, exc_val, exc_tb):
        self.session.close()