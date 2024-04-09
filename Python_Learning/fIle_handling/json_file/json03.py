import json

#Opening the json file
with open(r"C:\Users\home\Downloads\Format.json",'r') as file1:
    #reading the data from json file
    json_obj=json.load(file1)
print(json_obj)
print(type(json_obj))
