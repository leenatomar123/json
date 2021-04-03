import json
data = '{"Name":"Ram", "Class":"IV", "Age":9 }'

my_file=json.loads(data)
print(type(my_file))
print(my_file)