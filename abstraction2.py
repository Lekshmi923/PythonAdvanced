# create an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.

from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self):
        self.name=input("Enter the name:")
        self.empid=int(input("Enter the id:"))
        self.age=int(input("Enter the age:"))
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.salary=int(input("Enter the monthly salary:"))

    def calculate_salary(self):
        print("Salary:",self.salary)

f=FullTimeEmployee()
f.calculate_salary()


class PartTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.salary = int(input("Enter the salary per hour:"))
        self.hour=int(input("Enter the hours:"))

    def calculate_salary(self):
        print("Salary:", self.salary*self.hour)


p=PartTimeEmployee()
p.calculate_salary()