import json
x =  '{ "name":"John", "age":30, "city":"New York"}' #json
y = json.loads(x) # jsonto dict
print(y["age"])