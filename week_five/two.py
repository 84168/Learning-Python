# # Word Search
# with open("data.txt", "r+") as f:

#     data = f.readline()
#     line = 0
#     while data : 
#         line += 1
#         if("practise" in data):
#             print(f"present in line {line}")
#         data = f.readline()

# # Exception handling
# # try, except, else, finally

# try:
#     x = int(input("enter something"))
#     ans = 10 / x
# except ZeroDivisionError:
#     print("divid by zero not allowed")
# except ValueError:
#     print("invalid input")
# else:
#     print(ans)
# finally:
#     print("end of programme")


# # List Comprehension
# squares = []

# for val in range(6):
#     squares.append(val * val)

# print(squares)

# sq = [i*i for i in range(6)]
# print(sq)

# sq = [i*i for i in range(6) if i % 2 != 0]  # using only if use these way
# print(sq)

# nums =[-2,-4,3,5,2,-1]
# nums = [ 0 if i < 0 else i for i in nums ]  # using both if , else use these
# print(nums)

def print_table(val):
    print(f"--- Multiplication Table of {val} ---")
    for i in range(1, 11):
        print(f"{val} x {i} = {val * i}")

print_table(2)