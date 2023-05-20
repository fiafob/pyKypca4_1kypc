import datetime
from sqlalchemy import orm, Column, String, Integer, ForeignKey, DateTime

from .db_session import SqlAlchemyBase


class Flight(SqlAlchemyBase):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True)
    flight_number = Column(String(10), unique=True)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    departure_city = Column(String(50))
    arrival_city = Column(String(50))
    aircraft_id = Column(Integer, ForeignKey('aircrafts.id'))

    #aircraft = orm.relationship("Aircraft")

    def __repr__(self):
        return f"| Flight: {self.id} - {self.flight_number} - "\
            f"{self.departure_city} - {self.arrival_city} - "\
            f"{self.departure_time} - {self.arrival_time} - "\
            f"__Aircraft__: {self.aircraft_id} |"