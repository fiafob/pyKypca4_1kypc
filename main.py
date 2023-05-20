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


import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)

class PassengersView(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(750, 650)
        headings = ["id", "first_name", "last_name", "patronymic", "passport_number",
             "flight_id", "seat_id"]
        # Set up the view and load the data
        self.view = QTableWidget()
        self.view.setColumnCount( len(headings) )
        self.view.setHorizontalHeaderLabels(headings)

        self.view.setRowCount(db_sess.query(Passenger).count())
        columns = self.view.columnCount()
        data = get_data_from_db(Passenger)

        for j in range(len(data)):
            for i in range(columns):
                print([headings[i]])
                self.view.setItem(j, i, QTableWidgetItem(str(data[j].get(headings[i], None))))
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)

def main():
    app = QApplication(sys.argv)
    win = PassengersView()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

