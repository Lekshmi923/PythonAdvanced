try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    r=num1/num2
    print("result:",r)

except ZeroDivisionError :
    print("Zero Division Error")

except ValueError:
    print("Value Error")

except:
    print("Error")

