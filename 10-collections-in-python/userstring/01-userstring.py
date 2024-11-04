# Declaring UserString()
# class collections.UserString(seq)
# wrapper around string objects for easier string subclassing

from collections import UserString

# create empty UserString string
print("create empty UserString string")
userstring_empty = UserString("")  # Create empty UserString object
print(userstring_empty)            # Elements in UserString object
print(type(userstring_empty))      # Class type of UserString object

print("\n---------------------------------------------------\n")

# create UserString string with initialized data
print("create UserString string with initialized data")
courses = "AWS,Python,ML"
userstring_courses = UserString(courses) # UserString object with initial string elements
print(userstring_courses)                # Elements in UserString object
print(userstring_courses.data)           # data attribute on UserString object
