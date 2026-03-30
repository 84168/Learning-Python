# Question 1
salary = int(input("Enter your salary : "))
if(salary <= 30000):
    print("Your tax rate is : 5%")
elif(salary > 30000 and salary < 70000):
    print("Your tax rate is : 10%")
else:
    print("Your tax rate is : 25%")

# Question 2
start = int(input("Enter starting point : "))
end = int(input("Enter ending point : "))

while(start <= end):
    if(start % 2 == 0):
        print(start)
    
    start += 1


# Question 3
num = int(input("Enter a Number : "))

while(num > 0):
    n  = num % 10
    print(n)
    num = int (num / 10)

# Question 4
num = int(input("Enter a number : "))
def digitCount(num):
    count = 0
    while(num > 0):
        count += 1
        num = int(num / 10)
    
    return count

print(digitCount(num))

# Question 5
num = int(input("Enter a number : "))
def digitCount(num):
    sum = 0
    while(num > 0):
        sum += num % 10
        num = int(num / 10)
    
    return sum

print(digitCount(num))

# Question 6
for var in range(1,101):
    if(var % 3 == 0 and var % 5 == 0):
        print(var)

# Question 7
val = input("enter a num else Quit")
while(True):
    if(val == "Quit"):
        break
    print(val)
    val = input("Enter a number else Quit")

# Question 8
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
ope = input("Enter operation : ")

if(ope == "+"):
     print(a + b)
elif(ope == "-"):
     print(a -b)
elif(ope == "*"):
     print(a*b)
elif(ope == "/"):
     print( a/b)
else:
     print("enter valid operation")

# Question 9
num = int(input("enter number : "))
def is_prime(num):
    for var in range (2 , num):
        if(num % var == 0):
            return "Non_Prime"
    return True
print(is_prime(num))

# Question 10
my_Guess = 9
num = int(input("Guess the number or zero "))
while(True):
    
    if(num == 0):
        break
    elif(my_Guess - num == 0):
        print("Congratulations you guessed it right")
        break
    elif(my_Guess - num > 0 ):
        print("Too Low")
    elif(my_Guess - num < 0):
        print("Too High")

    num = int(input("Guess the number or zero "))