#Declaring namedtuple()
#collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

from collections import namedtuple

# create named tuple with default settings
print("create named tuple with default settings")
namedtuple_class = namedtuple('shbytes',['c1','c2','c3']) # field names passed as list
o = namedtuple_class('AWS','Python','DevOps')   # create object from namedtuple class and assign values to fields
print(o)
print(type(o))

# create named tuple with field names passed with space separated
print("create named tuple with field names passed with space separated")
shbytes_class = namedtuple('shbytes',"c1 c2 c3") # field names passed with space separated
o = shbytes_class('AWS','Python','DevOps')     # create object from namedtuple class and assign values to fields
print(o)
print(type(o))

print("\n---------------------------------------------------\n")

# create named tuple with field names cannot start with underscore
print("create named tuple with field names cannot start with underscore")
try:
	shbytes = namedtuple('shbytes',['_c1', '_c2']) # field names start with underscore not allowed
except ValueError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

#named tuple - invalid field names
print("named tuple - invalid field names")
from collections import namedtuple
try:
	shbytes = namedtuple('shbytes',['c1', 'def', 'c1']) 
except ValueError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

from collections import namedtuple

# invalid field names are replaced with positional name
print("invalid field names are replaced with positional name")
shbytes_class = namedtuple('shbytes',['_c1', '_c2'], rename=True)
o = shbytes_class('Python','Power BI')
print(o)
print(type(o))

# invalid field names are replaced with positional names
print("named tuple - invalid field names are replaced with positional names")
shbytes_class = namedtuple('shbytes',['c1','def','c1'], rename=True)
o = shbytes_class('AWS','Python','Power BI')
print(o)
print(type(o))

print("\n---------------------------------------------------\n")

from collections import namedtuple

# Scenario 1 - named tuple - default value applied to right most parameters
print("named tuple - default value applied to right most parameters")
shbytes_class = namedtuple('shbytes',['c1','c1','c2'], rename=True, defaults=('Python','Power BI'))
o = shbytes_class('AWS')
print(o)
print(type(o))

print("\n---------------------------------------------------\n")

# Scenario 2 - named tuple - default value is ignored if no parameter left to assign
print("named tuple - default value applied to right most parameters")
shbytes_class = namedtuple('shbytes',['c1','c1','def'], rename=True, defaults=('Python', 'Azure',))
o = shbytes_class('AWS', 'Power BI')
print(o)
print(type(o))

# Scenario 3 - named tuple - Total count of values and default values is less than field names
print("named tuple - Total count of values and default values is less than field names")
try:
	shbytes_class = namedtuple('shbytes', ['c1', 'c1', 'def'], rename=True, defaults=('Python',))
	o = shbytes_class('Power BI')
except TypeError as err:
	print("error", err)

# Scenario 4 - named tuple - more values than field names
print("named tuple - more values than field names")
try:
	shbytes_class = namedtuple('shbytes', ['c1', 'c1', 'def'], rename=True)
	o = shbytes_class('AWS', 'DevOps', 'Python', 'Power BI')
except TypeError as err:
	print("error", err)

#if module is defined, the __module__ attribute of the named tuple is set to that value.