#class collections.ChainMap(*maps)
#ChainMap - collection of dictionaries

#get all keys, values, items from ChainMap
print("get all keys, values, items from ChainMap")

from collections import ChainMap

dict_1 = {1: 'a', 2: 'b', 3: 'c'}
dict_2 = {3: 'c', 4: 'd', 5: 'e'}
dict_3 = {5: 'e', 6: 'f', 7: 'g'}
shbytes_chainmap = ChainMap(dict_1, dict_2, dict_3)    # created ChainMap object of three dictionaries
print(shbytes_chainmap)

all_keys = shbytes_chainmap.keys()        # Get KeysView from the ChainMap object
print("all keys view in ChainMap - ", all_keys)
print("all keys as list - ", list(all_keys))      # Get all unique keys as list from KeysView
print("all keys as set - ", set(all_keys))      # Get all unique keys as set from KeysView

all_values = shbytes_chainmap.values()   # Get ValuesView from the ChainMap object
print("all values view in ChainMap - ", all_values)
print("all values as list - ", list(all_values))  # Get all unique values as list from ValuesView
print("all values as set - ", set(all_values))  # Get all unique values as set from ValuesView

all_items = shbytes_chainmap.items()   # Get ItemsView from the ChainMap object
print("all items view in ChainMap - ", all_items)
print("all items as list - ", list(all_items))  # Get all unique items as list from ItemsView
print("all items as set - ", set(all_items))  # Get all unique items as set from ItemsView

print("\n---------------------------------------------------\n")

#get value at given key in ChainMap
print("get value at given key in ChainMap")
from collections import ChainMap
dict_1 = {1: 'a', 2: 'b', 3: 'c'}
dict_2 = {3: 'd', 4: 'e', 5: 'dict_2_5'}
dict_3 = {5: 'dict_3_5', 6: 'h', 7: 'i'}
shbytes_chainmap = ChainMap(dict_1, dict_2, dict_3)
print(shbytes_chainmap)

print("value at key 4 - ", shbytes_chainmap.get(4))
print("value at key 5 - ", shbytes_chainmap[5])
print("return None value, when given key not found in ChainMap")
print("value at key 12 - ", shbytes_chainmap.get(12))

print("\n---------------------------------------------------\n")

#fromkeys returns dictionary with the specified keys and value
print("fromkeys returns dictionary with the specified keys and value")
from collections import ChainMap
# training_dict = {"1":"shbytes","2":"Online","3":"Training"}
# courses_dict = {"c1":"Python","c2":"PowerBI","c3":"AWS"}
# shbytes_chainmap = ChainMap(training_dict, courses_dict)
# print(shbytes_chainmap)
new_shbytes_chainmap = ChainMap.fromkeys([3, 'c2','l1','l2'], 'expert')
print(new_shbytes_chainmap)

print("\n---------------------------------------------------\n")

#copy() - returns deep copy
print("copy() - returns deep copy")
from collections import ChainMap
training_dict = {1:"shbytes",2:"Online",3:"Training"}
courses_dict = {"c1":"Python","c2":"PowerBI","c3":"AWS"}
shbytes_chainmap = ChainMap(training_dict, courses_dict) 
print(shbytes_chainmap)
copy_shbytes_chainmap = shbytes_chainmap.copy()
print(copy_shbytes_chainmap)
shbytes_chainmap["c3"] = "LLM"
print(copy_shbytes_chainmap)
print(shbytes_chainmap)

print("\n---------------------------------------------------\n")

#update() - inserts or updates the specified items to the first dictionary of ChainMap
print("update() - inserts or updates the specified items in first dictionary")
from collections import ChainMap
dict_1 = {1: 'a', 2: 'b', 3: 'c'}
dict_2 = {3: 'd', 4: 'e', 5: 'dict_2_5'}
dict_3 = {5: 'dict_3_5', 6: 'h', 7: 'i'}
shbytes_chainmap = ChainMap(dict_1, dict_2, dict_3)
print(shbytes_chainmap)
shbytes_chainmap.update({3:"Learning"})
shbytes_chainmap.update({4:"Training"})
print(shbytes_chainmap)

print("\n---------------------------------------------------\n")

# remove elements from first dictionary of ChainMap
print("remove elements from first dictionary of ChainMap")
from collections import ChainMap
courses_dict = {"c1":"Python","c2":"AWS","c3":"Azure", "c4":"LLM"}
training_dict = {1:"shbytes",2:"Online",3:"Training"}
shbytes_chainmap = ChainMap(courses_dict, training_dict)
print(shbytes_chainmap)
pop_value = shbytes_chainmap.pop("c2")
print(shbytes_chainmap)
print(pop_value)

print("popitem - take out last item with given key from first dictioary in ChainMap")
popitem_element = shbytes_chainmap.popitem()
print(shbytes_chainmap)
print(popitem_element)

del shbytes_chainmap["c3"]
print(shbytes_chainmap)

print("\n---------------------------------------------------\n")
print(shbytes_chainmap.maps)  # Original order: [dict1, dict2, dict3]
shbytes_chainmap.maps = reversed(shbytes_chainmap.maps)
print(ChainMap(shbytes_chainmap.maps))  # Reversed order: [dict3, dict2, dict1]
