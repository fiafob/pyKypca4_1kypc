import datetime
from sqlalchemy import orm, Column, String, Integer, ForeignKey, DateTime

from .db_session import SqlAlchemyBase


class Employee(SqlAlchemyBase):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    position = Column(String(128))