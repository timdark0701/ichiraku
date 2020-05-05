from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import sqlite3
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QPushButton )
from functools import partial


conn = sqlite3.connect('db.sqlite3')
curs = conn.cursor()
curs.execute('CREATE TABLE IF NOT EXISTS feedback_feedback (name TEXT,email TEXT, phone TEXT , description TEXT)')

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(494, 348)
        self.Add = QtWidgets.QDialogButtonBox(Dialog)
        self.Add.setGeometry(QtCore.QRect(100, 290, 341, 32))
        self.Add.setOrientation(QtCore.Qt.Horizontal)
        self.Add.setObjectName("Add")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 391, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 190, 391, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 80, 391, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 140, 391, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 25, 55, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 55, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 55, 21))
        self.label_5.setObjectName("label_5")
        self.Add_button = QtWidgets.QPushButton(Dialog)
        self.Add_button.setGeometry(QtCore.QRect(380, 290, 93, 28))
        self.Add_button.setObjectName("Add_button")

        self.Add_button.clicked.connect(self.Add_data)

        ##clear button
        #self.Clear_button = QtWidgets.QPushButton(Dialog)
        #self.Clear_button.setGeometry(QtCore.QRect(300, 290, 93, 28))
        #self.Clear_button.setObjectName("Clear_button")

        #self.Clear_button.clicked.connect(self.clear)

        self.retranslateUi(Dialog)
        self.Add.accepted.connect(Dialog.accept)
        self.Add.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def load_Data(self):
        connection = sqlite3.connect('db.sqlite3')
        query = "SELECT * FROM feedback_feedback"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        return

        self.tableWidget.setHorizontalHeaderLabels(
            ('ID', 'NAME', 'EM@IL', 'Phone', 'Description')
        )


    def Add_data(self):
        name = self.lineEdit.text()
        phone = self.lineEdit_3.text()
        commentary = self.lineEdit_4.text()
        email = self.lineEdit_2.text()
        try:
            curs.execute('INSERT into feedback_feedback (name,email,phone,description)VALUES(?,?,?,?)',(name,phone,commentary,email))
            conn.commit()
            print('DONE')
            self.load_Data()
        except Exception as error :
            print(error)

    #def clear(self):
        #self.tableWidget.clear()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_2.setText(_translate("Dialog", "Phone"))
        self.label_3.setText(_translate("Dialog", "Commentary"))
        self.label_5.setText(_translate("Dialog", "Email:"))
        self.Add_button.setText(_translate("Dialog", "Add"))
        #self.Clear_button.setText(_translate("Dialog", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
