import datetime
from sqlalchemy import orm, Column, String, Integer, ForeignKey

from .db_session import SqlAlchemyBase


class Aircraft(SqlAlchemyBase):
    __tablename__ = 'aircrafts'
    id = Column(Integer, primary_key=True)
    model = Column(String(50))
    capacity = Column(Integer)
    manufacturer = Column(String(50))