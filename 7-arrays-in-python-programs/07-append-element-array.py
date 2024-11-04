
# array of double type - append method - append double
print("array of double type - append method - append double")
import array as array
double_array = array.array("d", [13.43, 25.67, 32.54, 40.76])
print(double_array)
double_array.append(58.76)
print(double_array)

print("\n---------------------------------------------------\n")

# array of integer type - append method - append duplicate integer
print("array of integer type - append method - append duplicate integer")
import array as array
integer_array = array.array("i", [10, 20, 30, 40])
print(integer_array)
integer_array.append(40)
print(integer_array)

print("\n---------------------------------------------------\n")

# array of integer type - append method - append double
print("array of integer type - append method - append double")
import array as array
integer_array = array.array("i", [10, 20, 30, 40])
print(integer_array)
try:
	integer_array.append(50.55)
except TypeError as err:
	print("error", err)
	print(integer_array)

print("\n---------------------------------------------------\n")

# array of unsigned short type - append method - append unsigned short
print("array of unsigned short type - append method - append unsigned short")
import array as array
unsigned_short_array = array.array("H", [1, 2, 3, 4])
print(unsigned_short_array)
unsigned_short_array.append(5)
print(unsigned_short_array)

print("\n---------------------------------------------------\n")

# array of unsigned short type - append method - append signed short
print("array of unsigned short type - append method - append signed short")
import array as array
unsigned_short_array = array.array("H", [1, 2, 3, 4])
print(unsigned_short_array)
try:
	unsigned_short_array.append(-5)
except OverflowError as err:
	print("error", err)
	print(unsigned_short_array)
	
# similarly we can append elements from other typecode type array

# custom implementation - append() method
print("custom implementation - append() method")

import array as array

def custom_append(array_object, element):

	new_array_object = array.array(array_object.typecode, [0] * (len(array_object) + 1))

	for x in range(len(array_object)):
		new_array_object[x] = array_object[x]

	new_array_object[len(array_object)] = element
	return new_array_object


signed_long_array = array.array("l", [135, 28976, -323674, -499834])
signed_long_array = custom_append(signed_long_array, 5055)
print(signed_long_array)