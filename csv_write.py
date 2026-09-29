import csv
f=open('data.csv','w',newline="")
content=[['name','age','place'],['achu',25,'london'],['carol',26,'las vegas']]
w=csv.writer(f)
print(w)
w.writerows(content)
f.close()
