#Static input

# class Person:
#     def __init__(self,n,a): #__init__ used to create and in initialize object attributes or properties
#         self.name=n
#         self.age=a
#
#     def show(self):     #self represents current object
#         print(self.name,self.age)
#
# p1=Person('Athul',25) #creates object of class Person
# p1.show()                   #it will call __init__ automatically
# p2=Person("sadie",23)
# p2.show()

#Dynamic input

class Person:
    def __init__(self): #__init__ used to create and in initialize object attributes or properties
        self.name=input("Enter the name: ")
        self.age=input("Enter the age: ")

    def show(self):     #self represents current object
        print(self.name,self.age)

p1=Person() #creates object of class Person
p1.show()            #it will call __init__ automatically
p2=Person()
p2.show()