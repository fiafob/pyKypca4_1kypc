import datetime
import  sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

class Human(SqlAlchemyBase):
    __tablename__ = "people"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    # Возможно все нижеперечисленные поля надо шифровать
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    patronymic = sqlalchemy.Column(sqlalchemy.String, nullable=True)


    def __repr__(self):
        return f"{self.id} | name: {self.name} | surname: {self.surname} | patronymic: {self.patronymic}"