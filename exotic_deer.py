from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QTimer, QTime
import sqlite3
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QPushButton, QInputDialog)
from functools import partial
from add import Ui_Dialog
import time



class message:
    def __init__(self):
        self.message = 'none'
        self.lst_message = 'none'
    def set_msg(self, owner, data):
        self.owner = owner
        self.message = data

data0 = message()

class Ui_MainWindow(QWidget):
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

    #def delete(self):
        #self.tableWidget.removeRow(self.tableWidget.currentRow())
    def delete(self):
        connection = sqlite3.connect('db.sqlite3')
        query = "SELECT * FROM feedback_feedback"
        result = connection.execute(query)
        for row in enumerate(result):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
                name = data[1]
                mail = data[2]
                telephone = data[3]
                opisanie = data[4]
                result = connection.execute("DELETE FROM feedback_feedback WHERE id=? AND name=? AND  email=? AND phone=? AND description=?", (id, name, mail, telephone, opisanie))
                connection.commit()
                self.load_Data()


    def calldelete(self):
        connection = sqlite3.connect('db.sqlite3')
        query = "SELECT * FROM feedback_feedback"
        result = connection.execute(query)
        for row in enumerate(result):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
                result = connection.execute("DELETE FROM feedback_feedback WHERE id=? ", (id,))
                connection.commit()
                self.load_Data()

    def open_add(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1131, 781))
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("bg_2.jpg"))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 150, 441, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        ##


        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10,540, 501, 251))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        def chat_window_update():
            if(data0.lst_message != data0.message):
                data0.lst_message = data0.message
                self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText()+'\n'+data0.owner[11:-1] +' '+data0.message)

        #Setting Timer
        timer  = QTimer(self)
        timer.timeout.connect(chat_window_update)
        timer.setInterval(1500)
        timer.start()

        thread = threading.Thread(target=chat_window_update, args=())
        thread.start()

        event_witharg = partial(self.on_click, self.pushButton_2)
        self.pushButton_2.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        ##
        event_witharg = partial(self.on_click, self.pushButton_4)
        self.pushButton_4.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        ##
        event_witharg = partial(self.on_click, self.pushButton_3)
        self.pushButton_3.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        ##
        event_witharg = partial(self.on_click, self.pushButton_5)
        self.pushButton_5.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        ##
        event_witharg = partial(self.on_click, self.pushButton_6)
        self.pushButton_6.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        ##
        event_witharg = partial(self.on_click, self.pushButton_7)
        self.pushButton_7.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        ##
        event_witharg = partial(self.on_click, self.pushButton_8)
        self.pushButton_8.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        ##
        event_witharg = partial(self.on_click, self.pushButton_9)
        self.pushButton_9.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        ##
        event_witharg = partial(self.on_click, self.pushButton_10)
        self.pushButton_10.clicked.connect(event_witharg)
        ##
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.LoadData = QtWidgets.QPushButton(self.centralwidget)
        self.LoadData.setGeometry(QtCore.QRect(820, 920, 93, 28))
        self.LoadData.setObjectName("LoadData")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(960, 920, 93, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        ##
        event_witharg = partial(self.on_click, self.pushButton_11)
        self.pushButton_11.clicked.connect(event_witharg)
        ##
        self.LoadData_2 = QtWidgets.QPushButton(self.centralwidget)
        self.LoadData_2.setGeometry(QtCore.QRect(660, 680, 93, 28))
        self.LoadData_2.setObjectName("LoadData_2")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(800, 680, 93, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(620, 20, 471, 711))
        self.tableWidget.setStyleSheet("\n"
"\n"
"")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(670, 670, 93, 28))
        self.pushButton_load.setObjectName("pushButton_load")

        self.pushButton_load.clicked.connect(self.load_Data)

        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(800, 670, 93, 28))
        self.pushButton_delete.setObjectName("pushButton_delete")

        self.pushButton_delete.clicked.connect(self.delete)

        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(930, 670, 93, 28))
        self.pushButton_add.setObjectName("pushButton_add")

        self.pushButton_add.clicked.connect(self.open_add)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(120, 20, 181, 41))
        self.textBrowser.setStyleSheet("background-color:silver;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    @pyqtSlot()
    def on_click(self, data):
        data.setText(self.tableWidget.model().index(0,1).data())
        self.delete()
        print(data)
        print('PyQt5 button click')






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Table5"))

        self.pushButton_4.setText(_translate("MainWindow", "Table2"))
        self.pushButton_3.setText(_translate("MainWindow", "Table6"))
        self.pushButton_5.setText(_translate("MainWindow", "Table4"))
        self.pushButton_6.setText(_translate("MainWindow", "Table1"))
        self.pushButton_7.setText(_translate("MainWindow", "Table3"))
        self.pushButton_8.setText(_translate("MainWindow", "Table7"))
        self.pushButton_9.setText(_translate("MainWindow", "Table8"))
        self.pushButton_10.setText(_translate("MainWindow", "Table9"))
        self.LoadData.setText(_translate("MainWindow", "Load Data"))
        self.pushButton_11.setText(_translate("MainWindow", "Delete "))
        self.LoadData_2.setText(_translate("MainWindow", "Load Data"))
        self.pushButton_12.setText(_translate("MainWindow", "Delete "))
        self.pushButton_load.setText(_translate("MainWindow", "Load Data"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_add.setText(_translate("MainWindow", "Add to DB"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">Exotic_Deer</span></p></body></html>"))

import socket, time
import threading

def socket_server():
    host = socket.gethostbyname(socket.gethostname())
    port = 9090
    clients = []
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('localhost',port))
    print("[ Server Started ]")
    quit = False

    while not quit:
        try:
            data, addr = s.recvfrom(1024)

            if addr not in clients:
                clients.append(addr)

            itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

            print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
            data = data.decode("utf-8")
            '''
            eto my obnavlaem message v classe
            sverhu
            '''
            data0.set_msg(addr[0], data)

            print(data)
            for client in clients:
                if addr != client:
                    s.sendto(data,client)
        except:
            print("\n[ Server ReStarted ]")
            #quit = True

    s.close()

if __name__ == "__main__":
    '''С помощью Threadov мы сделали 2 процесса 1 dlya qt, 2 dlya socket'''
    thread = threading.Thread(target=socket_server, args=())
    def run_qt():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    thread1 = threading.Thread(target = run_qt, args=())

    thread.start()
    thread1.start()
