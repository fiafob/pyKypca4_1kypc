import psycopg2
import os
from config import ABSOLUTE_PROJECT_PATH, database_name, \
    database_file_name, user_name, user_password, host_name, table_names

absolute_database_path = ABSOLUTE_PROJECT_PATH + database_file_name

def is_database_exists(database_file_name):
    return os.path.isfile(absolute_database_path)

is_first_launch = False
def create_database():
    if not is_database_exists(database_file_name):
        new_file = open(absolute_database_path, 'x')
        new_file.close()
        is_first_launch = True

def first_launch():
    if is_first_launch:
        is_first_launch = False
        # cursor = conn.cursor()

        curs.execute(f'CREATE DATABASE {database_name} WITH owner={user_name}')
        curs.fetchall()

        for table_name in table_names:
            curs.execute(f"CREATE TABLE {table_name}()")


def create_connection(path):
    connection = None
    try:
        # пытаемся подключиться к базе данных
        connection = psycopg2.connect(dbname=database_name, user=user_name,
                                password=user_password, host=host_name)
        # or
        # conn = psycopg2.connect(
        # 'postgresql://{user_name}:{user_password}@{host_name}:{port}/{database_name}')
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')

    return connection


if __name__ == "__main__":
    create_connection(database_name, )


