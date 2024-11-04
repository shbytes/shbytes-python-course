
shbytes_tuple = ('Python', 'AWS', 'Java', 'Azure', 'Machine Learning')

# remove elements from tuple - using remove function
print("remove elements from tuple - using remove function")
print(shbytes_tuple)
# shbytes_tuple.remove('Java')
try:
	shbytes_tuple.remove('Java')
except AttributeError as err:
	print("error", err)
	print(shbytes_tuple)

print("\n---------------------------------------------------\n")

# remove elements from tuple - by converting it to list
print("remove elements from tuple - by converting it to list")
print(shbytes_tuple)
temp_list = list(shbytes_tuple)
temp_list.remove("Java")
new_tuple = tuple(temp_list)
print(new_tuple)

print("\n---------------------------------------------------\n")

# remove in mutable elements in tuple
print("remove in mutable elements in tuple")
nested_tuple = ('Python', 'AWS', 'Azure', [1, 2, 3])
print("original nested tuple", nested_tuple)
nested_tuple[3].remove(2)
print("changed mixed tuple", nested_tuple)

print("\n---------------------------------------------------\n")

# Error - Case-sensitive element not in tuple
shbytes_tuple = ('Python', 'AWS', 'JAVA', 'Azure', 'Machine Learning')
print(shbytes_tuple)
temp_list = list(shbytes_tuple)
# temp_list.remove("java")
new_tuple = tuple(temp_list)


# Error - element not in tuple
# shbytes_tuple = ('Python', 'AWS', 'JAVA', 'Azure', 'Machine Learning')
# print(shbytes_tuple)
# temp_list = list(shbytes_tuple)
# temp_list.remove("GoLang")
# new_tuple = tuple(temp_list)

print("\n---------------------------------------------------\n")

del new_tuple
# print(new_tuple) 	#raise an error, new_tuple no longer exists

print("\n---------------------------------------------------\n")
numbers_tuple = (14, 26, 38, 42, 54, 64, 78)   # Original tuple
elements_to_remove = {38, 54, 78}   # Elements to remove from tuple

# Convert tuple to list and filter out the elements
new_list = [item for item in numbers_tuple if item not in elements_to_remove]
new_tuple = tuple(new_list)  # Convert list back to tuple
print(new_tuple)  # Element in new_tuple => (14, 26, 42, 64)

print("\n---------------------------------------------------\n")
def remove_tuple_element(tuple_obj, value):
	temp_list = list(tuple_obj)  # Convert tuple to list

	if value in temp_list:
		temp_list.remove(value)  # Remove element from list if it exists

	return tuple(temp_list)      # Convert list back to tuple

# Test the function
original_tuple = (16, 42, 34, 42, 51)
new_tuple = remove_tuple_element(original_tuple, 42)
print(new_tuple)  # Elements in new_tuple => (16, 34, 42, 51)

print("\n---------------------------------------------------\n")
def remove_tuple_element_by_index(tuple_obj, index):
	if index < 0 or index >= len(tuple_obj):
		raise IndexError("Index out of range")

	# Return a new tuple with the element at the index removed
	return tuple_obj[:index] + tuple_obj[index + 1:]

# Test the function
original_tuple = (16, 42, 34, 42, 51)
new_tuple = remove_tuple_element_by_index(original_tuple, 1)
print(new_tuple)  # Elements in new_tuple => (16, 34, 42, 51)
