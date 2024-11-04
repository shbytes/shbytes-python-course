
# remove method - remove signed long
print("remove method - remove signed long")
import array as array
signed_long_array = array.array("l", [-18934898, 23478783, -3892839, -4378734, 38989347])
print(signed_long_array)
return_value = signed_long_array.remove(-3892839)
print(signed_long_array)
print(return_value)

print("\n---------------------------------------------------\n")

# ValueError - element to remove not in array
print("ValueError - element to remove not in array")
import array as array
integer_array = array.array("i", [10, -20, -30, 40])
print(integer_array)
try:
	integer_array.remove(50.89)
except ValueError as err:
	print("error", err)
	print(integer_array)

print("\n---------------------------------------------------\n")

# Custom implementation - remove element from an array
print("Custom implementation - remove element from an array")
import array as array

def custom_remove(array_object, element):
	new_array_object = array.array(array_object.typecode, [0] * (len(array_object) - 1))
	element_found = False
	for x in range(len(new_array_object)):
		if array_object[x] == element:
			element_found = True
		if element_found:
			new_array_object[x] = array_object[x+1]
		else:
			new_array_object[x] = array_object[x]
	if not element_found:
		raise ValueError("custom_remove(arr, x): x not in arr")
	return new_array_object

integer_array = array.array("i", [10, -20, -30, 40])
print(integer_array)
integer_array = custom_remove(integer_array, -30)
print(integer_array)

print("\n---------------------------------------------------\n")

# pop method - pop index element
print("pop method - pop index element")
import array as array
signed_long_array = array.array("l", [-18934898, 23478783, -3892839, -4378734, 38989347])
print(signed_long_array)
pop_element = signed_long_array.pop(-3)
print(signed_long_array)
print(pop_element)
print("\n---------------------------------------------------\n")

# IndexError - index out of range
print("IndexError - index out of range")
import array as array
integer_array = array.array("i", [10, -20, -30, 40])
print(integer_array)
try:
	pop_element = integer_array.pop(8)
except IndexError as err:
	print("error", err)
	print(integer_array)
print("\n---------------------------------------------------\n")

# array of integer type - del - delete integer
print("array of integer type - del - delete integer")
import array as array
integer_array = array.array("i", [10, 20, 30, 40])
print(integer_array)
del integer_array[2]
print(integer_array)

print("\n---------------------------------------------------\n")

# del - delete array
print("del - delete array")
import array as array
integer_array = array.array("i", [10, 20, 30, 40])
print(integer_array)
del integer_array
#print(integer_array)

print("\n---------------------------------------------------\n")

# del - delete element from an array
print("del - delete element from an array")
import array as array
integer_array = array.array("i", [1540, 245450, 345450, 445450, 89839, 236762])
print(integer_array)
del integer_array[2]
print(integer_array)
del integer_array[1:3]
print(integer_array)

# similarly we can remove elements from other typecode type array
# comprehension and filter