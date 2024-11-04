# Declaring UserDict()
# class collections.UserDict([initialdata])
# wrapper around dictionary objects for easier dict subclassing

from collections import UserDict

# create empty UserDict dictionary
print("create empty UserDict dictionary")
userdict_empty_dict = UserDict()  # Create empty UserDict object
print(userdict_empty_dict)        # Elements in UserDict object
print(type(userdict_empty_dict))  # Class type of UserDict object

print("\n---------------------------------------------------\n")

# access data from the UserDict dictionary
print("access data from the UserDict dictionary")
course_dict = {'c1':'AWS','c2':'Python','c3':'ML'}
userdict_course_dict = UserDict(course_dict) # UserDict object with initial dictionary
print(userdict_course_dict)                  # Elements in UserDict object
print(userdict_course_dict.data)             # data attribute on UserDict object
