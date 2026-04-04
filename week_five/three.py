# JASON Module, java script object notation , its a formate to store data 
# similar with python dictionaries
import json

# json.loads and dumps -> here "s" denotes the string => means Json string converted to python object
# jason_str = '{"name":"tarun", "isTeacher":true}'
# print(type(jason_str))                          # <class 'str'>

# py_obj = json.loads(jason_str)                  # to convert jason string to puthon object
# print(py_obj)
# print(type(py_obj))                             # <class 'dict'>


# python_obj = {
#     "name": "tarun parmar",
#     "isteacher": True
# }

# jason_string = json.dumps(python_obj)           # to convert python obj to json string
# print(jason_string)


# .load and .dump -> used to retreve and store from json file

# with open("data.json", "r") as f:
#     py_obj = json.load(f)                   # Convert json string file to python object
#     print(py_obj)

d = {
    "name": "Tarun Parmar",
    "age": 23,
    "isTeacher": True
}
with open("data.json", "w") as f:
    # json.dump(d, f)             # dump(data U want to stor in json file,  json file object)
    # json.dump(d, f, indent=4)    # can add indentatio in file data
    json.dump(d, f, indent=4, sort_keys=True)