# STRINGS , immutable
word = "python"
word1 = "i like "

# print(len(word)) # zero based indexing

# concatination
# print(word1 + word)

# for ch in word:
#     print(ch)

# slicing
# print(word[2:4])

# formating
a =2
b =3
sum = a+b

# normal formating
# print("sum of {} and {} is {}".format(a,b,sum))

# index formating
# print("sum of {1} and {0} is {2}".format(a,b,sum)) # format(idx0, idx1, idx2 ...)

# value based formating
# print("sum of {a} and {b} is {sum}".format(a=3, b=2, sum = a+b))

# f_ String
# print(f"sum of {a} and {b} is {a+b}")

# LIST is a mutable sequences of values
marks = [99, 89, 100, 65, 92]
# print(len(marks))
# print(marks[2])
# marks[2] = 17
# print(marks)

# print(marks[0:3])
# print(marks[-4:-1])

# LISTS METHODs
# .append(val)          add at last
# .insert(idx, val)     add at Index
# .sort()               increasing order
# .reverse()            reverse order


# marks.append(45)
# print(marks)

# marks.insert(2,2000)
# print(marks)

# marks.sort() #Ascending
# print(marks)

# marks.sort(reverse=True) #Descending
# print(marks)

# marks.reverse()
# print(marks)

# LIST , loops
idx = 0
ele = 89
for val in marks:
    if(val == ele):
        print(idx)
        break
    idx += 1
