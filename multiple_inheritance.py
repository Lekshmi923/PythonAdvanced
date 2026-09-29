class Hospital:
    def __init__(self):
        self.hos_name=input("Enter the hospital name:")
        self.location=input("Enter the location:")
        self.phone=int(input("Enter the phone number:"))

    def display_hospital(self):
        print("Hosptal name:",self.hos_name,"\nLocation:",self.location,"\nphone no:",self.phone)

class Department:
    def __init__(self):
        self.dept_name=input("Enter the department name:")
        self.doctor_name=input("Enter the name of doctor:")

    def display_department(self):
        print("Department name:",self.dept_name,"\nDoctor name:",self.doctor_name)

class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patient_name=input("Enter the name of patient:")
        self.age=int(input("Enter the age:"))
        self.gender=input("Enter the gender:")
        self.admission_date=input("Enter the admission date:")
        self.bedno=int(input("Enter the bed number:"))
        self.discharge_date=" "

    def set_discharge(self):
            self.discharge_date=input("Enter the discharge date:")

    def full_summary(self):
            Hospital.display_hospital(self)
            Department.display_department(self)
            print("Hosptal Details \nPatient:",self.patient_name,"\nAge:",self.age,"\nGender:",self.gender,"\nAdmission Date:",self.admission_date,"\nBed Number:",self.bedno)
            if(self.discharge_date==" "):
                print("Not yet discharged")
            else:
                print("Discharge Date:",self.discharge_date)
p=Patient()
p.full_summary()
p.set_discharge()
p.full_summary()
