import datetime
from sqlalchemy import orm, Column, String, Integer, ForeignKey, DateTime

from .db_session import SqlAlchemyBase

class Security(SqlAlchemyBase):
    __tablename__ = 'security'
    id = Column(Integer, primary_key=True)
    check_type = Column(String(100))
    check_time = Column(DateTime)
    passenger_id = Column(Integer, ForeignKey('passengers.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))

    passenger = orm.relationship("Passenger")
    employee = orm.relationship("Employee")

    def __repr__(self):
        return f"| Security: {self.id} - "\
                f"{self.check_type} - {self.check_time} - "\
                f"__Passenger__: {self.passenger_id} - "\
                f"__Employee__: {self.employee_id} |"