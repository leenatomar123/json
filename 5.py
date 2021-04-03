import json
dic={"4":5,"6":7,"1":3,"2":4}
dict={}
a=sorted(dic.keys())
for i in a:
    dict[i] = dic[i]
jsondata=json.dumps(dict)
print(jsondata) 
print(type(jsondata))   dict