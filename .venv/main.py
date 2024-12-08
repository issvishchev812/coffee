import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.uic import loadUi
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        loadUi('main.ui', self)
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffees")
        rows = cursor.fetchall()
        for row in rows:
            id_, name, roast_degree, ground_beans, taste_description, price, package_volume = row
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            print(self.tableWidget.rowCount())
            self.tableWidget.setColumnCount(len(row))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(name))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QTableWidgetItem(roast_degree))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem(ground_beans))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 4, QTableWidgetItem(taste_description))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 5, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 6, QTableWidgetItem(package_volume))

        cursor.close()
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())