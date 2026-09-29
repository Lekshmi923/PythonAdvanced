#Write a menu-driven Python program using a class Student
#to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.

class Student:
    def __init__(self):
        self.rollno=int(input("Enter the Roll number: "))
        self.name=input("Enter the name: ")
        self.marks=int(input("Enter the mark: "))

    def update(self):
        self.marks=int(input("Enter the new mark: "))

    def display(self):
        print(self.rollno,self.name,self.marks)



l=[]
while(True):
    print("1.Add a new student")
    print("2.Update mark")
    print("3.Display all students")
    print("4.Search a student by Roll NO")
    print("5.Delete a Student")
    print("6.Exit")

    ch=int(input("Enter the option: "))
    if ch==1:
        s=Student()
        l.append(s)
        print(s)

    elif ch==2:
        rollnum=int(input("Enter the roll number: "))
        for i in l:
            if (i.rollno==rollnum):
                i.update()
                break
        else:
            print("Student does not exist")

    elif ch==3:
        for i in l:
            i.display()


    elif ch==4:
        rollnum=int(input("Enter the roll number :"))
        for i in l:
            if (i.rollno==rollnum):
                print("Student found")
                print(i.rollno,i.name,i.marks)
                break
        else:
            print("Student not found")

    elif ch==5:
        rollnum=int(input("Enter the roll number: "))
        for i in l:
            if (i.rollno==rollnum):
                l.remove(i)

    else:
        exit()