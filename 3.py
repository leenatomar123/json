import json
dict1={"name":"rohan","sec":"b","age":4}
dict2=json.dumps(dict1)
print(type(dict2))
print(dict2)