import datetime
from sqlalchemy import orm, Column, String, Integer, ForeignKey, Float

from .db_session import SqlAlchemyBase



class Luggage(SqlAlchemyBase):
    __tablename__ = 'luggage'
    id = Column(Integer, primary_key=True)
    luggage_number = Column(String(20), unique=True)
    weight = Column(Float)
    type = Column(String(50))
    destination = Column(String(100))
    passenger_id = Column(Integer, ForeignKey('passengers.id'))

    #passenger = orm.relationship("Passenger")

    def __repr__(self):
        return f"Luggage: {self.id} - {self.luggage_number} - "\
            f"{self.weight} - {self.weight} - {self.type} - "\
            f"{self.destination} - "\
            f"__Passenger__: {self.passenger_id} |"