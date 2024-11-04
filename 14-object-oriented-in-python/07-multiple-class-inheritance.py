# Object-Oriented Programming (OOP) in Python
# Class is a user-defined prototype or a blueprint for an object
# defines set of attributes that characterize any object of class
# attributes are data members (class variables and instance variables) and methods
# attributes are accessed via dot notation

# Definition of Parent1 class
print("Definition of parent class")
class Parent1:
	def parent1_method(self):
		print("inside Parent1 class method")

# Definition of Parent2 class
class Parent2:
	def parent2_method(self):
		print("inside Parent2 class method")
		
# Definition of Child class which inherits Parent1 and Parent2 class
print("Definition of child class")
class Child(Parent1, Parent2):
	def child_method(self):
		print("inside Child class method")

print("\n---------------------------------------------------\n")		

# create object & instance of the class, with instance referring to object
print("create object & instance of the class, with instance referring to object")
child1 = Child()
child1.child_method()   # Child class object access Child class method
child1.parent1_method() # Child class object access Parent1 class method
child1.parent2_method() # Child class object access Parent2 class method

print("\n---------------------------------------------------\n")

# Parent Class 1
class Shbytes:
    def company_info(self):
        print("Shbytes is an EdTech company providing IT solutions and training.")

# Parent Class 2
class Courses:
    def course_info(self):
        print("Shbytes offers courses in Python, Data Science, and Cloud Computing.")

# Child Class inheriting from both Shbytes and Courses
class Training(Shbytes, Courses):
    def training_details(self):
        print("The training includes hands-on labs and real-world projects.")

# Creating an object of the Training class
training_session = Training()

# Accessing methods from parent classes and the child class
training_session.company_info()   # Method from Shbytes class
training_session.course_info()    # Method from Courses class
training_session.training_details()  # Method from Training class


print("\n---------------------------------------------------\n")

# Multilevel Inheritance

# Definition of GrandParent class
class GrandParent:
	def grand_parent_method(self):
		print("inside GrandParent class method")


# Definition of Parent class inherits GrandParent class
class Parent(GrandParent):
	def parent_method(self):
		print("inside Parent class method")

# Definition of Child class inherits Parent class
class Child(Parent):
	def child_method(self):
		print("inside Child class method")


print("\n---------------------------------------------------\n")

# create object & instance of the class, with instance referring to object
print("create object & instance of the class, with instance referring to object")
child1 = Child()
child1.child_method()         # Child class object access Child class method
child1.parent_method()        # Child class object access Parent class method
child1.grand_parent_method()  # Child class object access GrandParent class method

parent1 = Parent()
parent1.parent_method()       # Parent class object access Parent class method
parent1.grand_parent_method() # Parent class object access GrandParent class method

print("\n---------------------------------------------------\n")
# GrandParent class
class Shbytes:
    def company_info(self):
        print("Shbytes: A platform for educational courses.")

# Parent class (inherits from Shbytes)
class Courses(Shbytes):
    def course_info(self):
        print("Courses: Offering a variety of tech and business courses.")

# Child class (inherits from Courses)
class PythonCourse(Courses):
    def python_course_info(self):
        print("Python Course: A detailed course on Python programming.")

# Creating an object of the grandchild class
python_course = PythonCourse()

# Calling methods from all levels of inheritance
python_course.company_info()        # Inherited from Shbytes (GrandParent class)
python_course.course_info()         # Inherited from Courses (Parent class)
python_course.python_course_info()  # Method of PythonCourse (Child class)


print("\n---------------------------------------------------\n")

# Hierarchical Inheritance

# Definition of Parent class
class Parent():
	def parent_method(self):
		print("inside Parent class method")

# Definition of FirstChild class inherits Parent class
class FirstChild(Parent):
	def first_child_method(self):
		print("inside FirstChild class method")

# Definition of SecondChild class inherits Parent class
class SecondChild(Parent):
	def second_child_method(self):
		print("inside SecondChild class method")

# create object & instance of the class, with instance referring to object
print("create object & instance of the class, with instance referring to object")
first_child = FirstChild()
first_child.first_child_method()   # FirstChild class object access FirstChild class method
first_child.parent_method()        # FirstChild class object access Parent class method

second_child = SecondChild()
second_child.second_child_method()  # SecondChild class object access SecondChild class method
second_child.parent_method()        # SecondChild class object access Parent class method

# first_child.second_child_method()  # FirstChild class object cannot access SecondChild class method
# second_child.first_child_method()  # SecondChild class object cannot access FirstChild class method

print("\n---------------------------------------------------\n")

# Parent class
class Shbytes:
    def company_info(self):
        print("Welcome to Shbytes - Learn Tech Skills for a Digital Future!")

# Child class 1
class PythonCourse(Shbytes):  # Inherits from Shbytes
    def course_details(self):
        print("Course: Python Programming\nDuration: 8 Weeks")

# Child class 2
class PowerBICourse(Shbytes):  # Inherits from Shbytes
    def course_details(self):
        print("Course: Power BI for Data Analysis\nDuration: 6 Weeks")

# Creating objects of child classes
python_course = PythonCourse()
powerbi_course = PowerBICourse()

# Calling methods
python_course.company_info()    # Inherited from Shbytes
python_course.course_details()  # Method from PythonCourse

print()  # For readability

powerbi_course.company_info()    # Inherited from Shbytes
powerbi_course.course_details()  # Method from PowerBICourse
