import datetime
from sqlalchemy import orm, Column, String, Integer, ForeignKey

from .db_session import SqlAlchemyBase


class Aircraft(SqlAlchemyBase):
    __tablename__ = 'aircrafts'
    id = Column(Integer, primary_key=True)
    model = Column(String(50))
    capacity = Column(Integer)
    manufacturer = Column(String(50))

    def __repr__(self):
        return f"| Aircraft: {self.id} - {self.model} -" \
            f" {self.capacity} - {self.manufacturer} |"


class SeatAircraft(SqlAlchemyBase):
    __tablename__ = 'seat_aircraft'
    id = Column(Integer, primary_key=True)
    seat = Column(String(10))
    aircraft_id = Column(Integer, ForeignKey('aircrafts.id'))
    seat_type = Column(String(50))

    aircraft = orm.relationship("Aircraft")

    def __repr__(self):
        return f"| Seat - {self.id} - {self.row}{self.letter}"\
            f" - {self.seat_type} - "\
            f"__Aircraft__: {self.aircraft_id} |"