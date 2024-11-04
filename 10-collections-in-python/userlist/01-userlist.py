# Declaring UserList()
# class collections.UserList([list])
# wrapper around list objects for easier list subclassing

from collections import UserList

# create empty UserList list
print("create empty UserList list")
userlist_empty_list = UserList()    # Create empty UserList object
print(userlist_empty_list)          # Elements in UserList object
print(type(userlist_empty_list))    # Class type of UserList object

print("\n---------------------------------------------------\n")

# create UserList list with initialized data
print("create UserList list with initialized data")
course_list = ['AWS','Python','ML','DevOps']
userlist_course_list = UserList(course_list) # UserList object with initial list
print(userlist_course_list)      # Elements in UserList object
print(userlist_course_list.data) # data attribute on UserList object
