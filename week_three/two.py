# Tuples Immutable sequesce of values

# tup = (1,2,3,4,5,6, "abs")
# print(tup[2])
# # tup[2] = 100 # NO ASSIGNMENT IS POSSIBLE IN TUPLE

# tup1 = (1) # single value tuple, python interpret it as expression 
# print(type(tup1)) # int

# tup1 =(1,)
# print(type(tup1)) # tuple

# print(tup[1:3])

# Tuple methods
# .index(val)        return first occurance idx
# .count(val)        count total occurance

# print(tup.index(3))
# print(tup.count(3))

# Dictionary Mutable and unordered
info ={
    "name":"tarun parmar",
    "age": 23,
    "subjects": ["maths", "Science"]    # LIST
}
print(info)
info["age"] = 24

# Methods
# .keys()             return all keys
# .values()           return all values
# .items()            return (key,val) pairs
# .get(val)           return val access to key
# .update(new_item)   radds new item to dict

# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("age"))       # if age not present it return null
# print(info.update({
#     "city":"indore"
# }))
# print(info)

# SET, collection of unique elements IMMutable

set1 = {1,2,3,3}
print(set1)  # output: 1,2,3
print(len(set1))  # output: 3

# empty_set = {}      # its type is dictionary

empty_set = set()   # its type is set

# Methods 
# .add(val)             adds a val
# .remove(va)           remove a val
# .clear()              empties the set
# .pop()                removes a random val
# .union(set2)          returns new union
# .intersection(set2)   returns new intersection
 
set1.add(23)
print(set1)

set1.remove(23)
print(set1)

set1.clear()
print(set1)

set1 = {1,2,3,4,4,5}
set2 = {2,3,4,5,6,7,8}

print(set1.pop())

print(set1.union(set2))

print(set1.intersection(set2))
