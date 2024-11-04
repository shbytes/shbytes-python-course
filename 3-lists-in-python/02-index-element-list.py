shbytes_list = ["Java", "Azure", "AWS", "Python", 14, 15, 16]

# positive index, start from left, start with 0
print(shbytes_list)
print("element at index 0 - ", shbytes_list[0])
print("element at index 1 - ", shbytes_list[1])
print("element at index 5 - ", shbytes_list[5])

print("\n---------------------------------------------------\n")

# traversing list using index, start from left, start with 0
print(shbytes_list)
for i in range(len(shbytes_list)):
    print("index : ", i, " | value : ", shbytes_list[i])

print("\n---------------------------------------------------\n")	

# negative index, start from right, start with -1
print(shbytes_list)
print("element at index -1 - ", shbytes_list[-1])
print("element at index -2 - ", shbytes_list[-2])
print("element at index -7 - ", shbytes_list[-7])

print("\n---------------------------------------------------\n")

# traversing list using index, start from right, start with -1
print(shbytes_list)
for i in range(-1, -(len(shbytes_list)+1), -1):
    print("index : ", i, " | value : ", shbytes_list[i])

print("\n---------------------------------------------------\n")

# Error index out of range
print(shbytes_list)
print("element at index -8 - ", shbytes_list[-8])
print("element at index 7 - ", shbytes_list[7])