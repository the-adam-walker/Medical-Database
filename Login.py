import mysql.connector

def tryLogin(logUsername, logPassword):
    try:
        mydb = mysql.connector.connect(
            host='prclab1.erau.edu',
            user='pietzd',
            password='plus4db',
            database='pietzd_db',
            unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT First_Name, Surname, username, password from Patients where username = \'" 
            + logUsername + "\' and password = \'" + logPassword + "\'")
        rows = cursor.fetchall()
        if len(rows) == 1:
            return ['Patient',rows[0][0], rows[0][1], rows[0][2],
            rows[0][3]]
        elif len(rows) > 1:
            return -2
            pass

        cursor.execute("SELECT * from Staff where username = \'" 
            + logUsername + "\' and password = \'" + logPassword + "\'")
        rows = cursor.fetchall()
        if len(rows) == 1:
            return [rows[0][2],rows[0][0], rows[0][1], rows[0][3]]
        elif len(rows) > 1:
            return -2
            pass
        return -1

    except mysql.connector.Error as error:
        print(error)
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()


def createPatientProfile(ActorPermissions, Gender, First_Name, Surname, DOB, Height, Weight, BloodType, Phone_Number, 
    State, City, Zip, Address, Email, Username, Password):
    if (ActorPermissions != 'Admin'):
        return -1
    try:
        mydb = mysql.connector.connect(
            host='prclab1.erau.edu',
            user='pietzd',
            password='plus4db',
            database='pietzd_db',
            unix_socket='/var/lib/mysql/mysql.sock'
        )
        cursor = mydb.cursor()
        add_patient = ("INSERT INTO Patients (Gender, First_Name, Surname, DOB, Height, Weight, Blood_Type, Phone_Number, State, City, Zipcode, Address, Email, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_patient = ('male','Virgil2','Futral2','9/16/1956','181','96.3','B+','619-216-8974','CA','Chula Vista','92010','4296 Holden Street','VirgilRFutral@armyspy.com','Abinimbed','iePhi7Ohr')
        cursor.execute(add_patient, data_patient)
        rows = cursor.fetchall()
        mydb.commit()
        print(rows)
    except mysql.connector.Error as error:
        print(error)
    finally:
        if mydb.is_connected():
            print('Dont')
            cursor.close()
            mydb.close()


def main():
    print('Please Enter Username:')
    user = raw_input()
    print('Please Enter Password:')
    passw = raw_input()

    res = tryLogin(user,passw)

    ActorPermissions = res[0]
    ActorFirstName = res[1]
    ActorSurname = res[2]
    ActorUsername = res[3]

    if res == -1:
        print("ERROR: Incorrect Username or Password")
    elif res == -2:
        print("ERROR: Duplicate Username Password Combination")
    else:
        #print("{} {} {}".format(res[0], res[1], res[2]))
        print("User " + ActorFirstName + ' ' + ActorSurname)
        print("Permission Level:  " + ActorPermissions)
        pass

    print("Attempting to Add Patient to Database: ")

    if (createPatientProfile(ActorPermissions,'female','Alexandria','Ocasio','7/27/1972','156','66.3','A+','508-234-2424','MA',
        'Boston','02199','200 Smith Street','AlexandiaBOcasio@superrito.com','Swers2001','Fah1xaehoh') == -1):
        print("I'm Sorry, \'" + ActorPermissions+"\' does not have sufficient privaliges to create Patient profiles. If you believe this to be an error, contact your System Administrator ")
    else:
        print('Sucesfully Added Patient \'Alexandria Ocasio\' to the Database')
        pass



if __name__ == '__main__':
    main()