# class collections.UserDict([initialdata])
# wrapper around dictionary objects for easier dict subclassing
# UserDict demonstration using a program

from collections import UserDict

print("UserDict demonstration using a program")
class Courses(UserDict):     # Class created with UserDict
	def upsertCourse(self, key, course):
		self.data[key] = course
	
	def removeCourse(self, key):
		raise RuntimeError("remove of course is not allowed")


# main code to create object of class
shbytes_courses = Courses({1:"Python", 2:"AWS", 3:"Azure"}) # Courses object with dictionary elements
print("Initial courses list - ", shbytes_courses.data)      # Elements in Courses object

print("\n---------------------------------------------------\n")

# add course
shbytes_courses.upsertCourse(4, "DevOps")      # Add key-value in Courses object
print("Courses after addition - ", shbytes_courses.data)   # Elements after adding key-value

print("\n---------------------------------------------------\n")

# update course
shbytes_courses.upsertCourse(4, "ML")         # Update key-value in Courses object
print("Courses after update - ", shbytes_courses.data)    # Elements after updating key-value

print("\n---------------------------------------------------\n")

# remove course
try:
	shbytes_courses.removeCourse(4)   # Try removing element with key from Courses object
except RuntimeError as err:           # removeCourse() raise RuntimeError
	print("error", err)
print("Courses after remove - ", shbytes_courses.data) # Elements after trying removing key
