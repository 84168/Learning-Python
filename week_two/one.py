# conditional statement
age = int(input("enter your age"))
if age > 18:
    print("can vote")
elif age <18:
    print("can;t")
else :
    print("default")

# Traffic light
color = input("color is?? ")
if(color == "green"):
    print("you can go now")
elif(color == "red"):
    print("Stay till became green ")
elif(color == "yellow"):
    print("start the engine")
else:
    print("Enter a valid traffic light color")

# age to category
age = int(input("enter age "))
if(age <13):
    print("you are a child")
elif(age >= 13 and age < 18):
    print("you are teenager")
elif(age >= 18):
    print("your are an adult")
else:
    print("enter valid age")

# Multiple or not
multiple = int(input("check multilple for"))
num = int (input("enter number to check it is multiple or not: "))
if(num % multiple == 0):
    print("Yes it is multiple of ", multiple)
else:
    print("No it is not a multiple")

# Match case
color = input("enter color")
match color:
    case "green":
        print("GO")
    case "red":
        print("Stop")
    case "yellow":
        print("look")
    case _: # default
        print("enter valid color")