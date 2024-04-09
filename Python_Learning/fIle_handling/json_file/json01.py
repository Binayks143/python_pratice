import json

dict={
        "name":"Sachin",
        "class":"4A",
        "RollNo" : 87,
        "Address":"RKL"
    }
json_object=json.dumps(dict,indent=4)

with open('t2.json', 'w') as t1:
    t1.write(json_object)
