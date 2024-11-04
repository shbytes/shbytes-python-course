
# array of integer type - reverse method
print("array of integer type - reverse method")
import array as array
integer_array = array.array("i", [10, 20, 30, 40])
print(integer_array)
integer_array.reverse()
print(integer_array)

print("\n---------------------------------------------------\n")

# array of double type - reverse method
print("array of double type - reverse method")
import array as array
double_array = array.array("d", [1.1, 2.2, 3.3, 4.4])
print(double_array)
double_array.reverse()
print(double_array)

print("\n---------------------------------------------------\n")

# reverse array - reverse method
print("reverse array - reverse method")
import array as array
double_array = array.array("d", [134.1, 9267.2, 8763.3, 423.4, 273.89])
print(double_array)
reversed_array = double_array[::-1]
print(reversed_array)
double_array.reverse()
print(double_array)

