def FileRead():
    filename=input("Enter the filename: ")
    f=open(filename,'r')
    content=f.read()
    print(content)
    f.close()

def FileWrite():
    filename=input("Enter the filename: ")
    f=open(filename,'w')
    content=input("Enter the content: ")
    f.write(content)
    f.close()

def FileAppend():
    filename=input("Enter the filename: ")
    f=open(filename,'a')
    content=input("Enter the content: ")
    f.write(content)
    f.close()

def FileSearch():
    filename = input("Enter the filename: ")
    word=input("Enter the word: ")
    f = open(filename, 'r')
    content=f.read()
    if word in content:
        print("Word exists")
    else:
        print("Word does not exist")
    f.close()

def FileDelete():
    filename=input("Enter the filename: ")
    import os
    os.remove(filename)





while(True):
    print("1.File Read")
    print("2.File Write")
    print("3.File Append")
    print("4.File Search")
    print("5.File Delete")
    print("6.Exit")

    ch=int(input("Enter the option: "))
    if ch == 1:
        FileRead()
    elif ch == 2:
        FileWrite()
    elif ch == 3:
        FileAppend()
    elif ch == 4:
        FileSearch()
    elif ch == 5:
        FileDelete()
    else:
        exit()





