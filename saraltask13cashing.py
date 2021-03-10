import json
from pprint import pprint
data=open("saraltaskch4.json")
saral=json.load(data)
data2=open("saraltask12.json")
saral2=json.load(data2)
b=0
while b<(len(saral)):
    i=0
    while i<=b:
        if b==i:
            a=saral[b]
            a["Cast"]=saral2[i]
            print(a)
        i=i+1
    b=b+1
data=open("saraltask13.json","w")
saral=json.dumps(saral, indent=4)
data.write(saral)
    
        