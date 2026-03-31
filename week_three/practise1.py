info =[
    ("alice", "maths"),
    ("bob", "science"),
    ("alice", "science"),
    ("charlie", "maths"),
    ("bob", "maths"),
    ("alice", "english"),
    ("charlie","english"),
]
# list all unique course
# print(type(info))
# set1 = set()
# for var in info:
#     set1.add(var[1])

# print(set1)

# list stuedent enrolled in english
# for var in info:
#     if(var[1] == "english"):
#         print(var[0])


# create a dictionary (student, set of courses)
dict = {}
print(type(dict))
for name, course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)