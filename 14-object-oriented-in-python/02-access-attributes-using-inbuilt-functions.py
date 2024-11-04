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

# validate if object has given attribute
print(hasattr(shbytes1, 'course_name'))  # validate if shbytes1 object has course_name attribute

# get attribute value for the object
print(getattr(shbytes1, 'course_id'))    # get value of course_id attribute for shbytes1 object
print(shbytes1.course_id)                # get value of course_id attribute for shbytes1 object

# set attribute value for the object
setattr(shbytes3, 'course_duration', 70) # set value of course_duration attribute for shbytes3 object

# delete attribute for the object
delattr(shbytes3, 'course_duration')     # delete course_duration attribute for shbytes3 object

try:
	print(getattr(shbytes3, 'course_duration')) # Try accessing attribute after delete
except AttributeError as err:
	print("error", err)


# validate if object has given attribute
print("validate if object has given attribute")
print(hasattr(shbytes1, 'course_name'))

print("\n---------------------------------------------------\n")

# get attribute value for the object
print("get attribute value for the object")
print("value for course_id - ", getattr(shbytes1, 'course_id'))
print("value for course_id - ", shbytes1.course_id)

print("\n---------------------------------------------------\n")

# set attribute value for the object
print("set attribute value for the object")
print("course details before setting attribute")
shbytes3.courseDetails()
setattr(shbytes3, 'course_duration', 70)
print("course details after setting attribute")
shbytes3.courseDetails()

print("\n---------------------------------------------------\n")

# delete attribute for the object
print("delete attribute for the object")
print("get attribute course_duration before deleting attribute")
print(getattr(shbytes3, 'course_duration'))
delattr(shbytes3, 'course_duration')
print("get attribute course_duration after deleting attribute")

try:
	print(getattr(shbytes3, 'course_duration'))
except AttributeError as err:
	print("error", err)
