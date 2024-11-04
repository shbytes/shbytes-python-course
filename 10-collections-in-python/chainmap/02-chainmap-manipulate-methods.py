# class collections.ChainMap(*maps)
# ChainMap - collection of dictionaries

from collections import ChainMap

# maps - returns list of maps in ChainMap
print("maps - returns list of maps in ChainMap")
training_dict = {"1": "shbytes", "2": "Online", "3": "Training"}
courses_dict = {"c1": "Python", "c2": "AWS", "c3": "Azure"}
shbytes_chain_map = ChainMap(training_dict, courses_dict)
print(shbytes_chain_map)
print(shbytes_chain_map.maps)

print("\n---------------------------------------------------\n")

# new_child() - add new empty child map at front of ChainMap
print("new_child() - add new empty child map at front of ChainMap")
from collections import ChainMap
training_dict = {"1": "shbytes", "2": "Online", "3": "Training"}
courses_dict = {"c1": "Python", "c2": "AWS", "c3": "Azure"}
shbytes_chain_map = ChainMap(training_dict, courses_dict)
print(shbytes_chain_map)
new_shbytes_chain_map = shbytes_chain_map.new_child()
print(new_shbytes_chain_map)

print("\n---------------------------------------------------\n")

#new_child(map) - add dictionary as new child map at front of ChainMap
print("new_child(map) - add dictionary as new child map at front of ChainMap")
from collections import ChainMap
training_dict = {"1":"shbytes","2":"Online","3":"Training"}
courses_dict = {"c1":"Python","c2":"AWS","c3":"Azure"}
shbytes_chainmap = ChainMap(training_dict, courses_dict)
print(shbytes_chainmap)
level_shbytes_chainmap = shbytes_chainmap.new_child({"l1":"intermediate","l2":"expert"})
print(level_shbytes_chainmap)

print("\n---------------------------------------------------\n")

#parents
#return new ChainMap containing all of the maps in current instance except the first one
print("return new ChainMap containing all of the maps in current instance except the first one")
from collections import ChainMap
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {3: 'c', 4: 'd'}
dict_3 = {5: 'e', 6: 'f'}
shbytes_chainmap = ChainMap(dict_1, dict_2, dict_3)
print(shbytes_chainmap)
parent_shbytes_chainmap = shbytes_chainmap.parents
print(parent_shbytes_chainmap)
