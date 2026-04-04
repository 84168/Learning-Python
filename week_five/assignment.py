# # Question 1:
# with open("names.txt", "w") as f:
#     i = 1
#     while(i <= 5):
#         name = input("enter name: ")
#         f.write(str(i) + "."+ name + "\n")
#         i += 1

# with open("names.txt","r") as f:
#     data = True
#     while(data):
#         data = f.readline()
        # print(data)

# # Question 2:
# with open("log.txt", "a")as f:
#     f.write("\n Program run successfully")

# with open("log.txt", "r") as f:
#     print(f.read())

# # Question 3:
# list =[5,10,15,20,25]
# new_list = [i for i in list if i > 15]
# print(new_list)

# # Question 4:
# import json
# with open("cities.json", "r") as f:
#     py_obj = json.load(f)
#     print(py_obj)

#     check = input("want to add more (y/n): ")
#     if(check == "y"):
#         new_city = input("Enter city name: ")
#         new_popu = input("Enter pupulation: ")
#         py_obj[new_city] = new_popu
#     with open("cities.json", "w")as f:
#         json.dump(py_obj, f, indent=4)

# Question 5:
try:
    data = open("file.txt" ,"r")
except FileNotFoundError:
    print("File Not Found")
else:
    print(data.read())
finally:
    print("programme success")