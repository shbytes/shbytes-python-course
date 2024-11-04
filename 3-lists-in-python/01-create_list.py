# Creation of list
# Declaration and Initialization of list

# empty list creation with brackets
empty_list = []
print(empty_list)
print(type(empty_list))

print("\n---------------------------------------------------\n")

# Number list creation with brackets
num_list = [30, 40, 50, 60]						    # list of numbers
print(num_list)
print(type(num_list))

# String list creation with brackets
string_list = ['Python', 'Java', 'AWS', 'Azure']		# list of string
print(string_list)
print(type(string_list))

# Boolean list creation with brackets
boolean_list = [False, True, True, True]		# list of string
print(boolean_list)
print(type(boolean_list))

print("\n---------------------------------------------------\n")

# list creation with list constructor
list_m = list(('Python', 'Java', 'AWS', 'Shbytes'))
print(list_m)
print(type(list_m))

print("\n---------------------------------------------------\n")

# list of lists
nested_list = [['C', 2], [2.4, 3], ['AWS', 6], 4]
print(nested_list)
print(type(nested_list))

print("\n---------------------------------------------------\n")

# list of mixed collections
mixed_list = [1.13, 5, "shbytes", {'Azure': 1}, ['AWS', 2]]
print(mixed_list)
print(type(mixed_list))

print("\n---------------------------------------------------\n")

# list with single element
single_element_list = [5]
print(single_element_list)
print(type(single_element_list))

print("\n---------------------------------------------------\n")

# list allows duplicate elements
duplicate_element_list = ["Python", "Java", "AWS", "Azure", "AWS"]
print(duplicate_element_list)
print(type(duplicate_element_list))
