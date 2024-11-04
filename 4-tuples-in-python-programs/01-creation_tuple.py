# Creation of tuple
# Declaration and Initialization of tuple

# empty tuple creation with parentheses
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

print("\n---------------------------------------------------\n")

# tuple creation with parentheses
num_tuple = (30, 40, 50, 60)						    # tuple of numbers
print(num_tuple)
print(type(num_tuple))

print("\n---------------------------------------------------\n")

# tuple creation with parentheses
string_tuple = ('Python', 'Java', 'AWS', 'Azure')		# tuple of string elements
print(string_tuple)
print(type(string_tuple))

# tuple creation with parentheses
boolean_tuple = (False, True, True)		# tuple of boolean elements
print(boolean_tuple)
print(type(boolean_tuple))

print("\n---------------------------------------------------\n")

# tuple creation parentheses are optional
tuple_obj = "AWS", "Azure", "Python"
print(tuple_obj)
print(type(tuple_obj))

print("\n---------------------------------------------------\n")

# tuple creation with tuple constructor
tuple_m = tuple(('Python', 'Java', 'AWS', 'Azure'))
print(tuple_m)
print(type(tuple_m))

print("\n---------------------------------------------------\n")

# tuple of tuples
nested_tuple = (('C', 2), (2.4, 3), ('AWS', 6), 4)
print(nested_tuple)
print(type(nested_tuple))

print("\n---------------------------------------------------\n")

# tuple of nested collections
nested_tuple = (1.13, 5, "shbytes", {'Azure': 1}, ['AWS', 2])
print(nested_tuple)
print(type(nested_tuple))

print("\n---------------------------------------------------\n")

# tuple with single element
single_element_tuple = (5,)
print(single_element_tuple)
print(type(single_element_tuple))

print("\n---------------------------------------------------\n")

# tuple allows duplicate elements
duplicate_element_tuple = ("Python", "Java", "AWS", "Azure", "AWS")
print(duplicate_element_tuple)
print(type(duplicate_element_tuple))

print("\n---------------------------------------------------\n")
number_tuple = ([12, 22, 32], 24)
number_tuple[0].append(44)     # list inside the tuple is modified
# Elements in number_tuple ([12, 22, 32, 44], 24)
print(number_tuple)

print("\n---------------------------------------------------\n")
def get_coordinates():
    return (10, 20)

latitude, longitude = get_coordinates()

print("\n---------------------------------------------------\n")
tuple_dict = {('a', 1): "value1", ('b', 2): "value2"}

