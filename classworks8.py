# # # #write a program to read a text file and displays the number of lines in a file

# f=open('k.txt','r')
# lines=f.readlines()
# count=len(lines)
# print("The number of lines is",count)

# # # #write a program to display the number of words in a file

# f=open('k.txt','r')
# content=f.read()
# words=content.split()
# count=len(words)
# print("The number of words is",count)

# # #write a program to update the second line in a file

# f=open('k.txt','r')
# lines=f.readlines()
# print(lines)
# lines[1]="updated line\n"
# f.close()
# f=open('k.txt','w')
# f.writelines(lines)
# f.close()

# # #write a program to display the last 5 lines in a file

# f=open('k.txt','r')
# lines=f.readlines()
# print(lines)
# a=lines[-5:]
# print(a)
# f.close()

# #program to search a particular word in a file

# f=open('k.txt','r')
# content=f.read()
# words=content.split()
# w=input("Enter the word :")
# if w in words:
#     print("yes")
# else:
#     print("no")

# # #find the number of letters,digits,and spaces in a file

# f=open('k.txt','r')
# content=f.read()
# letters=0
# digits=0
# space=0
# for i in content:
#     if i.isalpha():
#         letters=letters+1
#     elif i.isdigit():
#         digits=digits+1
#     elif i.isspace():
#         space=space+1
#     else:
#         break
# print(f"letters:{letters},digits:{digits},space:{space}")

#reverse the lines in a file

# f=open('k.txt','r')
# lines=f.readlines()
# print(lines)
# rev=lines[::-1]
# f.close()
# f=open('k.txt','w')
# f.writelines(rev)
# f.close()
# print(rev)

# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.

# f1=open('totalstudents.txt','r')
# f2=open('passedstudents.txt','r')
# f3=open('failedstudents.txt','w')
#
# total=f1.readlines()
# passed=f2.readlines()
# failed=[]
# for i in total:
#     if i not in passed:
#         failed.append(i)
# f3.writelines(failed)
# print(total)
# print(passed)
# print(failed)
# f1.close()
# f2.close()
# f3.close()


f1=open('totalstudents.txt','r')
f2=open('passedstudents.txt','r')
f3=open('failedstudents.txt','w')

total=[i.strip() for i in f1.readlines()]
passed=[i.strip() for i in f2.readlines()]
failed=[]
for i in total:
    if i not in passed:
        failed.append(i+'\n')
f3.writelines(failed)
print(total)
print(passed)
print(failed)
f1.close()
f2.close()
f3.close()




