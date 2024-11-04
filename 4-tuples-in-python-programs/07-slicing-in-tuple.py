#slicing using colon (:) operator
#tuple[start:end:step]

#slicing using slice method
#slice(start, end, step)

shbytes_tuple=(0,1,2,3,4,5,6,7,8,9,10,11)

#length of a tuple
print("length of a tuple")
print(shbytes_tuple, type(shbytes_tuple))
print("length of tuple", len(shbytes_tuple))

print("\n---------------------------------------------------\n")

# slicing range will be from index 1 to 8 (end - 1) and step of 2
print("slicing range will be from index 1 to 8 (end - 1) and step of 2")
print(shbytes_tuple, type(shbytes_tuple))
print(shbytes_tuple[1:9:2])
print(shbytes_tuple[slice(1, 9, 2)])

print("\n---------------------------------------------------\n")

# slicing will not throw an error, if end index is more than tuple limit
print("slicing will not throw an error, if end index is more than tuple limit")
print(shbytes_tuple, type(shbytes_tuple))
print(shbytes_tuple[2:14])
print(shbytes_tuple[slice(2, 14)])

print("\n---------------------------------------------------\n")

# slicing value from index 1 to end of the tuple
print("slicing value from index 1 to end of the tuple")
print(shbytes_tuple, type(shbytes_tuple))
print(shbytes_tuple[1:])
print(shbytes_tuple[slice(1, -1)])
print(shbytes_tuple[slice(1, 12)])

print("\n---------------------------------------------------\n")

# slicing value from index 0 to 3 of the tuple
print("slicing value from index 0 to 3 of the tuple")
print(shbytes_tuple, type(shbytes_tuple))
print(shbytes_tuple[:4])
print(shbytes_tuple[slice(4)])

print("\n---------------------------------------------------\n")

# Negative slicing start from the right hand side from -1 index position
print("Negative slicing start from the right hand side from -1 index position")
print(shbytes_tuple, type(shbytes_tuple))
print(shbytes_tuple[:-1])
print(shbytes_tuple[slice(-1)])

print("\n---------------------------------------------------\n")

# slicing value will be start from -3 index to -2 index position
print("slicing value will be start from -3 index to -2 index position")
print(shbytes_tuple, type(shbytes_tuple))
print(shbytes_tuple[-3:-1])
print(shbytes_tuple[slice(-3,-1)])

print("\n---------------------------------------------------\n")

# slicing value from index position 0 to (tuple limit - 1) from left
print("slicing value from index position 0 to (tuple limit - 1) from left")
print(shbytes_tuple, type(shbytes_tuple))
print(shbytes_tuple[0:-1])
print(shbytes_tuple[slice(0, -1)])

print("\n---------------------------------------------------\n")

# slicing value from index position 0 to 10 from left
print("slicing value from index position 0 to 10 from left")
print(shbytes_tuple, type(shbytes_tuple))
print(shbytes_tuple[0:11])
print(shbytes_tuple[slice(0,11)])

print("\n---------------------------------------------------\n")

# slicing value from index 0 and after second step each of the element from left
print("slicing value from index 0 and after second step each of the element from left")
print(shbytes_tuple, type(shbytes_tuple))
print(shbytes_tuple[::2])
print(shbytes_tuple[slice(0, -1, 2)])

print("\n---------------------------------------------------\n")

# slicing value from index -1 and after second step each of the element from right
print("slicing value from index -1 and after second step each of the element from right")
print(shbytes_tuple, type(shbytes_tuple))
print(shbytes_tuple[::-2])
print(shbytes_tuple[slice(-1, 0, -2)])

print("\n---------------------------------------------------\n")
numbers_tuple = (130, 220, 35, 46, 51)
# slice from left to right
result = numbers_tuple[3:1:1]  # Start index is greater than stop index, positive step
print(result)  # Empty tuple => ()

numbers_tuple = (130, 220, 35, 46, 51)
# slice from right to left
result = numbers_tuple[3:1:-1]     # Start index is greater than stop index, negative step
print(result)  # Tuple elements => (46, 35)

print("\n---------------------------------------------------\n")
numbers_tuple = (130, 220, 35, 46, 51)
sliced_tuple = numbers_tuple[::0]  # ValueError: slice step cannot be zero

