f=open('data.json','r')
import json
content=json.load(f)
print(content)
print(content[0]['name'])
f.close()