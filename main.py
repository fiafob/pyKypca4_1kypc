import json

from data import db_session
from config import user_name, user_password, host_name, \
    database_file_name, ABSOLUTE_PROJECT_PATH, port, database_name


db_session.global_init(user_name, user_password, host_name, port, database_name)
db_sess = db_session.create_session()

def collect_data(source: str, data: str) -> list:
    raw_data = json.loads(data)


def main():
    ...


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
    for user in db_sess.query(Human).filter((Human.id >= 1) | (Human.name.notlike("%1%"))):
        print(user)
    '''