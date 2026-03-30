# LOOPS
# i = 1
# while(i <= 5):
#     print("hell0")
#     i = i -1 

# i = 5
# while(i >0):
#     print(i)
#     i -= 1


# table
# num = int(input("enter a number"))
# i = 1
# while(i<= 10):
#     print(i * num)
#     i+=1

# Break : To terinate the loop
# i = 1
# while(i<=10):
#     if(i%6 == 0):
#         break
#     print(i)
#     i += 1

# Continue : skip the perticular Iteraions
# i = 1
# while(i<=10):
#     if(i%3 ==0):
#         i+=1
#         continue

#     print(i)
#     i+=1


# FOR LOOP USED FOR Sequential traversal
# string = "Hello"
# for var in string: # in => membership operator
#     print(var)

# if 'o' in string:
#     print("o exist in string")

# for i in range(5): # range(n) means a sequence of elements from 0 to n-1 is created
#     print(i)


# COUNT i 
# word = "artificial intellingence"
# count =0
# for var in word:
#     if(var == "i"):
#         count += 1

# print(count)

# range(start, stop, step)
# start: starting point of range (not compulsory to be added in function)
# stop: must be added
# step: how much increment in value 
for i in range(2, 11, 2):
    print(i)