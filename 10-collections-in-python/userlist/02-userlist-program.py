# class collections.UserList([list])
# wrapper around list objects for easier list subclassing
# UserList demonstration using a program

from collections import UserList

print("UserList demonstration using a program")
class Courses(UserList):   # Class created with UserList
	def addCourse(self, course):
		self.data.append(course)
	
	def updateCourse(self, course1, course2):
		for index, item in enumerate(self.data):
			if item == course1:
				self.data[index] = course2
	
	def removeCourse(self, course):
		raise RuntimeError("remove of course is not allowed")


# main code to create object of class
shbytes_courses = Courses(["Python","AWS","DevOps","ML","Azure"]) # Courses object with list elements
print("Initial courses - ", shbytes_courses.data) # Elements in Courses object

print("\n---------------------------------------------------\n")

# add course for shbytes
shbytes_courses.addCourse("HTML")  # Add element in Courses object
print("Courses after addition - ", shbytes_courses.data) # Elements in Courses object after adding

print("\n---------------------------------------------------\n")

# update course for shbytes
shbytes_courses.updateCourse("HTML", "PHP") # Update element in Courses object
print("Courses after update - ", shbytes_courses.data) # Elements in Courses object after updating

print("\n---------------------------------------------------\n")

# remove course for shbytes
try:
	shbytes_courses.removeCourse("PHP") # Remove element in Courses object
except RuntimeError as err:
	print("error", err)
print("Courses after remove - ", shbytes_courses.data) # Elements in Courses object after trying removing
