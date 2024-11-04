# Creation of an array
# Declaration and Initialization

import array as array

# taking list as an array
print("taking list as an array")
num_array = [12, 8, 68, 11]
print(num_array)
print(type(num_array))

print("\n---------------------------------------------------\n")

# create array by importing array module - array of integer type
# array.array(data_type, value_list)
print("create array by importing array module - array of integer type")
num_array = array.array("i", [10, 20, 30, 40])
print(num_array)
print(type(num_array))
print(num_array.typecode)

print("\n---------------------------------------------------\n")

# create array by importing array module - array of char type
# array.array(data_type, value_list)
print("create array by importing array module - array of char type")
char_array = array.array("u", ['o', 'm', 'p', 'r'])
print(char_array)
print(type(char_array))
print(char_array.typecode)

print("\n---------------------------------------------------\n")

# create array by importing array module - array of double type
# array.array(data_type, value_list)
print("create array by importing array module - array of double type")
double_array = array.array("d", [1.1, 2.2, 3.3, 4.4])
print(double_array)
print(type(double_array))
print(double_array.typecode)

print("\n---------------------------------------------------\n")

# create array by importing array module - array of float type
# array.array(data_type, value_list)
print("create array by importing array module - array of float type")
float_array = array.array("f", [1.111, 2.222, 3.333, 4.444])
print(float_array)
print(type(float_array))
print(float_array.typecode)

print("\n---------------------------------------------------\n")

# array can store duplicate elements
print("array can store duplicate elements")
num_array = array.array("i", [10, 10, 10, 10])
print(num_array)
print(type(num_array))

print("\n---------------------------------------------------\n")

# create 2D array of integer type
print("create 2D array of integer type")
num2d_array = [[2, 4], [7, 9], [10, 20]]
print(num2d_array)

print("\n---------------------------------------------------\n")

# create 3D array of integer type
print("create 3D array of integer type")
num3d_array = [[[2, 4], [7, 9]], [[10, 20], [30, 40]]]
print(num3d_array)

# similarly we can create other typecode type array
