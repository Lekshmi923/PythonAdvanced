#1.Create a class named Circle with an attribute radius.
# Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
# Create an object of the Circle class and call both methods to display the results.

class Circle:
    def __init__(self):
        self.radius=int(input("Enter the radius: "))

    def getArea(self):
        area=3.14*self.radius*self.radius
        print("Area of the circle is",area)

    def getPerimeter(self):
        perimeter=2*3.14*self.radius
        print("Perimeter of the circle is",perimeter)
r=Circle()
r.getArea()
r.getPerimeter()

# 2.Create a class named Account with attributes acctnumber, acctname, and balance.
# Initialize these values using a constructor by taking input from the user. Define the following methods:
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.

class Account:
    def __init__(self):
        self.acctnumber=int(input("Enter the Account number: "))
        self.acctname=input("Enter the Account name: ")
        self.balance=int(input("Enter the balance: "))

    def withdraw(self):
        w_amount=int(input("Enter the withdraw amount: "))
        if (w_amount>self.balance):
            print("Insuffient Balance")
        else:
            self.balance=self.balance-w_amount
            self.showbalance()

    def deposit(self):
        d_amount=int(input("Enter the deposit amount: "))
        self.balance=self.balance+d_amount
        self.showbalance()

    def  showbalance(self):
        print("The current balance is",self.balance)

a1=Account()
a.withdraw()
a.deposit()
a.showbalance()

a2=Account()
a3=Account()

l=[a1,a2,a3]
# for i in l:                                    #for all objects
#     print(i.acctnumber,i.acctname,i.balance)
#     i.showbalance()

for i in l:
    if (i.acctnumber==123):
        i.showbalance()
