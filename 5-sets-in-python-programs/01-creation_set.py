# Creation of set
# Declaration and Initialization of set

# empty set creation with set constructor
print("empty set creation with set constructor")
empty_set = set()							# empty set
print(empty_set)
print(type(empty_set))

print("\n---------------------------------------------------\n")

# set creation with curly brackets
print("set creation with curly brackets")
boolean_set = {True, False, True, True}				# set of boolean
print(boolean_set)
print(type(boolean_set))

print("\n---------------------------------------------------\n")

# set creation with curly brackets
print("set creation with curly brackets")
string_set = {'Python','Java','AWS','Azure'}		# set of string
print(string_set)
print(type(string_set))

print("\n---------------------------------------------------\n")

# set creation with set constructor
print("set creation with set constructor")
set_from_list = set(['Python','Java','AWS','Azure'])	# set from list with set constructor
print(set_from_list)
print(type(set_from_list))

set_from_tuple = set(('Python','Java','AWS','Azure'))	# set from tuple with set constructor
print(set_from_tuple)
print(type(set_from_tuple))

print("\n---------------------------------------------------\n")

# set not allows duplicate elements
print("set not allows duplicate elements")
no_duplicate_set = {"Python","Java","AWS","Azure","AWS", "aws"}
print(no_duplicate_set)
print(type(no_duplicate_set))

print("\n---------------------------------------------------\n")

# frozenset with frozenset constructor
print("frozenset with frozenset constructor")
frozen_set = frozenset(["Python","Java","AWS","Azure"])
print(frozen_set)
print(type(frozen_set))

print("\n---------------------------------------------------\n")
#mutable_element_set = {1, 2, [3, 4]}  # This will raise an error

print("\n---------------------------------------------------\n")
course_list = ['Python','Java','AWS','Azure']
course_set = set(course_list)
print(course_set)

course_tuple = ('Python','Java','AWS','Azure')
course_set = set(course_tuple)
print(course_set)
print("\n---------------------------------------------------\n")
