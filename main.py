import json

from data import db_session
from config import user_name, user_password, host_name, \
    database_file_name, ABSOLUTE_PROJECT_PATH, port, database_name
from data.passengers import Passenger
from data.flights import Flight
from data.aircrafts import Aircraft, SeatAircraft
from data.luggages import Luggage
from data.maintenances import Maintenance
from data.employees import Employee
from data.securities import Security
from data.managments import Management

table_types = [Aircraft, Passenger, Flight, Luggage,
                     Maintenance, Employee, Security, Management]

db_session.global_init(user_name, user_password, host_name, port, database_name)
db_sess = db_session.create_session()


def collect_data(source: str, data: str) -> list:
    raw_data = json.loads(data)


# Returns list of dictionaries with key, value: table_column, table_value
def get_data_from_db(table_type: table_types) -> list:
    result = db_sess.query(table_type).all()
    for i in range(len(result)):
        result[i] = result[i].__dict__
        result[i].pop('_sa_instance_state', None)
    return result


# Add information in database tables
def set_data_to_db(*args: table_types):
    for data in args:
        db_sess.add(data)
    db_sess.commit()

def main():
    ...


if __name__ == "__main__":
    main()

