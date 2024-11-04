# Declaring ChainMap()
# class collections.ChainMap(*maps)
# ChainMap - collection of dictionaries

from collections import ChainMap

# create empty ChainMap
print("create empty ChainMap")
empty_chain_map = ChainMap()
print(empty_chain_map)
print(type(empty_chain_map))

print("\n---------------------------------------------------\n")

# Chainmap object with dictionaries
print("Chainmap object with dictionaries")
training_dict = {"1": "Shbytes", "2": "Online", "3": "Training"}
courses_dict = {"c1": "Python", "c2": "AWS", "c3": "Azure"}
dicts_chain_map = ChainMap(training_dict, courses_dict)
print(dicts_chain_map)
print(type(dicts_chain_map))

print("\n---------------------------------------------------\n")
