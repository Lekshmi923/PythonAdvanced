try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    s=num1+num2
except:
    print("Invalid number")

#optional
else:
    print("sum:",s)

finally:
    print("process finished")