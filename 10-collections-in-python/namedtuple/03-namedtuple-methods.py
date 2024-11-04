#collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

from collections import namedtuple

# Scenario 1 - _make(iterable) - method used on namedtuple object to create another instance
print("_make(iterable) - method used on namedtuple object to create another instance")
Courses = namedtuple('Courses',['c1','c2','c3']) 
course_tuple = Courses('AWS','Python','DevOps')
print(course_tuple)
o = course_tuple._make(course_tuple) # _make used on object
print(o)

# Scenario 2 - _make(iterable) - method used on namedtuple class to create another instance
print("_make(iterable) - method used on namedtuple class to create another instance")
Courses = namedtuple('Courses',['c1','c2','c3']) 
level_tuple = Courses._make(["beginner", "intermediate", "expert"]) # _make used on class
print(level_tuple)

print("\n---------------------------------------------------\n")

from collections import namedtuple

# _asdict() - method returns dictionary with values mapped to named parameters
print("_asdict() - method returns dictionary with values mapped to named parameters")
Courses = namedtuple('Courses',['c1','c2','c3']) 
course_tuple = Courses('AWS','Python','DevOps')
print(course_tuple)                  # namedtuple object
print(type(course_tuple))            # type of namedtuple object
course_dict = course_tuple._asdict() # convert to dictionary
print(course_dict)                   # dictionary object
print(type(course_dict))             # type of dictionary object

print("\n---------------------------------------------------\n")

from collections import namedtuple

# _replace(**kwargs) - method returns a new instance of namedtuple
# replacing the specified fields with new values
print("_replace(**kwargs) - method returns a new instance of namedtuple")

Courses = namedtuple('Courses',['c1','c2','c3']) 
course_tuple = Courses('AWS','Azure','DevOps')
print(course_tuple) # original namedtuple object
replaced_course_tuple = course_tuple._replace(c2='Python',c3='ML') # values replaced using _replace() method
print(replaced_course_tuple) # new object with replaced values
