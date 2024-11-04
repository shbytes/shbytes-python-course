
# positive indexing - access and update element in array
print("positive indexing - array of integer type - update integer")
import array as array
integer_array = array.array("i", [10, 20, 30, 40, 50])
print(integer_array)
print("element at index 3 = ", integer_array[3])
integer_array[3] = 70
print("updated element at index 3 = ", integer_array[3])

print("\n---------------------------------------------------\n")

# negative indexing - access and update element in array
print("negative indexing - array of integer type - update integer")
import array as array
integer_array = array.array("i", [10, 20, 30, 40, 50])
print(integer_array)
print("element at index -3 = ", integer_array[-3])
integer_array[-3] = 70
print("updated element at index -3 = ", integer_array[-3])

print("\n---------------------------------------------------\n")

# IndexError - access element in array
print("IndexError - access element in array")
import array as array
integer_array = array.array("i", [10, 20, 30, 40, 50])
print(integer_array)
print("element at index 5 = ", integer_array[5])

print("\n---------------------------------------------------\n")

# array of integer type - update 2D integer
print("array of integer type - update 2D integer")
integer_2d_array = [[10, 20], [30, 40], [50, 60]]
print(integer_2d_array)
integer_2d_array[1][1] = 70
print(integer_2d_array)

print("\n---------------------------------------------------\n")

# array of integer type - update 3D integer
print("array of integer type - update 3D integer")
integer_3d_array = [[[10, 20], [30, 40]], [[1, 2], [3, 4]]]
print(integer_3d_array)
integer_3d_array[1][1][1] = 7
print(integer_3d_array)

# similarly we can update elements in other type array
