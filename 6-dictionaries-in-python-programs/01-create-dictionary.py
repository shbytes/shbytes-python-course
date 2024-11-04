# Creation of dictionary
# Declaration and Initialization of dictionary

# empty dictionary with curly brackets
print("empty dictionary creation with curly brackets")
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

print("\n---------------------------------------------------\n")

# dictionary with curly brackets
print("dictionary creation with curly brackets")
training_dict = {"1": "ShBytes", "2": "Online", "3": "Training"}
print(training_dict)
print(type(training_dict))

print("\n---------------------------------------------------\n")

# dictionary with dict constructor
print("dictionary creation with dict constructor")
courses_dict = dict({"c1": "Python", "c2": "AWS", "c3": "Azure"})
print(courses_dict)
print(type(courses_dict))

print("\n---------------------------------------------------\n")

# dictionary of dictionaries
print("dictionary of dictionaries")
nested_dict = {"courses": {"c1": "Python", "c2": "AWS"}}
print(nested_dict)
print(type(nested_dict))

print("\n---------------------------------------------------\n")

# dictionary key of immutable datatype
print("dictionary key of immutable datatype")
string_key_dict = {"courses": ["Python", "Java"], "numbers": (1, 2, 3)}
print(string_key_dict)
print(type(string_key_dict))

number_key_dict = {10: ["NumPy", "Pandas"], 20: {"ML", "AI"}}
print(number_key_dict)
print(type(number_key_dict))

tuple_key_dict = {(10, 20): {"NumPy", "Pandas", "AI", "ML"}}
print(tuple_key_dict)
print(type(tuple_key_dict))


# dictionary of mixed collections
print("dictionary of mixed collections")
mixed_dict = {"courses": ["Python", "AWS"], "numbers": (1, 2, 3)}
print(mixed_dict)
print(type(mixed_dict))

print("\n---------------------------------------------------\n")

# dictionary from sequence with each item as pair
print("dictionary from sequence with each item as pair")
pair_dict = dict([(1, 'AWS'), (2, 'Python')])
print(pair_dict)
print(type(pair_dict))

print("\n---------------------------------------------------\n")

# dictionary using zip
print("dictionary using zip")
zip_dict = dict(zip([1, 2, 3], ['AWS', 'Python', 'Azure']))
print(zip_dict)
print(type(zip_dict))

print("\n---------------------------------------------------\n")

# dictionary does not allow duplicate keys
print("dictionary does not allow duplicate keys")
duplicate_key_dict = {1: 'AWS', 1: 'Python'}
print(duplicate_key_dict)
print(type(duplicate_key_dict))

print("\n---------------------------------------------------\n")

# dictionary using for loop
print("dictionary using for loop")
for_dict = {x: x**2 for x in (1, 2, 3)}
print(for_dict)
print(type(for_dict))

# Error - dictionary key of mutable datatype
print("Error - dictionary key of mutable datatype")
#list_key_dict = {[10, 20]: {"NumPy", "Pandas", "AI", "ML"}}
#print(list_key_dict)

print("\n---------------------------------------------------\n")
courses_dict = {"c1": "Python", "c2": "NumPy", "c3": "Pandas", "c4": "Java"}
numbers_dict = {1: 2, 2: 4, 3: 9, 4: 16}

updated_dict_1 = {**courses_dict, **numbers_dict}  # Creates a new dictionary with merged key-value pairs
print(updated_dict_1)
# {'c1': 'Python', 'c2': 'NumPy', 'c3': 'Pandas', 'c4': 'Java', 1: 2, 2: 4, 3: 9, 4: 16}

updated_dict_2 = courses_dict | numbers_dict  # Creates a new dictionary with merged key-value pairs
print(updated_dict_2)
# {'c1': 'Python', 'c2': 'NumPy', 'c3': 'Pandas', 'c4': 'Java', 1: 2, 2: 4, 3: 9, 4: 16}

courses_dict.update(numbers_dict)
print(courses_dict)
# {'c1': 'Python', 'c2': 'NumPy', 'c3': 'Pandas', 'c4': 'Java', 1: 2, 2: 4, 3: 9, 4: 16}


