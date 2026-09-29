#Define a class named Employee with attributes empid,name,age,place,salary,designation and methods
#getsalary() and shoepersondetails().Create an employee object and call the methods

# class Employee:
#     def __init__(self):
#         self.empid=int(input("Enter the id:"))
#         self.name=input("Enter the name:")
#         self.age=input("Enter the age:")
#         self.place=input("Enter the place:")
#         self.salary=int(input("Enter the salary:"))
#         self.designation=input("Enter the designation:")
#
#     def getSalary(self):
#         print("The salary is",self.salary)
#
#     def showpersonDetails(self):
#         print("Name:",self.name,"\nAge:",self.age,"\nplace:",self.place)
#
# p1=Employee()
# p1.getSalary()
# p1.showpersonDetails()


#Define a class named Student with attributes rollno,name,mark1,mark2,mark3 and methods
#display() to display roll no and total mark of student.Create 2 student object and call the methods


# class Student:
#     def __init__(self):
#         self.rollno=int(input("Enter the Rollno:"))
#         self.name=input("Enter the name:")
#         self.mark1=int(input("Enter the first mark:"))
#         self.mark2=int(input("Enter the second mark:"))
#         self.mark3=int(input("Enter the third mark:"))
#
#     def display(self):
#         total=self.mark1+self.mark2+self.mark3
#         print("Roll no :",self.rollno,"Total marks:",total)
#
# s1=Student()
# s1.display()
# s2=Student()
# s2.display()


#Define a class named Book with attributes title,author,price,pages,languages and methods
#gettitle(),getauthor(),getPrice(),settitle(),setauthor(),setPrice().Create a Book object and call the methods

# class Book:
#     def __init__(self):
#         self.title=input("Enter the title:")
#         self.author=input("Enter the author name:")
#         self.price=int(input("Enter the price:"))
#         self.pages=int(input("Enter the pages:"))
#         self.languages=input("Enter the language:")
#
#     def getTitle(self):
#         print("Title:",self.title)
#
#     def getAuthor(self):
#         print("Author:",self.author)
#
#     def getPrice(self):
#         print("Price:",self.price)
#
#     def setTitle(self):
#         self.title=input("Enter the new title:")
#         print("New Title:",self.title)
#
#     def setAuthor(self):
#         self.author = input("Enter the new author:")
#         print("New Author:", self.author)
#
#     def setPrice(self):
#         self.price= input("Enter the new price:")
#         print("New price:", self.price)
#
# b=Book()
# b.getTitle()
# b.getAuthor()
# b.getPrice()
# b.setTitle()
# b.setAuthor()
# b.setPrice()


class Book:
    def __init__(self):
        self.title=input("Enter the title:")
        self.author=input("Enter the author name:")
        self.price=int(input("Enter the price:"))
        self.pages=int(input("Enter the pages:"))
        self.languages=input("Enter the language:")

    def getTitle(self):
        print("Title:",self.title)

    def getAuthor(self):
        print("Author:",self.author)

    def getPrice(self):
        print("Price:",self.price)

    def setTitle(self):
        self.title=input("Enter the new title:")
        self.getTitle()

    def setAuthor(self):
        self.author = input("Enter the new author:")
        self.getAuthor()

    def setPrice(self):
        self.price= input("Enter the new price:")
        self.getPrice()

b=Book()
b.setTitle()
b.setAuthor()
b.setPrice()