
courses = {'Python','AWS','Java','Azure','ML'}

# addition to set - using add method
print("addition to set - using add method")
print(courses)
courses.add('PHP')
courses.add(15)
courses.add(True)
courses.add(12.55)
print(courses)

print("\n---------------------------------------------------\n")

# try adding duplicate element to set
print("try adding duplicate element to set")
courses = {'Python', 'AWS', 'Java', 'Azure', 'ML', 'PHP'}
print(courses)
courses.add('PHP')
print(courses)
print("no addition of duplicate element")

print("\n---------------------------------------------------\n")

# addition of tuple to set - using add method
print("addition of tuple to set - using add method")
courses = {'Python','AWS','Java','Azure','ML'}
print(courses)
tuple = ('PHP', 'MongoDB')
courses.add(tuple)
print(courses)

print("\n---------------------------------------------------\n")

# Error while adding list to set - using add method
print("Error while adding list to set - using add method")
courses = {'Python','AWS','Java','Azure','ML'}
print(courses)
course_list = ['PHP', 'MongoDB']
# courses.add(course_list)
try:
	courses.add(course_list)
except TypeError as err:
	print("error", err)
	print(courses)

print("\n---------------------------------------------------\n")

# addition of tuple elements to set - using update method
print("addition of tuple elements to set - using update method")
courses = {'Python','AWS','Java','Azure','ML'}
print(courses)
tuple = ('PHP', 'MongoDB')
courses.update(tuple)
print(courses)

print("\n---------------------------------------------------\n")

# addition of list elements to set - using update method
print("addition of list elements to set - using update method")
courses = {'Python','AWS','Java','Azure','ML'}
print(courses)
course_list = ['PHP', 'MongoDB']
courses.update(course_list)
print(courses)

