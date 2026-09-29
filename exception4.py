try:
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    r=n1/n2
    print(r)
except ValueError as e:
    print(e)
    print(type(e))

except ZeroDivisionError as e:
    print(e)
    print(type(e))

except Exception as e:
    print(e)
    print(type(e))

