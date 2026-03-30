# Question: 1
name = input("Enter Your Name:")
age = input("Enter Your Age")
print("hello", name, "you are", age, "years old!")

# Question: 2
a = int(input("Enter first no."))
b = int(input("Enter second no."))
print("Addition",a+b)
print("Subtraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)

# Question: 3
# a = float(input("Enter a integer"))
# b = float(input("Enter a integer"))
# c = float(input("Enter a float"))

avg = (a+b+c)/3
print(avg)

# Question: 4
a = input("Enter an number")
a = int(a)
print(a, type(a) )
a = float(a)
print(a, type(a))
a = str(a)
print(a, type(a))

# Question: 5
x = 10 + 3 * 2 ** 2
print(x)

# Question: 6
a = input("enter first number")
b = input("eneter another number")

c = a
a = b
b = c

print("first no is", a,"\nsecond no is", b)

# Question: 7
temp = float(input("enter temperature in celsius"))
print("temperature in fahrenheit is ", temp * (9 / 5) + 32)

# Question: 8
radius = int(input("enter radius:"))
pi = 3.14
print("Area is ", pi * radius ** 2)

# Question: 9
P = float(input("Enter Principal"))
R = float(input("Enter Rate"))
T = float(input("Enter Time"))
print("Simple Interest is", (P*R*T)/100)

# Question: 10
num = float(input('enter flaot value'))
print("integer part-", int(num))
print("fractional part-", int((num - int(num)) * 100) / 100)