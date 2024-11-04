# Declaring OrderedDict()
# class collections.OrderedDict([items])

from collections import OrderedDict

# move_to_end(key, last=True) (default is True)
# Scenario 1 - move an existing key to right end of an ordered dictionary, if last is True (the default)
print("move an existing key to right end of an ordered dictionary, if last is True (the default)")
courses_odict = OrderedDict({1:"AWS", 2:"Python", 3:"DevOps"})
print(courses_odict)         # Original order of elements
courses_odict.move_to_end(2) # default value for last=True
print(courses_odict)         # Order of elements after moving key element to right end

print("\n---------------------------------------------------\n")

# move_to_end(key, last=False) (default is True)
# Scenario 2 - move an existing key to left end of an ordered dictionary, if last is False
print("move an existing key to left end of an ordered dictionary, if last is False")
courses_odict = OrderedDict({1:"AWS", 2:"Python", 3:"DevOps"})
print(courses_odict)                         # Original order of elements
courses_odict.move_to_end(2, False) # last=False, key element move to left end
print(courses_odict)                         # Order of elements after moving key element to left end

print("\n---------------------------------------------------\n")

# Scenario 3 - raises KeyError if the key does not exist
print("raises KeyError if the key does not exist")
courses_odict = OrderedDict({1:"AWS", 2:"Python", 3:"DevOps"})
print(courses_odict)
try:
	courses_odict.move_to_end(4) # key 4 does not exist in dictionary
except KeyError as err:          # raise and catch KeyError
	print("error", err)

print("\n---------------------------------------------------\n")

# pop(key)
# take out element with the given key
print("take out element with the given key")
courses_odict = OrderedDict({1:"AWS", 2:"Python", 3:"DevOps"})
print(courses_odict)              # Original elements in dictionary
pop_value = courses_odict.pop(3)  # Pop element with key 3
print(courses_odict)              # Elements after removing element with key 3
print(pop_value)                  # Value for key 3

print("\n---------------------------------------------------\n")

# returns and removes a (key, value) pair, LIFO order if last is true
print("returns and removes a (key, value) pair, LIFO order if last is true")
courses_odict = OrderedDict({1:"AWS", 2:"Python", 3:"DevOps"})
print(courses_odict)                        # Original elements in dictionary
pop_item = courses_odict.popitem(last=True) # Pop last element from right
print(courses_odict)                        # Elements after removing last element from right
print(pop_item)                             # Element taken out

print("\n---------------------------------------------------\n")

# returns and removes a (key, value) pair, FIFO order if last is False
print("returns and removes a (key, value) pair, FIFO order if last is False")
courses_odict = OrderedDict({1:"AWS", 2:"Python", 3:"DevOps"})
print(courses_odict)                         # Original elements in dictionary
pop_item = courses_odict.popitem(last=False) # Pop last element from left
print(courses_odict)                         # Elements after removing last element from left
print(pop_item)                              # Element taken out

print("\n---------------------------------------------------\n")

courses_odict = OrderedDict({'c1':"AWS",'c2':"Python",'c3':"DevOps"})
print(courses_odict)
print(courses_odict.keys())   # Access all keys in order
print(courses_odict.items())  # Access all values in order
print(courses_odict.values()) # Access key-value pairs
print('c4'.join(courses_odict.keys())) # all keys are joined with c4 in between those keys
