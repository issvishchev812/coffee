# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(299, 140, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(299, 180, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(299, 260, 111, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(299, 220, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 340, 111, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(299, 300, 91, 20))
        self.label_7.setObjectName("label_7")
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(420, 140, 113, 21))
        self.name_edit.setObjectName("name_edit")
        self.roast_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.roast_edit.setGeometry(QtCore.QRect(420, 180, 113, 21))
        self.roast_edit.setObjectName("roast_edit")
        self.beans_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.beans_edit.setGeometry(QtCore.QRect(420, 220, 113, 21))
        self.beans_edit.setObjectName("beans_edit")
        self.taste_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.taste_edit.setGeometry(QtCore.QRect(420, 260, 113, 21))
        self.taste_edit.setObjectName("taste_edit")
        self.price_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.price_edit.setGeometry(QtCore.QRect(420, 300, 113, 21))
        self.price_edit.setObjectName("price_edit")
        self.volume_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.volume_edit.setGeometry(QtCore.QRect(420, 340, 113, 21))
        self.volume_edit.setObjectName("volume_edit")
        self.claim_button = QtWidgets.QPushButton(self.centralwidget)
        self.claim_button.setGeometry(QtCore.QRect(370, 400, 113, 32))
        self.claim_button.setObjectName("claim_button")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(200, 380, 431, 20))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "name"))
        self.label_2.setText(_translate("MainWindow", "roast_degree"))
        self.label_3.setText(_translate("MainWindow", "taste_description"))
        self.label_4.setText(_translate("MainWindow", "ground_beans"))
        self.label_6.setText(_translate("MainWindow", "package_volume"))
        self.label_7.setText(_translate("MainWindow", "price"))
        self.claim_button.setText(_translate("MainWindow", "Подтвердить"))
