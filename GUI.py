import sys
import mysql.connector
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QLabel, QPushButton, QAction, QLineEdit, QMessageBox
from Login import *

"""Single Global Connection to the SQL Server"""

mydb = mysql.connector.connect(
    host='localhost',
    user='CONNECTOR',
    password='password',
    database='HospitalRecords',
    unix_socket='/tmp/mysql.sock'
)
cursor = mydb.cursor()

"""
This is the class that stores the users information, mainly used for permissions
"""


class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.title = 'Access'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QPushButton('Doctor/Nurse', self)
        self.button.move(100,50)
        self.button.resize(200, 50)

        self.button = QPushButton('Patient', self)
        self.button.move(100,120)
        self.button.resize(200, 50)

        self.button = QPushButton('Admin', self)
        self.button.move(100,190)
        self.button.resize(200, 50)

        self.button = QPushButton('Other', self)
        self.button.move(100,260)
        self.button.resize(200, 50)



class WindowTwo(QtWidgets.QWidget):

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)


class Login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.title = 'Login Window'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        attempts = 0
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('Username', self)
        label.move(20,20)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 50)
        self.textbox.resize(280,40)

        label = QLabel('Password', self)
        label.move(20,120)

        self.textbox1 = QLineEdit(self)
        self.textbox1.setEchoMode(QLineEdit.Password)
        self.textbox1.move(20, 150)
        self.textbox1.resize(280,40)

        self.button = QPushButton('Login', self)
        self.button.move(20,200)
        self.button.resize(140, 30)


        self.button.clicked.connect(self.on_click, attempts)
        self.show()



    def on_click(self, attempts):
        patientTable = ('Gender','First_Name','Surname','DOB','Height','Weight',
                     'Blood_Type','Phone_Number','State','City','Zipcode',
                     'Address','Email','username','password')
        print(attempts)
        attempts += 1
        attemptsLeft = 3 - attempts
        userInput = self.textbox.text()
        passInput = self.textbox1.text()
        print(userInput + ", " + passInput)
        username = patientTable[13]
        password = patientTable[14]
        res = tryLogin(userInput, passInput)
        print(res)

        if res == -1:
            print("Incorrect Username/Password")
            QMessageBox.question(self, 'Welcome',"ERROR: Incorrect Username/Password. " +
            "Please contact your system administrator if you believe this is a mistake", QMessageBox.Ok, QMessageBox.Ok)
            self.textbox1.setText("")

        else:
            QMessageBox.question(self, 'Welcome', 'Welcome, ' + res[1] + ' '
            + res[2]+ '!', QMessageBox.Ok, QMessageBox.Ok)
            self.textbox1.setText("")
            self.switch_window.emit()
            pass


        """if username == userInput:
            if (password != passInput):
                print("Password is incorrect!")
                print(attemptsLeft)
                QMessageBox.question(self, 'Incorrect Password', 'aTtEmPtS LeFt WoNt WoRk' ,QMessageBox.Ok, QMessageBox.Ok)
                self.textbox1.setText("")

            else:
                QMessageBox.question(self, 'Welcome', 'Welcome, ' + username + '!', QMessageBox.Ok, QMessageBox.Ok)
                self.textbox1.setText("")
                print("oof")
                self.switch_window.emit()
                print("after oof")
        else:
            print('Username does not exist')"""


class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()

    def show_window_two(self, text):
        self.window_two = WindowTwo(text)
        self.window.close()
        self.window_two.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
