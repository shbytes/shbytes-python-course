
shbytes_tuple = ('Python', 'AWS', 'Java', 'Azure')

# change tuple values - TypeError
print("change tuple values - TypeError")
print(shbytes_tuple)
# shbytes_tuple[2] = 'Machine Learning'
try:
	shbytes_tuple[2] = 'Machine Learning'
except TypeError as err:
	print("error", err)
	print(shbytes_tuple)

print("\n---------------------------------------------------\n")

# change tuple values - by converting it to list
print("change tuple values - by converting it to list")
print(shbytes_tuple)
temp_list = list(shbytes_tuple)
temp_list[2] = 'Machine Learning'
new_tuple = tuple(temp_list)
print(new_tuple)

print("\n---------------------------------------------------\n")

# change mutable elements in tuple
print("change mutable elements in tuple")
nested_tuple = ('Python', 'AWS', 'Azure', [1, 2, 3])
print("original nested tuple", nested_tuple)
nested_tuple[3][2] = 4
print("changed mixed tuple", nested_tuple)

print("\n---------------------------------------------------\n")
number_tuple = (16, 25, 35)
new_tuple = number_tuple[:1] + (44,) + number_tuple[2:]
print(new_tuple)  # Elements in new_tuple => (16, 44, 35)

print("\n---------------------------------------------------\n")
shbytes_tuple = ('Python', 'AWS', 'Java', 'Azure')
temp_list = list(shbytes_tuple)
temp_list[2] = 'Machine Learning'
new_tuple = tuple(temp_list)
print(new_tuple)  # Elements in new_tuple => ('Python', 'AWS', 'Machine Learning', 'Azure')

print("\n---------------------------------------------------\n")
number_tuple = (16, [25, 45], 35)
number_tuple[1][0] = 105
print(number_tuple)    # Elements in number_tuple: (16, [105, 45], 35)

print("\n---------------------------------------------------\n")
nested_tuple = (12, (22, 32), [45, 55])

# Accessing elements
print(nested_tuple[1])     # Returns element at index 1 => (22, 32)
print(nested_tuple[2][0])  # Returns 0 index from element at index 2 => 45

# Modifying mutable elements within the nested tuple
nested_tuple[2][1] = 66
print(nested_tuple)  # Elements in nested_tuple => (12, (22, 32), [45, 66])


print("\n---------------------------------------------------\n")
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(12, 22)
print(p.x, p.y)  # Output: 12 22

print("\n---------------------------------------------------\n")
from immutables import Map

m = Map({"a": 12, "b": 22})
print(m["a"])   # print value 12

