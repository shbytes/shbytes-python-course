
# comprehension with array
print("comprehension with array")
import array as array
comprehension_array = array.array("h", [x for x in range(100) if x > 30 and x % 6 == 0])
print(comprehension_array)

print("\n---------------------------------------------------\n")

import array as array
double_array = array.array("d", [13.43, 25.67, 32.54, 40.76, 80.89])
print(double_array)
comprehension_array = array.array("d", [x for x in double_array if x > 30.00])
print(comprehension_array)

print("\n---------------------------------------------------\n")

# slicing of arrays
print("slicing of arrays")
import array as array
double_array = array.array("d", [13.43, 25.67, 32.54, 40.76, 80.89, 60.0, 96.0])
print(double_array[::])
print(double_array[0:])
print(double_array[:4])
print(double_array[-3:])
print(double_array[:-4])
print(double_array[0::-1])
print(double_array[:4:2])
print(double_array[-3::2])
print(double_array[:-4:-1])
print(double_array[0:5:2])
print(double_array[-6:-1:2])

print("\n---------------------------------------------------\n")

# filter with array
print("filter with array")
import array as array
filter_array = array.array("h", filter(lambda x: x > 30 and x % 6 == 0, array.array("h", range(100))))
print(filter_array)

print("\n---------------------------------------------------\n")

double_array = array.array("d", [13.43, 25.67, 32.54, 40.76, 80.89])
print(double_array)
filter_array = array.array("d", filter(lambda x: x > 30.00, double_array))
print(filter_array)
