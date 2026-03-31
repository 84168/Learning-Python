# FUNCTIONS
def printHelo(): # function definition 
    print("hello")

printHelo() # function call

def sum(a,b):
    return a + b

print(sum(1,2))

def avg(a,b,c):
    return (a+b+c)/3

print(avg(1,1,1))

def sum(a, b =1):  # default value of b is 1 NOTE : all default variable should be at last
    return a + b

print(sum(4,5)) # output is 9
print(sum(5)) # output is 6

# Lambda function
sum = lambda a,b : a+b   # lambda any no. of variables : only one mathematical expression can be written
print(sum(2,2))

def factorial(a):
    fact = 1
    while(a > 0):
        fact = fact * a
        a -= 1
    return fact

print(factorial(5))

# using recursion 
def facto(a):
    if(a == 0):
        return 1
    else:
        return a * facto(a-1)

print(facto(3))
