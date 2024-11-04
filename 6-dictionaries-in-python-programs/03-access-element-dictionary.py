shbytes = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}

# access element using key
print("access element using key")
print(shbytes)
print("value at key c2 - ", shbytes["c2"])
# print("value at key c5 - ", shbytes["c5"])

print("\n---------------------------------------------------\n")

# access element using get method with key
print("access element using get method with key")
print(shbytes)
print("value at key c1 - ", shbytes.get("c1"))
print("value at key c5 - ", shbytes.get("c5"))

print("\n---------------------------------------------------\n")	

# get all keys of dictionary using key() method
print("get all keys of dictionary using key() method")
print(shbytes)
print("All keys in dictionary - ", shbytes.keys())
print(type(shbytes.keys()))

print("\n---------------------------------------------------\n")

# get all values of dictionary using values() method
print("get all values of dictionary using values() method")
print(shbytes)
print("All values in dictionary - ", shbytes.values())
print(type(shbytes.values()))

print("\n---------------------------------------------------\n")

# get all items of dictionary using items() method
print("get all items of dictionary using items() method")
print(shbytes)
print("All items in dictionary - ", shbytes.items())
print(type(shbytes.items()))


# Nested dictionary
print("Access items in nested dictionary")
courses = {
    "CS": {"topics": ["Algorithms", "Data Structures", "Programming Basics"]},
    "MATH": {"topics": ["Integrals", "Series", "Differential Equations"]},
    "ENG": {"topics": ["Poetry", "Prose", "Drama"]}
}
print(courses)
print("Math topics in dictionary - ", courses["MATH"]["topics"])

print("\n---------------------------------------------------\n")

# check for a key in dictionary
print("check for a key in dictionary")
print(shbytes)
if "c3" in shbytes:
    print("c3 key is in the dictionary")
if "c5" not in shbytes:
    print("c5 key is not in the dictionary")

print("\n---------------------------------------------------\n")

# access elements in nested dictionary
print("access elements in nested dictionary")
nested_dict = {"courses": {"c1": "Python", "c2": "AWS"}}
print(nested_dict)
print(nested_dict["courses"]["c1"])

print("\n---------------------------------------------------\n")

shbytes = {"c1": "Python", "c2": "Java"}

for key in shbytes.keys():
    print(f"{key}",)

for value in shbytes.values():
    print(f"{value} ")

for key, value in shbytes.items():
    print(f"{key}: {value}")

print("\n---------------------------------------------------\n")
def dictionary_deep_update(nested_dict, keys_list, value):
    for key in keys_list[:-1]:
        nested_dict = nested_dict.setdefault(key, {})
    nested_dict[keys_list[-1]] = value

nested_dict = {}
dictionary_deep_update(nested_dict, ["a", "b", "c", "d"], 82)
print(nested_dict)
# nested_dict elements {'a': {'b': {'c': {'d': 82}}}}

print("\n---------------------------------------------------\n")
courses_dict = {"c1": "Python", "c2": "AWS", "c3": "Power BI", "c4": "Java"}
keys_list = ["c1", "c3"]

subset_dict = {key: courses_dict[key] for key in keys_list if key in courses_dict}
print(subset_dict)
# Elements in subset_dict => {'c1': 'Python', 'c3': 'Power BI'}

print("\n---------------------------------------------------\n")
from operator import itemgetter

courses_dict = {"c1": "Python", "c2": "AWS", "c3": "Power BI", "c4": "Java"}
keys_list = ["c1", "c3"]
values_tuple = itemgetter(*keys_list)(courses_dict)
print(values_tuple)
# Elements in values_tuple => ('Python', 'Power BI')

print("\n---------------------------------------------------\n")
numbers_dict = {"a": 11, "b": 22, "c": 33}

# Increment all values by 2
incremented_dict = dict(map(lambda item: (item[0], item[1] + 2), numbers_dict.items()))
print(incremented_dict)
# Elements in incremented_dict => {'a': 13, 'b': 24, 'c': 35}

numbers_dict = {"a": 11, "b": 22, "c": 33}
# Filter out items where the value is greater than 20
filtered_dict = dict(filter(lambda item: item[1] > 20, numbers_dict.items()))
print(filtered_dict)
# Elements in filtered_dict => {'b': 22, 'c': 33}
