CREATE TABLE Charts (
  `Gender` varchar(6) NOT NULL,
  `First_Name` varchar(20) NOT NULL,
  `Surname` varchar(23) NOT NULL,
  `DOB` varchar(10) NOT NULL,
  `Height` varchar(3) NOT NULL,
  `Weight` varchar(5) NOT NULL,
  `Blood_Type` varchar(5) NOT NULL,
  `Nurse` varchar(50) NOT NULL,
  `Nurse_Notes` varchar(1000) NOT NULL,
  `Diagnosis` varchar(1000) NOT NULL,
  `Treatment_Plan` varchar(1000) NOT NULL,
  `Treatment_History` varchar(1000) NOT NULL,
  `Medications` varchar(1000) NOT NULL,
  `Allergies` varchar(1000) NOT NULL,
  `General_Info` varchar(1000) NOT NULL
);



insert into Charts values('male','Virgil','Futral','9/16/1956','181','96.3','B+', 'Daisy Carothers','Patient is alive', 'Patient does not have arms', 'Find Patient Arms', 'Patient Previously Had Arms', 'Arm-Off', 'Morphine', 'Most Patients have Arms');
