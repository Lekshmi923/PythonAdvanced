class Person:
    def __init__(self):
        self.name=input("Enter the name: ")
        self.age=int(input("Enter the age: "))

    def show(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self):
        super().__init__()
        self.rollno=int(input("Enter the rollno: "))
        self.course=input("Enter the course: ")
        self.mark=int(input("Enter the mark: "))

    def show(self):
        super().show()
        print(self.rollno,self.course,self.mark)

    def updatemark(self):
        self.mark=int(input("Enter the new mark: "))
s=Student()
s.show()
s.updatemark()