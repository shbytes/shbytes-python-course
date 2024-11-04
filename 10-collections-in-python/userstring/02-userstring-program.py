# class collections.UserString(seq)
# wrapper around string objects for easier string subclassing
# UserString demonstration using a program - to create mutable string

from collections import UserString

print("program to create mutable string")
class Courses(UserString):       # Class created with UserString
	def addCourse(self, course):
		self.data += course
	
	def updateCourse(self, course1, course2):
		self.data = self.data.replace(course1, course2)
	
	def removeCourse(self, course):
		self.data = self.data.replace(course, "")

		
# main code to create object of class
shbytes_courses = Courses("Python,AWS,DevOps,ML,Azure") # Courses object with string sequence
print("Initial courses - ", shbytes_courses.data) # Elements in Courses object

print("\n---------------------------------------------------\n")

# add course for shbytes
shbytes_courses.addCourse("HTML") # Add element in Courses object
print("Courses after addition - ", shbytes_courses.data) # Elements in Courses object after adding string

print("\n---------------------------------------------------\n")

# update course for shbytes
shbytes_courses.updateCourse("HTML", "PHP") # Update element in Courses object
print("Courses after update - ", shbytes_courses.data) # Elements in Courses object after updating string

print("\n---------------------------------------------------\n")

# remove course for shbytes
shbytes_courses.removeCourse("PHP") # Remove element in Courses object
print("Courses after remove - ", shbytes_courses.data) # Elements in Courses object after removing string
