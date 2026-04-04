# f = open("data.txt" ,"r") # open(fileName, mode) 

# print(f)  # stores the object of the file contains info like address, mode, encoding 
# # data = f.read()
# # print(data)
# # print(type(data))

# data1 = f.readline()  # reads the data line by line
# print(data1)          # Prints only first line

# data2 = f.readline()
# print(data2)
# f.close()

# # f = open("data.txt", "w")
# # f.write("my whole file data is overwritten by f.write")
# # f.close()



# Modes
# 1. Reading        Default is the reading mode
# f = open("data.txt")  #OR
f = open("data.txt" , "r")
f.close()

# 2. Writing, truncate file first
# f = open("data.txt", "w")
# f.close()

# 3. writing, appends at end
# f = open("data.txt", "a")
# f.write("new text is appended \n and this is it")
# f.close()

# 4. creates new and open for writing
# x is used only when file is not exits but if file is exist then 
# it shows error
# f = open("data2.txt", "x")
# f.write("this is text is written from creates X")
# f.close()

# 5. text mode default
# f = open("data.txt" , "rt")         # also write "r"
# f.close()
# f = open("data.txt", "wt")          # also write "w"
# f.close()

# 6. opens disk file for updation (r&w)

# r+  we can perform both read and write.  read starts from the first index of file
# w+  we can both overwrite and read.      truncate the entire file
# a+  we can both append and read.         read starts from the last index of file
# f = open("data.txt", "r+")
# f.write("this is a text inmode r+") # this text is added at index zero of file
# f.close()

# f = open("data.txt", "w+")
# f.write("this is a text inmode w+") # first truncate the data.txt and then add this text
# f.close()

# f = open("data.txt", "a+")
# f.write("this is a text inmode a+") # append the data from last of the file 
# f.close()

# With Keyword : used so we dont need to explicitly close the file
# when we open and close file as above there is a gap of possibility of error so we Use
# with open("data.txt","r")as f:
#     data = f.read()
#     print(len(data)) # nextline is also counted
