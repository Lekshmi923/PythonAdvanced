# f=open('k.txt','a')
# new="python"
# f.write(new)

#write a program to write content from one file to another file

f1=open('k.txt','r')
content=f1.read()
f2=open('p.txt','a')
f2.write('\n'+content)
f1.close()
f2.close()