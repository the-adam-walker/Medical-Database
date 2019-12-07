import sys
import mysql.connector
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QLabel,QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget
from Login import *
import qdarkstyle
import os
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

Actor = None

class DoctorWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.title = 'Doctor/Nurse Access'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        center  = (QDesktopWidget().availableGeometry().center())
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button = QPushButton('Doctor/Nurse', self)
        self.button.move(center.x()-140,0.8*center.y() - 20-50)
        self.button.resize(200, 50)
        self.showMaximized()
        self.button.clicked.connect(self.on_click)
        self.show()


    def on_click(self):
        createPatientProfile(Actor, 'male', 'Test', 'McTest', '1/1/1111', '', Weight, BloodType, Phone_Number,
                             State, City, Zip, Address, Email, Username, Password)
        self.switch_window.emit()
pass

class DoctorWindow2(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.title = 'Doctor/Nurse Access'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        center  = (QDesktopWidget().availableGeometry().center())
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel('Patient Lookup', self)
        label.move(center.x() - 52 , 0.8*center.y()-300)

        self.textbox = QLineEdit(self)
        self.textbox.resize(280,40)
        self.textbox.move(center.x() - 350, 0.8*center.y() - 240)
        self.textbox1 = QLineEdit(self)
        self.textbox1.resize(280,40)
        self.textbox1.move(center.x() + 70, 0.8*center.y() - 240)
        self.button = QPushButton('Search', self)
        self.button.move(center.x() -105, 0.8*center.y() - 180)
        self.button.resize(200, 50)
        self.showMaximized()
        self.button.clicked.connect(self.on_click)
        self.show()


    def on_click(self):
        center  = (QDesktopWidget().availableGeometry().center())
        firstName = self.textbox.text()
        lastName = self.textbox1.text()
        data = getPatientData(Actor, firstName, lastName)
        self.switch_window.emit(data)
pass

class AdminWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()
    switch_window1 = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.title = 'Admin Access'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        center  = (QDesktopWidget().availableGeometry().center())
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button = QPushButton('Patient Lookup', self)
        self.button.move(center.x()-140,0.8*center.y() - 20-50)
        self.button.resize(200, 50)
        self.button1 = QPushButton('Add Patient', self)
        self.button1.move(center.x()-140,0.8*center.y() + 70)
        self.button1.resize(200, 50)
        self.showMaximized()
        self.button.clicked.connect(self.on_click)
        self.button1.clicked.connect(self.on_click1)
        self.show()


    def on_click(self):
         self.switch_window.emit()

    def on_click1(self):
         self.switch_window1.emit()
pass

class AdminWindow2(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.title = 'Admin Access 2'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        center  = (QDesktopWidget().availableGeometry().center())
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel('Patient Lookup', self)
        label.move(center.x() - 52 , 0.8*center.y()-300)

        self.textbox = QLineEdit(self)
        self.textbox.resize(280,40)
        self.textbox.move(center.x() - 350, 0.8*center.y() - 240)
        self.textbox1 = QLineEdit(self)
        self.textbox1.resize(280,40)
        self.textbox1.move(center.x() + 70, 0.8*center.y() - 240)
        self.button = QPushButton('Search', self)
        self.button.move(center.x() -105, 0.8*center.y() - 180)
        self.button.resize(200, 50)
        self.showMaximized()
        self.button.clicked.connect(self.on_click)
        self.show()


    def on_click(self):
        center  = (QDesktopWidget().availableGeometry().center())
        firstName = self.textbox.text()
        lastName = self.textbox1.text()
        data = getPatientData(Actor, firstName, lastName)
        if data == -1:
            print("error")
        print(data)
        self.switch_window.emit(data)

    pass

class PatientWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.title = 'Patient Access'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        center  = (QDesktopWidget().availableGeometry().center())
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button = QPushButton('Patient Info', self)
        self.button.move(center.x()-140,0.8*center.y() - 20-50)
        self.button.resize(200, 50)
        self.showMaximized()
        self.button.clicked.connect(self.on_click)
        self.show()



    def on_click(self):
        data = getPatientData(Actor, globals()["Actor"].Name, (globals()["Actor"].Surname))
        self.switch_window.emit(data)

pass

'''
class PatientWindow2(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str, str, list)

    def __init__(self):
        super().__init__()
        self.title = 'Patient Access'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        center  = (QDesktopWidget().availableGeometry().center())
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel('Patient Lookup', self)
        label.move(center.x() - 52 , 0.8*center.y()-300)

        self.textbox = QLineEdit(self)
        self.textbox.resize(280,40)
        self.textbox.move(center.x() - 350, 0.8*center.y() - 240)
        self.textbox1 = QLineEdit(self)
        self.textbox1.resize(280,40)
        self.textbox1.move(center.x() + 70, 0.8*center.y() - 240)
        self.button = QPushButton('Search', self)
        self.button.move(center.x() -105, 0.8*center.y() - 180)
        self.button.resize(200, 50)
        self.showMaximized()
        self.button.clicked.connect(self.on_click)
        self.show()


    def on_click(self):
        center  = (QDesktopWidget().availableGeometry().center())
        firstName = self.textbox.text()
        lastName = self.textbox1.text()
        data = getPatientData(Actor, firstName, lastName)
        self.switch_window.emit(firstName, lastName, data)
pass
'''

class OtherWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.title = 'Low Access'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        center  = (QDesktopWidget().availableGeometry().center())
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QPushButton(Actor.Permissions, self)
        self.button.move(center.x()-140,0.8*center.y() - 20-50)
        self.button.resize(200, 50)
        self.showMaximized()
        self.button.clicked.connect(self.on_click)
        self.show()


    def on_click(self):
         self.switch_window.emit()
pass

'''This Function creates a window that displays the PatientInfo for Admins'''

class PatientInfo(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, data):
        super().__init__()
        self.title = "Patient Info: " + str(data[0][1]) + " " + str(data[0][2])
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI(data)

    def initUI(self, data):
        center  = (QDesktopWidget().availableGeometry().center())
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('Name: ' + data[0][1] + " " + data[0][2] , self)
        label.move(center.x() - 70,0.8*center.y()-200)
        label = QLabel('Gender: ' + data[0][0] , self)
        label.move(center.x() - 70,0.8*center.y()-150)
        label = QLabel('DOB: ' + data[0][3] , self)
        label.move(center.x() - 70,0.8*center.y()-100)
        label = QLabel('Height: ' + data[0][4] , self)
        label.move(center.x() - 70,0.8*center.y()-50)
        label = QLabel('Weight: ' + data[0][5] , self)
        label.move(center.x() - 70,0.8*center.y()-0)
        label = QLabel('BloodType: ' + data[0][6] , self)
        label.move(center.x() - 70,0.8*center.y()+50)
        label = QLabel('Phone Number: ' + data[0][7] , self)
        label.move(center.x() - 70,0.8*center.y()+100)
        label = QLabel('State: ' + data[0][8] , self)
        label.move(center.x() - 70,0.8*center.y()+150)
        label = QLabel('City: ' + data[0][9] , self)
        label.move(center.x() - 70,0.8*center.y()+200)
        label = QLabel('Zipcode: ' + data[0][10] , self)
        label.move(center.x() - 70,0.8*center.y()+250)
        label = QLabel('Address: ' + data[0][11] , self)
        label.move(center.x() - 70,0.8*center.y()+300)
        label = QLabel('Email: ' + data[0][12] , self)
        label.move(center.x() - 70,0.8*center.y()+350)
        label = QLabel('username: ' + data[0][13] , self)
        label.move(center.x() - 70,0.8*center.y()+400)
        label = QLabel('password: ' + data[0][14] , self)
        label.move(center.x() - 70,0.8*center.y()+450)

        self.showMaximized()
        self.show()

class AddPatient(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.title = 'Add Patient'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        center  = (QDesktopWidget().availableGeometry().center())
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel("Insert Patient's Info: ", self)
        label.move(center.x()-35,center.y()-400)

        label = QLabel('First Name: ', self)
        label.move(center.x() - 400,center.y()-350)
        self.textbox = QLineEdit(self)
        self.textbox.resize(280,40)
        self.textbox.move(center.x()-300,center.y() - 350)

        label = QLabel('Last Name: ', self)
        label.move(center.x() + 100,center.y()-350)
        self.textbox1 = QLineEdit(self)
        self.textbox1.resize(280,40)
        self.textbox1.move(center.x() + 200,center.y() - 350)

        label = QLabel('Gender: ', self)
        label.move(center.x() - 400,center.y()-250)
        self.textbox2 = QLineEdit(self)
        self.textbox2.resize(280,40)
        self.textbox2.move(center.x() -300,center.y() - 250)

        label = QLabel('DOB: ', self)
        label.move(center.x() + 100,center.y()-250)
        self.textbox3 = QLineEdit(self)
        self.textbox3.resize(280,40)
        self.textbox3.move(center.x() + 200,center.y() - 250)

        label = QLabel('Height: ', self)
        label.move(center.x() - 400,center.y()-150)
        self.textbox4 = QLineEdit(self)
        self.textbox4.resize(280,40)
        self.textbox4.move(center.x() -300,center.y() - 150)

        label = QLabel('Weight: ', self)
        label.move(center.x() + 100,center.y()-150)
        self.textbox5 = QLineEdit(self)
        self.textbox5.resize(280,40)
        self.textbox5.move(center.x() + 200,center.y() - 150)

        label = QLabel('Blood Type: ', self)
        label.move(center.x() - 400,center.y()-50)
        self.textbox6 = QLineEdit(self)
        self.textbox6.resize(280,40)
        self.textbox6.move(center.x() -300,center.y() - 50)

        label = QLabel('Phone Number: ', self)
        label.move(center.x() + 100,center.y()-50)
        self.textbox7 = QLineEdit(self)
        self.textbox7.resize(280,40)
        self.textbox7.move(center.x() + 200,center.y() - 50)

        label = QLabel('State: ', self)
        label.move(center.x() - 400,center.y()+ 50)
        self.textbox8 = QLineEdit(self)
        self.textbox8.resize(280,40)
        self.textbox8.move(center.x() -300,center.y() + 50)

        label = QLabel('City: ', self)
        label.move(center.x() + 100,center.y()+50)
        self.textbox9 = QLineEdit(self)
        self.textbox9.resize(280,40)
        self.textbox9.move(center.x() + 200,center.y() +50)

        label = QLabel('ZipCode: ', self)
        label.move(center.x() - 400,center.y()+150)
        self.textbox10 = QLineEdit(self)
        self.textbox10.resize(280,40)
        self.textbox10.move(center.x() -300,center.y() +150)

        label = QLabel('Address: ', self)
        label.move(center.x() + 100,center.y()+150)
        self.textbox11 = QLineEdit(self)
        self.textbox11.resize(280,40)
        self.textbox11.move(center.x() + 200,center.y() +150)

        label = QLabel('Email: ', self)
        label.move(center.x() - 400,center.y()+250)
        self.textbox12 = QLineEdit(self)
        self.textbox12.resize(280,40)
        self.textbox12.move(center.x() -300,center.y() +250)

        label = QLabel('Username: ', self)
        label.move(center.x() + 100,center.y()+250)
        self.textbox13 = QLineEdit(self)
        self.textbox13.resize(280,40)
        self.textbox13.move(center.x() + 200,center.y() +250)

        label = QLabel('Password: ', self)
        label.move(center.x() - 400,center.y()+350)
        self.textbox14 = QLineEdit(self)
        self.textbox14.resize(280,40)
        self.textbox14.move(center.x() -300,center.y() + 350)

        self.button = QPushButton('Add Patient', self)
        self.button.move(center.x() + 100,center.y() + 350)
        self.button.resize(200, 50)

        self.button1 = QPushButton('Back', self)
        self.button1.move(center.x() + 500,center.y() + 400)
        self.button1.resize(200, 50)

        self.showMaximized()
        self.button.clicked.connect(self.on_click)
        self.button1.clicked.connect(self.on_click1)
        self.show()

    def on_click(self):
        firstName = self.textbox.text()
        lastName = self.textbox1.text()
        gender = self.textbox2.text()
        DOB = self.textbox3.text()
        height = self.textbox4.text()
        weight = self.textbox5.text()
        bloodType = self.textbox6.text()
        phoneNumber = self.textbox7.text()
        state = self.textbox8.text()
        city = self.textbox9.text()
        zipCode = self.textbox10.text()
        address = self.textbox11.text()
        email = self.textbox12.text()
        username = self.textbox13.text()
        password = self.textbox14.text()
        createPatientProfile(Actor, gender, firstName, lastName, DOB, height, weight, bloodType, phoneNumber,
                             state, city, zipCode, address, email, username, password)
        print("Patient Added")
        QMessageBox.information(self, 'Sucess!', 'Patient Added!', QMessageBox.Ok, QMessageBox.Ok)

    def on_click1(self):
        self.switch_window.emit()

pass

class WindowTwo(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel()
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
        self.width = 288
        self.height = 180
        self.attempts = 0
        self.initUI()


    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('Username', self)
        center  = (QDesktopWidget().availableGeometry().center())
        label.move(center.x()-140,0.8*center.y()-50-50)

        self.textbox = QLineEdit(self)
        self.textbox.resize(280,40)
        self.textbox.move(center.x()-140,0.8*center.y() - 20-50)

        label = QLabel('Password', self)
        label.move(center.x()-140,center.y()-50-50)

        self.textbox1 = QLineEdit(self)
        self.textbox1.setEchoMode(QLineEdit.Password)
        self.textbox1.resize(280,40)
        self.textbox1.move(center.x()-140,center.y() - 20-50)

        self.button = QPushButton('Login', self)
        self.button.resize(140, 30)
        self.button.move(center.x()-70,center.y() + 40-50)


        self.showMaximized()
        self.button.clicked.connect(self.on_click)
        self.show()

    def keyPressEvent(self, event):
            if event.key() == QtCore.Qt.Key_Return:
                self.on_click()

    def on_click(self):

        userInput = self.textbox.text()
        passInput = self.textbox1.text()
        print(userInput + ", " + passInput)
        res = tryLogin(userInput, passInput)
        print(res)

        if res == -1:
            print("Incorrect Username/Password")
            QMessageBox.critical(self, 'Welcome',"ERROR: Incorrect Username/Password. " +
            "Please contact your system administrator if you believe this is a mistake", QMessageBox.Ok, QMessageBox.Ok)
            self.textbox1.setText("")

        else:
            globals()["Actor"] = ActorC(res[1], res[2], res[3], res[0])
            QMessageBox.information(self, 'Welcome', 'Welcome, ' + res[1] + ' '
            + res[2]+ '!', QMessageBox.Ok, QMessageBox.Ok)
            self.textbox1.setText("")
            self.switch_window.emit()
            pass



class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()

        self.login.switch_window.connect(self.switchScreen)
        self.login.show()

    def switchScreen(self):
        print(Actor)

        if Actor.Permissions == "Doctor" or Actor.Permissions == "Nurse":
            self.show_doctor()
        elif Actor.Permissions == "Admin":
            self.show_admin()
        elif Actor.Permissions == "Patient":
            self.show_patient()
        else:
            self.show_other()
            pass

    def show_doctor(self):
        self.window = DoctorWindow()
        self.window.switch_window.connect(self.show_doctor2)
        self.login.close()
        self.window.show()

    def show_doctor2(self):
        self.window = DoctorWindow2()
        self.window.switch_window.connect(self.show_patientInfo)
        self.login.close()
        self.window.show()

    def show_admin(self):
        self.window = AdminWindow()
        self.window.switch_window.connect(self.show_admin2)
        self.window.switch_window1.connect(self.show_addPatient)
        self.login.close()
        self.window.show()

    def show_admin2(self):
        self.window = AdminWindow2()
        self.window.switch_window.connect(self.show_patientInfo)
        self.login.close()
        self.window.show()

    def show_patient(self):
        self.window = PatientWindow()
        self.window.switch_window.connect(self.show_patientInfo)
        self.login.close()
        self.window.show()

    def show_patient2(self):
        self.window = PatientWindow2()
        self.window.switch_window.connect(self.show_patientInfo)
        self.login.close()
        self.window.show()

    def show_other(self):
        self.window = OtherWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()

    def show_patientInfo(self, data):
        self.window = PatientInfo(data)
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()

    def show_window_two(self):
        self.window_two = WindowTwo()
        self.window.close()
        self.window_two.show()

    def show_addPatient(self):
        self.window = AddPatient()
        self.window.close()
        self.window.switch_window.connect(self.show_admin)
        self.window.show()




def main():
    sys._excepthook = sys.excepthook
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)
    sys.excepthook = exception_hook
    app = QtWidgets.QApplication(sys.argv)
    os.environ['PYQTGRAPH_QT_LIB']="PyQt5"
    os.environ['QT_API']="pyqt5"
    app.setStyleSheet(qdarkstyle.load_stylesheet_from_environment())
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
