# Declaring OrderedDict()
# class collections.OrderedDict([items])
# dict subclass that remembers the order entries were added

from collections import OrderedDict

# check for OrderedDict as subclass of dict
print("check for OrderedDict as subclass of dict")
print(issubclass(OrderedDict, dict))

print("\n---------------------------------------------------\n")

# create empty OrderedDict
print("create empty OrderedDict")
empty_odict = OrderedDict()
print(empty_odict)
print(type(empty_odict))

print("\n---------------------------------------------------\n")

# create OrderedDict from dictionary
print("create OrderedDict from dictionary")
courses_odict = OrderedDict({1:"AWS", 2:"Python", 3:"DevOps"}) 
print(courses_odict)
print(type(courses_odict))

print("\n---------------------------------------------------\n")

# create OrderedDict using fromkeys() method
print("create OrderedDict using fromkeys() method")
fromkeys_odict = OrderedDict.fromkeys("shbytes")
print(fromkeys_odict)
print(type(fromkeys_odict))

print("\n---------------------------------------------------\n")

# compare OrderedDict and dict
print("compare dictionary")
print({1:"AWS", 2:"Python"} == {1:"AWS", 2:"Python"})

print("compare OrderedDict")
courses1_odict = OrderedDict({1:"AWS", 2:"Python"}) 
courses2_odict = OrderedDict({1:"AWS", 2:"Python"}) 
print(courses1_odict==courses2_odict)
