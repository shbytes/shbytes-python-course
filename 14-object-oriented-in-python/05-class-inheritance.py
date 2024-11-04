# Object-Oriented Programming (OOP) in Python
# Class is a user-defined prototype or a blueprint for an object
# defines set of attributes that characterize any object of class
# attributes are data members (class variables and instance variables) and methods
# attributes are accessed via dot notation

# create a class by deriving it from a pre-existing class
# syntax of child class creation
print("syntax of child class creation")
# class ChildClassName(ParentClass1[, ParentClass2, ...]):
# 	"""class documentation string is optional"""
# 	class_attributes

print("\n---------------------------------------------------\n")


# Definition of parent class
class Parent:
	"""Parent class docstring"""
	
	# __init__() is the constructor of the class
	def __init__(self):                     # Initialize Parent class
		print("inside Parent class constructor")
	
	def parentClassMethod(self):            # method in Parent class
		print("inside Parent class method")

parent1 = Parent()            # create an object of Parent Class
parent1.parentClassMethod()   # call Parent class method using Parent class object

# Definition of child class
class Child(Parent):                        # Child class inherit Parent class
	"""Child"""
	
	# __init__() is the constructor of the class
	def __init__(self):                     # Initialize Child class
		print("inside Child class constructor")
	
	def childClassMethod(self):             # method in Child class
		print("inside Child class method")

print("\n---------------------------------------------------\n")		

# create object & instance of Child class, with instance referring to object
child1 = Child()            # create an object of Child Class
child1.childClassMethod()   # call Child class method using Child class object
child1.parentClassMethod()  # call Parent class method using Child class object

try:
	parent1.childClassMethod()  # Using the Parent class, we cannot call Child class method
except AttributeError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

# check for subclass (child class) of a superclass (parent class)
print("check for subclass (child class) of a superclass (parent class)")
print("Child class is sub class of Parent - ", issubclass(Child, Parent)) # Output => True
print("Parent class is sub class of Child - ", issubclass(Parent, Child)) # Output => False

print("\n---------------------------------------------------\n")

# check for object is instance of given class
print("check for object is instance of given class")
print("child1 is instance of Child class - ", isinstance(child1, Child))     # Output => True
print("child1 is instance of Parent class - ", isinstance(child1, Parent))   # Output => True
print("parent1 is instance of Child class - ", isinstance(parent1, Child))   # Output => False
print("parent1 is instance of Parent class - ", isinstance(parent1, Parent)) # Output => True

print("\n---------------------------------------------------\n")

# Parent class
class Shbytes:
    def company_info(self):
        print("Shbytes is a platform for learning tech skills.")

# Child class inheriting from Shbytes
class Courses(Shbytes):
    def display_course(self):
        print("We offer courses on Python, Data Science, and AI.")

# Create an object of the child class
course = Courses()

# Calling method from the parent class
course.company_info()   # Output => Shbytes is a platform for learning tech skills.

# Calling method from the child class
course.display_course() # Output => We offer courses on Python, Data Science, and AI.
