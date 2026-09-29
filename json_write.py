#write

f=open('data.json','w')
import json

content=[{'name':'Achu','age':23,'course':'python'},{'name':'max','age':28,'course':'java'}]
json.dump(content,f)
f.close()