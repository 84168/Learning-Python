# Question: 1
str = input("enter a string: ")
rev_str =""
i = 0
while(i < len(str)):
    rev_str = str[i] + rev_str
    i += 1

if(str == rev_str):
    print("Is a Palindrome")
else:
    print("Not a Plaindrome")

# Question: 2
list =[1,2,3,4,5]
print(len(list))
sum = 0
for var in list:
    sum += var
print(f"average is : {sum / 3}")

# Question: 3
i = 3
list1 = []
list2 = []
print(type(list1))
while(i > 0):
    list1.append(input("Enter a number to add in list1 : "))
    i -= 1

while(i < 3):
    list2.append(input("Enter a number to add in list2 : "))
    i += 1
for var in list2:
    list1.append(var)

print(f"list one is : {list1}")
print(f"list two is : {list2}")
list1.sort()
print(list1)
# print(list1.sort()) => Once sort done method return NONE as completed
# You are asking Python to print the result of that rearrangement. 
# Since the result is None, that's what shows up on your screen.

# Question: 4
tup = (1,2,3,4,5,6,7,8,9,10)
even_tup = ()
odd_tup = ()
for var in tup:
    if(var % 2 == 0):
        even_tup = even_tup + (var,)
    else:
        odd_tup = odd_tup + (var,)

print(f"even values are : {even_tup}")
print(f"odd values are : {odd_tup}")

# Question: 5
dict = {}
print("Enter A to add student")
print("Enter B to update marks")
print("Enter C to search for student")
print("Enter D to display all student and marks")
print("Enter Z to terminate ")

val = input("Enter Operation: ")
while(val != "Z"):

    if(val == "A"):
        print("ADDITION OPERATION")
        student = input("Enter Student Name: ")
        marks = input("Enter marks: ")
        dict.update({student : marks})
        print("Student added Successfully! ")

    elif(val == "B"):
        print("UPDATION OPERATION")
        student = input("Enter student name : ")
        if student in dict:
            marks = input("Enter updated marks: ")
            dict[student] = marks # Direct assignment updates the value
            print("Updated successfully!")
        else:
            print("Student not found!")
        print("updated success")

    elif(val == "C"):
        student = input("Enter student name")

        if student in dict:
            print("Yes it is present")
        else:
            print("Not present")
    elif(val == "D"):

        print(dict)
    val = input("Enter Operation: ")

# Question: 6
words =["apple","banana","kiwi","cherry","mango"]
dict = {}
for var in words:
    if(dict.get(var) == None):
        dict.update({var: len(var)})

print(dict)

# Question: 7
str = input("Enter string: ")
i = 0
count = 0
while( i < len(str)):
    if(str[i] == " "):
        count += 1
    i += 1

print(f"space count is {count}")

# Question: 8
set1 = {1,2,3,4}
set2 = {5,2,7,8}
set3 = set1.intersection(set2)
if(len(set3) == 0):
    print("No common elements")
else:
    print("Common elements")

# Question: 9
list = [1,2,4,4,5,6,6,7]
print(type(list))
for var in list:
    if(list.count(var) > 1):
        print(var)


# Question: 10
str = input("Enter String: ")
set = set()
print(str)
for var in str:
    set.add(var)

print(f"all unique character : {set}")
print(f"count of unique charecter : {len(set)}")