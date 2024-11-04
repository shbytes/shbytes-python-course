# Object-Oriented Programming (OOP) in Python
# polymorphism means having many forms
# same function name (but different signatures) use for different types


# Polymorphism with + operator
# + operator performs integer addition
print(15 + 30)    # Output => 45
# + operator performs string concatenation
print("Courses" + "@shbytes.com")  # Output => "Courses@shbytes.com"

print("\n---------------------------------------------------\n")

# Function demonstrating polymorphism
def add_objects(obj_1, obj_2):
    return obj_1 + obj_2

# Using the same function for integers additions
print(add_objects(40, 70))  # Output => 110

# Using the same function for strings concatenation
print(add_objects("Python", "@shbytes.com"))  # Output => Python@shbytes.com

# Using the same function for list extend
print(add_objects([4, 18, 20], [80, 30, 60]))  # Output => [4, 18, 20, 80, 30, 60]

# Using the same function for tuple
print(add_objects((4, 18, 20), (80, 30, 60)))  # Output => (4, 18, 20, 80, 30, 60)

print("\n---------------------------------------------------\n")

# PythonCourse Class
class PythonCourse():  # Inherits from Shbytes
    def course_details(self):
        print("Course: Python Programming\nDuration: 8 Weeks")

# PowerBICourse Class
class PowerBICourse():  # Inherits from Shbytes
    def course_details(self):
        print("Course: Power BI for Data Analysis\nDuration: 6 Weeks")

def get_course_details(course):
    print(course.course_details())

# Creating objects of different classes
python_course = PythonCourse()
powerbi_course = PowerBICourse()

# Calling the same function with different objects
get_course_details(python_course)   # Output => Course: Python Programming\nDuration: 8 Weeks
get_course_details(powerbi_course)  # Output => Course: Power BI for Data Analysis\nDuration: 6 Weeks

print("\n---------------------------------------------------\n")

# Parent class
class Course:
    def course_details(self):
        raise NotImplementedError("Subclasses must implement this method")

# Child class 1
class PythonCourse(Course):     # Inherits from Course
    def course_details(self):   # override definition of course_details function from Course class
        print("Course: Python Programming\nDuration: 8 Weeks")

# Child class 2
class PowerBICourse(Course):    # Inherits from Course
    def course_details(self):   # override definition of course_details function from Course class
        print("Course: Power BI for Data Analysis\nDuration: 6 Weeks")

# create list of objects from Child classes
courses_object_list = [PythonCourse(), PowerBICourse()]

for course_obj in courses_object_list:
    course_obj.course_details() # call course_details() function on each object

print("\n---------------------------------------------------\n")

# len() - inbuilt polymorphic function
print("len() - inbuilt polymorphic function")
print("length of a string - ", len("shbytes"))
print("length of a list - ", len([2, 4, 6, 8]))

print("\n---------------------------------------------------\n")

# user defined polymorphic function
print("user defined polymorphic function")
def sum(k, l, m = 0): 
	return k + l + m

sum(5, 6)
sum(3, 5, 6)

print("\n---------------------------------------------------\n")

# polymorphism with class method
print("polymorphism with class method")

class AWSCourse():
    def name(self):
        print("AWS")
  
    def duration(self):
        print(50)
  
class PythonCourse():
    def name(self):
        print("AWS")
  
    def duration(self):
        print(50)

print("\n---------------------------------------------------\n")
		
aws_course = AWSCourse()
python_course = PythonCourse()

for course in (aws_course, python_course):
    course.name()
    course.duration()

print("\n---------------------------------------------------\n")

# Polymorphism with Inheritance
print("polymorphism with class method")

# Definition of parent class
print("Definition of parent class")
class Parent1:
	def parent1_method(self):
		print("inside Parent1 class method")
	
	def common_method(self):
		print("inside Parent1 common method")

class Parent2:
	def parent2_method(self):
		print("inside Parent2 class method")
	
	def common_method(self):
		print("inside Parent1 common method")
		
# Definition of child class
print("Definition of child class")
class Child(Parent1, Parent2):
	def child_method(self):
		print("inside Child class method")
		
print("\n---------------------------------------------------\n")

child1 = Child()
child1.child_method()
child1.common_method()
child1.parent1_method()

parent2 = Parent2()
parent2.common_method()

print("\n---------------------------------------------------\n")

class FileReader:
    def read_file(self):
        raise NotImplementedError("Subclasses must implement this method")

class TextFileReader(FileReader):
    def read_file(self):
        return "Reading text file"

class CSVFileReader(FileReader):
    def read_file(self):
        return "Reading CSV file"

def file_processor(reader):
    print(reader.read_file())

# Creating objects of different file readers
text_reader = TextFileReader()
csv_reader = CSVFileReader()

# Processing files using polymorphism
file_processor(text_reader)  # Output => Reading text file
file_processor(csv_reader)   # Output => Reading CSV file
