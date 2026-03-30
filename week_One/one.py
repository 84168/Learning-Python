# This is python basics, it is CASE Secnsitive 

print("hello world", "this is me")
print("hello world \n", "this is me")

# Variables
name="comrade"
age = 23
PI = 3.14
isTrue = True
gender = None

print("my name is", name, "and i am", age, "years old")

# Data Type
print(type(gender))

# tot_price -> snake case
# totPrice -> camelCase
# TotPrice -> pascle case

a=10
b=5
# Arithmetic Operator
print(a+b)
print(a-b)
print(a/b)
print(a%b)
print(a**b)

# Relational / Comparison
print(a>b)
print(a<b)
print(a == b)
print(a != b)
print( not (a != b))
print(a>=b)

# Assignment 

c = a
c += 2 # c = c + 2

# Logical Expression 
print((False) and (True))
print((False) or (True))
print(not ((False) and (True)))

# Type Concersion Implicit -> python
a = 3
b = 3.0
print(type(a+b))

# Type casting explicit ->user
ans1 = int(a + b) #casting
ans2 = a + b    #Conversion

print(type(ans1))
print(type(ans2))

a = input("enter value of a") #BY DEFAULT ALL THE INPUT IS OF TYPE STRING
b = input("eneter b ")
print(a+b)
print(int(a) + int(b))

print("Average of two no's are : \n")
print(int((int(a) + int(b)) / 2))