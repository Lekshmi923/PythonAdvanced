# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

import math
while(True):
    try:
        num=int(input("Enter a number:"))
        fact=math.factorial(num)
        print("Factorial:",fact)
    except ValueError:
        print("Value Error")
    else:
        exit()



# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.


# while (True):
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.Multiplication")
#     print("4.Division")
#     print("5.Exit")
#     try:
#         ch=int(input("Enter the choice:"))
#         if ch in [1,2,3,4]:
#             n1 = int(input("Enter the first number:"))
#             n2 = int(input("Enter the second number:"))
#             r = n1 - n2
#             r = n1 + n2
#             r = n1 * n2
#             r = n1 / n2
#
#     except ValueError:
#         print("Invalid input")
#
#     except ZeroDivisionError:
#         print("Zero Division Error")
#
#     except:
#         print("Error")
#
#     else:
#         if ch==1:
#             print("sum",r)
#         elif ch==2:
#             print("subtraction:",r)
#         elif ch==3:
#             print("Multiplication",r)
#         elif ch==4:
#             print("Division",r)
#         else:
#             exit()





# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist

try:
    filename=input("Enter the filename: ")
    f=open(filename,"r")
    print(f.read())
except FileNotFoundError:
    print("File does not exist")



#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

try:
    d={"name":"arun","age":23,"place":"ekm"}
    key=input("Enter the key:")
    print(d[key])
except KeyError:
    print("Key does not exist")








