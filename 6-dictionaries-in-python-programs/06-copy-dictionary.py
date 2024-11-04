# reference one dictionary with another
print("reference one dictionary with another")
courses = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}
print(courses)
subjects = courses
print(subjects)
subjects["c5"] = "ML"
print(courses)

print("\n---------------------------------------------------\n")

# copy of dictionary using copy() method
print("copy of dictionary using copy() method")
courses = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}
print(courses)
copy_dict = courses.copy()
copy_dict["c5"] = "ML"
print(copy_dict)
print(courses)

print("\n---------------------------------------------------\n")

print("copy of dictionary using copy() method")
dictionary_1 = {'student_1': {'name': 'Johnson'}}
dictionary_2 = dictionary_1.copy()
print(dictionary_2)
dictionary_1["student_2"] = {"name": "Smith"}   # dictionary_1 direct update, will not affect dictionary_2
dictionary_1["student_1"]["name"] = "Harrison"  # nested dictionary update, will affect dictionary_2
print(dictionary_1)
print(dictionary_2)

print("\n---------------------------------------------------\n")

# copy of dictionary using dict() constructor
print("copy of dictionary using dict() constructor")
courses = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}
print(courses)
dict_dict = dict(courses)
dict_dict["c5"] = "ML"
print(dict_dict)
print(courses)

print("\n---------------------------------------------------\n")

print("copy of dictionary using dict() constructor")
dictionary_1 = {'student_1': {'name': 'Johnson'}}
dictionary_2 = dict(dictionary_1)
print(dictionary_2)
dictionary_1["student_2"] = {"name": "Smith"}   # dictionary_1 direct update, will not affect dictionary_2
dictionary_1["student_1"]["name"] = "Harrison"  # nested dictionary update, will affect dictionary_2
print(dictionary_1)
print(dictionary_2)

print("\n---------------------------------------------------\n")
# deep copy of dictionary using copy.deepcopy() method
print("deep copy of dictionary using copy.deepcopy() method")

import copy
dictionary_1 = {'student_1': {'name': 'Johnson'}}
dictionary_2 = copy.deepcopy(dictionary_1)
print(dictionary_2)
dictionary_1["student_2"] = {"name": "Smith"}   # dictionary_1 direct update, will not affect dictionary_2
dictionary_1["student_1"]["name"] = "Harrison"  # nested dictionary update, will not affect dictionary_2
print(dictionary_1)
print(dictionary_2)
