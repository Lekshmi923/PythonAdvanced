class Company:
    def __init__(self):
        self.company_name=input("Enter the company name: ")
        self.location=input("Enter the location: ")

    def display_company(self):
        print(self.company_name,self.location)

class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid=int(input("Enter the employee id: "))
        self.name=input("Enter the name: ")
        self.designation=input("Enter the designation: ")
        self.salary=int(input("Enter the salary: "))

    def display_details(self):
            super().display_company()
            print(self.empid,self.name,self.designation,self.salary)

    def update_salary(self):
        self.salary=self.salary*1.1
        print("Salary after increment is",int(self.salary))

e=Employee()
e.display_details()
e.update_salary()

