# Object-Oriented Programming (OOP) in Python
# Class is a user-defined prototype or a blueprint for an object
# defines set of attributes that characterize any object of class
# attributes are data members (class variables and instance variables) and methods
# attributes are accessed via dot notation


# syntax of class creation
print("syntax of class creation")
# class ClassName:
# 	"""class documentation string is optional"""
# 	class_attributes, variables, functions

print("\n---------------------------------------------------\n")

# Definition of class
print("Definition of class")
class Shbytes:                                         # define a class with name Shbytes
	"""Online training in various IT courses"""        # docstring for the Shbytes class

	# class level variable
	course_count = 0                                    # class level variable
	
	# __init__() is the constructor of the class
	def __init__(self, course_name, course_duration):  # initialize function for Shbytes class
		self.course_name = course_name             # course_name is Shbytes class attribute
		self.course_duration = course_duration     # course_duration is Shbytes class attribute
		Shbytes.course_count += 1                   # course_count is Shbytes class level variable
		self.course_id = "C" + str(Shbytes.course_count) # course_id is Shbytes class attribute
	
	# class functions, but first argument is self
	def totalCourses(self):                            # user-defined function in Shbytes class
		print("Total Courses - ", Shbytes.course_count)

	def courseDetails(self):                           # user-defined function in Shbytes class
		print("course id - ", self.course_id)
		print("course name - ", self.course_name)
		print("course duration - ", self.course_duration)

print("\n---------------------------------------------------\n")		

# create object & instance of the class, with instance referring to object
print("create object & instance of the class, with instance referring to object")
shbytes1 = Shbytes("AWS", 50)     # shbytes1 is an instance of Shbytes class
shbytes2 = Shbytes("Python", 50)  # shbytes2 is second instance of Shbytes class
shbytes3 = Shbytes("ML", 60)      # shbytes3 is third instance of Shbytes class

print("\n---------------------------------------------------\n")

# access attributes (class variable & functions) of a class
print("access attributes (class variable & functions) of a class")

print("details of first course")
shbytes1.courseDetails()           # call courseDetails() using shbytes1 instance

print("\n---------------------------------------------------\n")

print("details of second course")
shbytes2.courseDetails()           # call courseDetails() using shbytes2 instance

print("\n---------------------------------------------------\n")

print("total number of courses")
shbytes2.totalCourses()            # call totalCourses() using shbytes2 instance
