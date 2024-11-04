shbytes_tuple = ("Java", "Azure", "AWS", "Python", 14, 15, 16)

# positive index, start from left, start with 0
print(shbytes_tuple)
print("element at index 0 - ", shbytes_tuple[0])
print("element at index 1 - ", shbytes_tuple[1])
print("element at index 5 - ", shbytes_tuple[5])

print("\n---------------------------------------------------\n")

# traversing tuple using index, start from left, start with 0
print(shbytes_tuple)
for i in range(len(shbytes_tuple)):
    print("index : ", i, " | value : ", shbytes_tuple[i])

print("\n---------------------------------------------------\n")	

# negative index, start from right, start with -1
print(shbytes_tuple)
print("element at index -1 - ", shbytes_tuple[-1])
print("element at index -2 - ", shbytes_tuple[-2])
print("element at index -7 - ", shbytes_tuple[-7])

print("\n---------------------------------------------------\n")

# traversing tuple using index, start from right, start with -1
print(shbytes_tuple)
for i in range(-1, -(len(shbytes_tuple)+1), -1):
    print("index : ", i, " | value : ", shbytes_tuple[i])

print("\n---------------------------------------------------\n")

# Error out of range - positive index
print(shbytes_tuple)
#print("element at index 7 - ", shbytes_tuple[7])

# Error out of range - negative index
print(shbytes_tuple)
#print("element at index -8 - ", shbytes_tuple[-8])

print("\n---------------------------------------------------\n")
mixed_tuple = (12, 'shbytes', 33.14)
# print(mixed_tuple[3])  # Raises IndexError: tuple index out of range

mixed_tuple = (12, 'shbytes', 33.14, "Python")
print(mixed_tuple[1:4])  # slicing elements: ('shbytes', 33.14, 'Python')

