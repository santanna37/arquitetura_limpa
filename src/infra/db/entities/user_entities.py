from src.infra.db.settings.base import Base
from sqlalchemy import Column, Integer, String



class UsersEntities(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, autoincrement = True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Users [id = {self.id}, name = {self.first_name} {self.last_name}]"