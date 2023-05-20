import datetime
from sqlalchemy import orm, Column, String, Integer, Float

from .db_session import SqlAlchemyBase



class Management(SqlAlchemyBase):
    __tablename__ = 'management'
    id = Column(Integer, primary_key=True)
    budget = Column(Float)
    personnel = Column(Integer)
    schedule = Column(String(500))