import datetime
from sqlalchemy import orm, Column, String, Integer, ForeignKey

from .db_session import SqlAlchemyBase

class Passenger(SqlAlchemyBase):
    __tablename__ = 'passengers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    patronymic = Column(String(50))
    passport_number = Column(String(20), unique=True)
    flight_id = Column(Integer, ForeignKey('flights.id'))
    seat_id = Column(Integer, ForeignKey("seat_aircraft.id"))

    #flight = orm.relationship("Flight")
    #seat = orm.relationship("SeatAircraft")

    def __repr__(self):
        return f"| Passenger: {self.id} - {self.first_name} "\
            f"{self.last_name} {self.patronymic} - "\
            f"{self.passport_number} - "\
            f"__Flight__: {self.flight_id} - "\
            f"__Seat__: {self.seat_id}"