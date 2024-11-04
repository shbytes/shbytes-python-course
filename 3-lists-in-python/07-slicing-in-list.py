#slicing using colon (:) operator
#list[start:end:step]

#slicing using slice method
#slice(start, end, step)

sybytes_list=[0,1,2,3,4,5,6,7,8,9,10,1]

#length of a list
print("length of a list")
print(sybytes_list, type(sybytes_list))
print("length of list", len(sybytes_list))

print("\n---------------------------------------------------\n")

#slicing range will be from index 1 to 3 (end - 1)
print("slicing range will be from index 1 to 3 (end - 1)")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[1:4])
print(sybytes_list)
print(sybytes_list[slice(1, 4)])
print(sybytes_list)

print("\n---------------------------------------------------\n")

#slicing will not throw an error, if end index is more than list limit
print("slicing will not throw an error, if end index is more than list limit")
print(sybytes_list[2:14])
print(sybytes_list[slice(2, 14)])
print(sybytes_list)

print("\n---------------------------------------------------\n")

#slicing value from index 1 to end of the list
print("slicing value from index 1 to end of the list")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[1:])                 # colon operator, end index not required
print(sybytes_list[slice(1, -1)])       # slice method, end index with negative indexing
print(sybytes_list[slice(1, 12)])       # slice method, end index with positive indexing
print(sybytes_list)

print("\n---------------------------------------------------\n")

#slicing value from index 0 to 3 of the list
print("slicing value from index 0 to 3 of the list")
print(sybytes_list[:4])
print(sybytes_list[slice(4)])
print(sybytes_list, type(sybytes_list))

print("\n---------------------------------------------------\n")

# Slicing end index - Negative indexing
print("Slicing end index - Negative indexing")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[:-1])
print(sybytes_list[slice(-1)])

print("\n---------------------------------------------------\n")

# Slicing start and end index - Negative indexing
print("Slicing start and end index - Negative indexing")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[-3:-1])
print(sybytes_list[slice(-3,-1)])

print("\n---------------------------------------------------\n")

#slicing value from index position 0 to (list limit - 1) from left
print("slicing value from index position 0 to (list limit - 1) from left")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[0:-1])
print(sybytes_list[slice(0, -1)])

print("\n---------------------------------------------------\n")

#slicing value from index position 0 to 10 from left
print("slicing value from index position 0 to 10 from left")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[0:11])
print(sybytes_list[slice(0,11)])

print("\n---------------------------------------------------\n")

# Slicing left to right - Positive step
print("Slicing left to right - Positive step")
sybytes_list=[0,1,2,3,4,5,6,7,8,9,10,11]
print(sybytes_list, type(sybytes_list))
print(sybytes_list[::2])
print(sybytes_list[slice(0, -1, 2)])

print("\n---------------------------------------------------\n")

# Slicing right to left - Negative step
print("Slicing right to left - Negative step")
sybytes_list=[0,1,2,3,4,5,6,7,8,9,10,11]
print(sybytes_list, type(sybytes_list))
print(sybytes_list[::-2])
print(sybytes_list[slice(-1, 0, -2)])

print("\n---------------------------------------------------\n")
number_list = [12, 24, 36, 48, 58]
number_list[1:4] = [21, 31, 41]  # Replace elements from index 1 to 3
print(number_list)               # number_list after replacing elements: [10, 21, 31, 41, 50]

number_list[1:3] = [22]          # Replace elements at index 1 and 2 with a single element
print(number_list)               # number_list after replacing elements: [10, 22, 41, 50]

print("\n---------------------------------------------------\n")
number_list = [12, 24, 36, 48, 58]
number_list[2:2] = [25, 26]  # Insert [25, 26] at index 2
print(number_list)  # number_list elements after inserting: [12, 24, 25, 26, 36, 48, 58]

print("\n---------------------------------------------------\n")
number_list = [12, 24, 36, 48, 58]
number_list[1:3] = []
print(number_list)  # number_list elements after deleting: [12, 48, 58]

print("\n---------------------------------------------------\n")
number_list = [12, 24, 36, 48, 58]
del number_list[1:3]
print(number_list)  # number_list elements after deleting: [12, 48, 58]

print("\n---------------------------------------------------\n")
class ShbytesClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"ShbytesClass({self.value})"

obj_list = [ShbytesClass(1), ShbytesClass(2), ShbytesClass(3), ShbytesClass(4), ShbytesClass(5)]
slice = obj_list[1:4]
print(slice)  # Output: [ShbytesClass(2), ShbytesClass(3), ShbytesClass(4)]


print("\n---------------------------------------------------\n")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# Slicing the outer list
outer_slice = matrix[1:3]
print(outer_slice)    # slice elements from outer list: [[4, 5, 6], [7, 8, 9]]

# Slicing an inner list
inner_slice = matrix[1][1:3]
print(inner_slice)    # slice elements from inner list: [5, 6]

