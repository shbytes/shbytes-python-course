# collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

from collections import namedtuple

# Scenario 1 - namedtuple elements can be accessed with field name
print("namedtuple elements can be accessed with field name")
shbytes_class = namedtuple('shbytes',['c1','c2','c3'])
o = shbytes_class('AWS','Python','DevOps')
print("c1 - ", o.c1)
print("c2 - ", o.c2)
print("c3 - ", o.c3)

print("\n---------------------------------------------------\n")

# Scenario 2 - namedtuple elements can be accessed with index
print("namedtuple elements can be accessed with index")
shbytes_class = namedtuple('shbytes',['c1','c2','c3'])
o = shbytes_class('AWS','Python','DevOps')
print("c1 - ", o[0])
print("c2 - ", o[1])
print("c3 - ", o[2])

print("\n---------------------------------------------------\n")

# Scenario 3 - namedtuple elements can be unpacked like tuple
print("namedtuple elements can be unpacked like tuple")
shbytes_class = namedtuple('shbytes',['c1','c2','c3'])
o = shbytes_class('AWS','Python','DevOps')
l, m, n = o
print(l, m, n)

print("\n---------------------------------------------------\n")
# getattr(namedtuple, variable) - to get value for an attribute
print("getattr(namedtuple, variable) - to get value for an attribute")
shbytes_class = namedtuple('shbytes',['c1','c2','c3'])
o = shbytes_class('Python', 'AWS', 'Power BI')
value_c1 = getattr(o, 'c1')
print(value_c1)
print(getattr(o, 'c2'))
print(getattr(o, 'c3'))