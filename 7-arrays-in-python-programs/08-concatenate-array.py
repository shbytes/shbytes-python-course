
import array as array

# extend method - extend array
print("extend method - extend array")
integer_array = array.array("i", [10, 20, 30, 40])
print(integer_array)
integer_array.extend(array.array("i", [50, 60]))
print(integer_array)

print("\n---------------------------------------------------\n")

# concatenate array with same array
print("concatenate array with same array")
signed_long_array = array.array("l", [18989, -289897, 89330])
print(signed_long_array)
concat_array = signed_long_array + signed_long_array
print(concat_array)

print("\n---------------------------------------------------\n")

# concatenate array using '+' operator
print("concatenate array using '+' operator")
signed_short_array = array.array("h", [54, 22, -35, 89])
print(signed_short_array)
concat_array = signed_short_array + array.array("h", [-35, 69])
print(concat_array)

print("\n---------------------------------------------------\n")

# error while concatenate array with array of different typecode
print("concatenate array wih same array")
integer_array = array.array("i", [10, 20, 30, 40])
print(integer_array)
try:
	concat_array = integer_array + array.array("d", [50.5])
except TypeError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

# Concatenate using operator plugin
print("Concatenate using operator plugin")
import operator                         # Import operator module
a = array.array("i", [5,6,8])
b = array.array("i", [50,60,80])
c = operator.add(a,b)                   # Concatenate array using operator.add method
print("a - ", a)
print("b - ", b)
print("c - ", c)                        # Print concatenated array

print("\n---------------------------------------------------\n")

# Concatenate using itertools.chain()
print("Concatenate using itertools.chain()")
import itertools                            # Import itertools module
x = array.array("i", [5,6,8])
y = array.array("i", [50,60,80])
z = array.array("i", itertools.chain(x, y)) # Concatenate array using itertools.chain
print("x - ", x)
print("y - ", y)
print("z - ", z)                            # Print concatenated array

print("\n---------------------------------------------------\n")

# unpacking - (*k, *l) - using asterisk*
print("unpacking - [*k, *l] - using asterisk*")

k = array.array("i", [5,6,8])
l = array.array("i", [50,60,80])       # Print defined arrays k and l

m = array.array("i", [*k , *l])        # unpack and collect elements

print("k - ", k)
print("l - ", l)
print("m - ", m)                       # Print concatenated array

print("\n---------------------------------------------------\n")

# TypeError - array with different type-code
print("TypeError - array with different type-code")
signed_short_array = array.array("h", [54, 22, -35, 89])
concat_array = signed_short_array + array.array("H", [35, 69])