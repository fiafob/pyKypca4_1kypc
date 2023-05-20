import json

from sqlalchemy import exc

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
    print(*get_data_from_db(Employee))
    try:
        # suppose the database has been restarted.
        print(*get_data_from_db(Employee))
    except exc.DBAPIError as e:
        # an exception is raised, Connection is invalidated.
        if e.connection_invalidated:
            print("Connection was invalidated!")

    # set_tests()
    # print(*get_data_from_db(Aircraft), sep='\n')

    # et1 = Employee(first_name="Акакий",
    #                last_name="Алексеев",
    #                patronymic="Александрович",
    #                position="Директор говна"
    #                )
    # db_sess.add(et1)
    # db_sess.commit()

    # print(et1)



if __name__ == "__main__":
    main()



# create line in table people
    '''
    human = Human()
    human.name = "Ivan"
    human.surname = "Ivanov"
    human.patronymic = "Ivanovich"
    db_sess.add(human)
    db_sess.commit()
    print(human)
    '''

# select people from table poeople
    '''
    for user in db_sess.query(Human).filter((Human.id >= 1) | \
    (Human.name.notlike("%1%"))):
        print(user)
    '''