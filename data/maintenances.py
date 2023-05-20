import datetime
from sqlalchemy import orm, Column, String, Integer, ForeignKey, DateTime

from .db_session import SqlAlchemyBase


class Maintenance(SqlAlchemyBase):
    __tablename__ = 'maintenance'
    id = Column(Integer, primary_key=True)
    work_type = Column(String(100))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    flight_id = Column(Integer, ForeignKey('flights.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))

    flight = orm.relationship("Flight")
    employee = orm.relationship("Employee")