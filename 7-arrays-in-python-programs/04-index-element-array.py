# index method to get 1D index

import array as array

# array of double type - index of an element
print("array of double type - index of an element")
double_array = array.array("d", [14.232, 27.3, 30.34, 49.87])
print(double_array)
index = double_array.index(30.34)
print("index of element 30.34 = ", index)

print("\n---------------------------------------------------\n")

import array as array

# index method - element not in array
print("index method - element not in array")
integer_array = array.array("i", [10, 20, 30, 40, 50])
print(integer_array)
# index = integer_array.index(60.54)

print("\n---------------------------------------------------\n")

# custom_index of an element
print("custom_index of an element")

import array as array

def custom_index(array_object, element):
	for index_iter in range(len(array_object)):
		if array_object[index_iter] == element:
			return index_iter
	raise ValueError("custom_index(arr, x): x not in arr")

integer_array = array.array("i", [10, 20, 30, 40, 50])
print(integer_array)
index = custom_index(integer_array, 40)
print("index of element 40 = ", index)

print("\n---------------------------------------------------\n")

# update 2D integer
print("update 2D integer")
integer_2d_array = [[10, 20], [30, 40], [50, 60]]
print(integer_2d_array)
try:
	index_2d = integer_2d_array.index(20)
	print("index of value 20 - ", index_2d)
except ValueError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

# update 2D integer
print("update 2D integer")
integer_2d_array = [[10, 20], [30, 40], [50, 60]]
print(integer_2d_array)
index_2d = integer_2d_array[0].index(20)
print("index of value 20 - ", index_2d)
	
print("\n---------------------------------------------------\n")

# update 3D integer
print("update 3D integer")
integer_3d_array = [[[10, 20], [30, 40]], [[1, 2], [3, 4]]]
print(integer_3d_array)
index_3d = integer_3d_array[0][0].index(20)
print("20", index_3d)

# similarly we can get index of elements in other type array
