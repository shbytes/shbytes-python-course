# Object-Oriented Programming (OOP) in Python
# Class is a user-defined prototype or a blueprint for an object
# defines set of attributes that characterize any object of class
# attributes are data members (class variables and instance variables) and methods
# attributes are accessed via dot notation

# Definition of class
print("Definition of class")
class Shbytes:
	"""Online training in various IT courses"""
	
	# class level variable
	courseCount = 0
	
	# __init__() is the constructor of the class
	def __init__(self, course_name, course_duration):
		self.course_name = course_name
		self.course_duration = course_duration
		Shbytes.courseCount += 1
		self.course_id = "C" + str(Shbytes.courseCount)
	
	# class functions, but first argument is self
	def totalCourses(self):
		print("Total Courses - ", Shbytes.courseCount)

	def courseDetails(self):
		print("course id - ", self.course_id)
		print("course name - ", self.course_name)
		print("course duration - ", self.course_duration)
	def __del__(self):
		class_name = self.__class__.__name__
		print (id(self))
		print("object of class", class_name, "is destroyed")

print("\n---------------------------------------------------\n")		

# create object & instance of the class, with instance referring to object
print("create object & instance of the class, with instance referring to object")
shbytes1 = Shbytes("AWS", 50)
shbytes2 = Shbytes("Python", 50)
shbytes3 = Shbytes("ML", 60)

print("\n---------------------------------------------------\n")

# delete object of a class
print("delete object of a class")
del shbytes3

print("\n---------------------------------------------------\n")

shbytes1.courseDetails()
shbytes2.courseDetails()

try:
	shbytes3.courseDetails() # shbytes3 object does not exists raise NameError
except NameError as err:     # catch NameError
	print("error", err)

print("\n---------------------------------------------------\n")