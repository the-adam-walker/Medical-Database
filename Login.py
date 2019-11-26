import mysql.connector



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

class ActorC(object):
    """docstring for Actor"""
    def __init__(self, Name, Surname, Username, Permission):
        super(ActorC, self).__init__()
        self.Name = Name
        self.Surname = Surname
        self.Username = Username
        self.Permissions = Permission
        pass

"""
This function takes a username and password and attempts to log in to the database. It searches
the Patients and Staff Tables in the SQL server and if there is a matching username and password,
it returns [ROLE, FIRSTNAME, LASTNAME, USERNAME]
if there is no match, a -1 is returned
if there are multiple matches, a -2 is returned
"""

def tryLogin(logUsername, logPassword):

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



"""This function does not work yet but the intent is it takes the Actor, and patient info, and if the actor
has sufficeint permissions, an entry is added to the Patient table will the criteria specified.
"""

def createPatientProfile(Actor, Gender, First_Name, Surname, DOB, Height, Weight, BloodType, Phone_Number,
    State, City, Zip, Address, Email, Username, Password):
    if (Actor.Permissions != 'Admin'):
        return -1
    try:
        mydb.autocommit = False
        add_patient = ("INSERT INTO Patients (Gender, First_Name, Surname, DOB, Height, Weight, bloodtype, Phone_Number, State, City, Zipcode, Address, Email, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_patient = (Gender, First_Name, Surname, DOB, Height, Weight, BloodType, Phone_Number, State, City, Zip, Address, Email, Username, Password)
        cursor.execute(add_patient, data_patient)
        mydb.commit()
        mydb.autocommit = True
    except mysql.connector.Error as error:
        print(error)
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()

"""
This function takes a First and Last name and searches the patient table to find the username associated. It will
not check for patients with the same name, this can be added later if we want, there are 141 duplicate names listed
 in the patient database as of right now
"""

def getPatientUserName(First_Name, Last_Name):
    cursor.execute("SELECT First_Name, Surname, username from Patients where First_Name = \'"
        + First_Name + "\' and Surname = \'" + Last_Name + "\'")
    rows = cursor.fetchall()
    if len(rows) == 1:
        return rows[0][2]
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


"""
This function takes an Actor, and patient First_Name, and patient Last_name
If the actor has sufficient permissions (Dr, Nurse, or Patient with the same username)
then the function returns the row of that patient in the database
"""

def getPatientData(Actor, First_Name, Last_Name):

    PatientUser = getPatientUserName(First_Name, Last_Name);
    if ((Actor.Permissions == 'Nurse') or (Actor.Permissions == 'Doctor') or
        ((Actor.Permissions == 'Patient') and (Actor.Username == Patient))):
        read_patient = ("SELECT * from Patients where username = \'" + PatientUser + "\'")
        cursor.execute(read_patient)
        rows = cursor.fetchall()
        print(rows)
    else:
        return -1
        pass



def main():

    """
    Get username and password
    """

    print('Please Enter Username:')
    user = input()
    print('Please Enter Password:')
    passw = input()
    #Attempt to login
    res = tryLogin(user,passw)


    if res == -1:
        print("ERROR: Incorrect Username or Password")
    elif res == -2:
        print("ERROR: Duplicate Username Password Combination")
    else:
        #Login was successful, create Actor Object

        Actor = ActorC(res[1], res[2], res[3], res[0])
        print("User " + Actor.Name + ' ' + Actor.Surname)
        print("Permission Level:  " + Actor.Permissions)
        pass

    createPatientProfile(Actor, 'male','Virgil2','Futral2','9/16/1956','181','96.3','B+','619-216-8974','CA','Chula Vista','92010','4296 Holden Street','VirgilRFutral@armyspy.com','Abinimbed','iePhi7Ohr')
    #getPatientData(Actor, 'Daryl', 'Stokes')








if __name__ == '__main__':
    main()
