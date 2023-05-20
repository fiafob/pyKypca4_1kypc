import datetime
from sqlalchemy import orm, Column, String, Integer, ForeignKey

from .db_session import SqlAlchemyBase

class Passenger(SqlAlchemyBase):
    __tablename__ = 'passengers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    passport_number = Column(String(20), unique=True)
    flight_id = Column(Integer, ForeignKey('flights.id'))
    flight = orm.relationship("Flight")

    def __repr__(self):
        ...