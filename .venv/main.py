import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from PyQt6.uic import loadUi
import sqlite3

### В задании конкретики я не нашел, поэтому сделал замену по имени.

class AddEditCoffeeForm(QMainWindow):
    def __init__(self, code):
        super().__init__()
        self.code = code
        loadUi('addCoffeeForm.ui', self)
        self.claim_button.clicked.connect(self.form)

    def form(self):
        name = self.name_edit.text()
        roast_degree = self.roast_edit.text()
        ground_beans = self.beans_edit.text()
        taste_description = self.taste_edit.text()
        price = self.price_edit.text()
        package_volume = self.volume_edit.text()
        if not all([name, roast_degree, ground_beans, taste_description, price, package_volume]):
            self.error_label.setText("Предупреждение! Пожалуйста, заполните все обязательные поля.")
            return
        conn = sqlite3.connect('coffee.sqlite')
        if self.code == 'a':
            cursor = conn.cursor()
            cursor.execute(
                    "INSERT INTO coffees (name, roast_degree, ground_beans, taste_description, price, package_volume)"
                    " VALUES (?, ?, ?, ?, ?, ?)",
                    (name, roast_degree, ground_beans, taste_description, price, package_volume)
                )
            conn.commit()
            self.back = MainWindow()
            self.back.show()
            self.close()
        elif self.code == 'e':
            cursor = conn.cursor()
            res = cursor.execute(
                "SELECT * FROM coffees WHERE name=?",
                (name,)
            ).fetchall()
            if len(res) == 0:
                self.error_label.setText('Кофе с таким именем не найден.')
            else:
                cursor.execute(
                    "UPDATE coffees SET roast_degree=?, ground_beans=?, taste_description=?, price=?, package_volume=? "
                    "WHERE name=?",
                    (roast_degree, ground_beans, taste_description, price, package_volume, name)
                )
                conn.commit()
                self.back = MainWindow()
                self.back.show()
                self.close()





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.pushButtonAdd.clicked.connect(self.add)
        self.pushButtonEdit.clicked.connect(self.edit)


    def add(self):
        self.form = AddEditCoffeeForm('a')
        self.form.show()
        self.close()

    def edit(self):
        self.edt = AddEditCoffeeForm('e')
        self.edt.show()
        self.close()


    def init_ui(self):
        loadUi('main.ui', self)
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffees")
        rows = cursor.fetchall()
        for row in rows:
            id_, name, roast_degree, ground_beans, taste_description, price, package_volume = row
            self.tableWidget.insertRow(self.tableWidget.rowCount())
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