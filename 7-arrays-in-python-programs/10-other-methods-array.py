
import array as array
double_array = array.array("d", [134.1, 9267.2, 8763.3, 423.4, 273.89])
print(double_array)

# itemsize of array - length in bytes of one array item
print("itemsize of array - itemsize method on array")
import array as array
double_array = array.array("d", [134.1, 9267.2, 8763.3, 423.4, 273.89])
print(double_array)
array_itemsize = double_array.itemsize
print(array_itemsize)

print("\n---------------------------------------------------\n")

# array built-in methods
print("array built-in methods")
import array as array
double_array = array.array("d", [134.1, 9267.2, 8763.3, 423.4, 273.89])
print(double_array)
array_length = len(double_array)
print(array_length)
elements_sum = sum(double_array)
print(elements_sum)
min_element = min(double_array)
print(min_element)
max_element = max(double_array)
print(max_element)

print("\n---------------------------------------------------\n")

# array built-in methods
print("array built-in methods")
import array as array
signed_short_array = array.array("h", [13, 92, 87, 42, 27, 87])
print(signed_short_array)
element_count = signed_short_array.count(87)
print(element_count)
array_itemsize = signed_short_array.itemsize
print(array_itemsize)
short_list = signed_short_array.tolist()
print(short_list)

print("\n---------------------------------------------------\n")

# sorting of an array - sorted() method
print("sorting of an array - sorted() method")
import array as array
double_array = array.array("d", [134.1, 9267.2, 8763.3, 423.4, 273.89])
print(double_array)
sorted_array = sorted(double_array)
print(sorted_array)