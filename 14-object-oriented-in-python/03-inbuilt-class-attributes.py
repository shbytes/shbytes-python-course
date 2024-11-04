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

print("\n---------------------------------------------------\n")		

# create object & instance of the class, with instance referring to object
print("create object & instance of the class, with instance referring to object")
shbytes1 = Shbytes("AWS", 50)
shbytes2 = Shbytes("Python", 50)
shbytes3 = Shbytes("ML", 60)

print("\n---------------------------------------------------\n")

# __dict__ - gives dictionary containing class namespace
print ("shbytes.__dict__ - ", Shbytes.__dict__)      # dictionary of Shbytes class namespace

print("\n---------------------------------------------------\n")

# __doc__ - gives class documentation string or none, if undefined
print ("shbytes.__doc__ - ", Shbytes.__doc__)       # Shbytes class documentation string

print("\n---------------------------------------------------\n")

# __name__ - gives class name
print ("shbytes.__name__ - ", Shbytes.__name__)     # Shbytes class name

print("\n---------------------------------------------------\n")

# __module__ - gives module name in which this class is defined
# This attribute is __main__ in interactive mode
print ("shbytes.__module__ - ", Shbytes.__module__) # Shbytes class module name

print("\n---------------------------------------------------\n")

# __bases__ - possibly empty tuple containing the base classes, in the order of their occurrence in the base class list
print ("shbytes.__bases__ - ", Shbytes.__bases__)   # tuple for Shbytes class base classes