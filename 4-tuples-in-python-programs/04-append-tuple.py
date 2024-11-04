
shbytes_tuple = ('Python', 'AWS', 'Java', 'Azure')

# addition to tuple - using append function - AttributeError
print("addition to tuple - using append function - AttributeError")
print(shbytes_tuple)
# shbytes_tuple.append('Machine Learning')
try:
	shbytes_tuple.append('Machine Learning')
except AttributeError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

# addition to tuple - by converting it to list
print("addition to tuple - by converting it to list")
print(shbytes_tuple)
temp_list = list(shbytes_tuple)
temp_list.append("Machine Learning")
new_tuple = tuple(temp_list)
print(new_tuple)

print("\n---------------------------------------------------\n")

# append in mutable elements in nested tuple
print("append in mutable elements in nested tuple")
nested_tuple = ('Python', 'AWS', 'Azure', [1, 2, 3])
print("original nested tuple", nested_tuple)
nested_tuple[3].append(4)
print("changed nested tuple", nested_tuple)

print("\n---------------------------------------------------\n")
original_tuple = (14, 24, 34)

# Appending multiple elements (4, 5) by creating a new tuple
new_tuple = original_tuple + (44, 54)
print(new_tuple)   # elements in new_tuple = (14, 24, 34, 44, 54)
