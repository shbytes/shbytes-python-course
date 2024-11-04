# Object-Oriented Programming (OOP) in Python
# Class is a user-defined prototype or a blueprint for an object
# defines set of attributes that characterize any object of class
# attributes are data members (class variables and instance variables) and methods
# attributes are accessed via dot notation

# Definition of parent class
print("Definition of parent class")
class Parent:
    """Parent"""

    # __init__() is the constructor of the class
    def __init__(self):
        print("inside parent class constructor")

    def overriding_method(self):
        print("inside parent class overriding method")

# Definition of child class
print("Definition of child class")
class Child(Parent):
    """Child"""

    # __init__() is the constructor of the class
    def __init__(self):
        print("inside child class constructor")

    def overriding_method(self):
        print("inside child class overriding method")

# create object & instance of the class, with instance referring to object
print("create object & instance of the class, with instance referring to object")
child1 = Child()
child1.overriding_method()
parent1 = Parent()
parent1.overriding_method()

print("\n---------------------------------------------------\n")

# Basic Method Overriding
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

python_course = PythonCourse()
powerbi_course = PowerBICourse()
python_course.course_details()   # Output: Course: Python Programming\nDuration: 8 Weeks
powerbi_course.course_details()  # Output: Course: Power BI for Data Analysis\nDuration: 6 Weeks

print("\n---------------------------------------------------\n")
# Method Overriding - Using super()
# Parent class
class Course:
    def course_details(self):
        return "Course completion certification"

# Child class 1
class PythonCourse(Course):     # Inherits from Course
    def course_details(self):   # override definition of course_details function from Course class
        # Call the parent class's method using super()
        parent_course_details = super().course_details()
        return "Course: Python Programming\nDuration: 8 Weeks\n" + parent_course_details

# Child class 2
class PowerBICourse(Course):    # Inherits from Course
    def course_details(self):   # override definition of course_details function from Course class
        # Call the parent class's method using super()
        parent_course_details = super().course_details()
        return "Course: Power BI for Data Analysis\nDuration: 6 Weeks\n" + parent_course_details

python_course = PythonCourse()
powerbi_course = PowerBICourse()
print(python_course.course_details())
# Output: Course: Python Programming\nDuration: 8 Weeks\nCourse completion certification

print(powerbi_course.course_details())
# Output: Course: Power BI for Data Analysis\nDuration: 6 Weeks\nCourse completion certification

print("\n---------------------------------------------------\n")
# Method Overriding - Using Constructors (__init__)
# Parent class
class Course:
    def __init__(self, name, duration):  # parent class constructor
        self.name = name
        self.duration = duration

# Child class 1
class PythonCourse(Course):     # Inherits from Course
    def __init__(self, name, duration):
        super().__init__(name, duration)                 # call the parent class's constructor
        self.course_syllabus = "Python course syllabus"  # sets another attribute

    def course_details(self):    # method to get complete course details
        return f"{self.name}, {self.duration}, {self.course_syllabus}"

python_course = PythonCourse("Python Programming", "Duration: 8 Weeks")
print(python_course.course_details())
# Output: Python Programming, Duration: 8 Weeks, Python course syllabus

print("\n---------------------------------------------------\n")
# Method Overriding - Using @classmethod
# Parent class
class Course:
    @classmethod                # Convert a function to be a class method.
    def course_details(cls):    # first parameter as cls
        return "Course completion certification"

# Child class 1
class PythonCourse(Course):     # Inherits from Course
    @classmethod                # Convert a function to be a class method.
    def course_details(cls):    # override course_details function from Course class
        return "Course: Python Programming\nDuration: 8 Weeks"

# Child class 2
class PowerBICourse(Course):    # Inherits from Course
    @classmethod                # Convert a function to be a class method.
    def course_details(cls):    # override course_details function from Course class
        return "Course: Power BI for Data Analysis\nDuration: 6 Weeks"

print(PythonCourse.course_details())
# Output: Course: Python Programming\nDuration: 8 Weeks

print(PowerBICourse.course_details())
# Output: Course: Power BI for Data Analysis\nDuration: 6 Weeks

print("\n---------------------------------------------------\n")
# Method Overriding - Using @staticmethod
# Parent class
class Course:
    @staticmethod            # Convert a function to static method.
    def course_details():    # first parameter as cls
        return "Course completion certification"

# Child class 1
class PythonCourse(Course):     # Inherits from Course
    @staticmethod               # Convert a function to static method.
    def course_details():       # override course_details function from Course class
        return "Course: Python Programming\nDuration: 8 Weeks"

# Child class 2
class PowerBICourse(Course):    # Inherits from Course
    @staticmethod               # Convert a function to static method.
    def course_details():       # override course_details function from Course class
        return "Course: Power BI for Data Analysis\nDuration: 6 Weeks"

print(PythonCourse.course_details())
# Output: Course: Python Programming\nDuration: 8 Weeks

print(PowerBICourse.course_details())
# Output: Course: Power BI for Data Analysis\nDuration: 6 Weeks

print("\n---------------------------------------------------\n")
# Overriding Properties Using @property
# Parent class
class Course:
    @property                    # define property
    def course_details(self):
        return "Course completion certification"

# Child class 1
class PythonCourse(Course):     # Inherits from Course
    @property                   # define property
    def course_details(self):   # override course_details function from Course class
        return "Course: Python Programming\nDuration: 8 Weeks\n" + super().course_details

# Child class 2
class PowerBICourse(Course):     # Inherits from Course
    @property                    # define property
    def course_details(self):    # override course_details function from Course class
        return "Course: Power BI for Data Analysis\nDuration: 6 Weeks\n" + super().course_details

python_course = PythonCourse()
powerbi_course = PowerBICourse()

print(python_course.course_details)
# Output: Course => Python Programming\nDuration: 8 Weeks\nCourse completion certification

print(powerbi_course.course_details)
# Output: Course => Power BI for Data Analysis\nDuration: 6 Weeks\nCourse completion certification

print("\n---------------------------------------------------\n")
# Overriding Magic (Dunder) Methods
# Parent class
class Course:
    def __str__(self):          # define __str__ method
        return "Course completion certification"

# Child class 1
class PythonCourse(Course):     # Inherits from Course
    def __str__(self):          # override __str__ method
        return "Course: Python Programming\nDuration: 8 Weeks"

course = Course()
python_course = PythonCourse()
print(course)          # Output => Course completion certification
print(python_course)   # Output => Course: Python Programming\nDuration: 8 Weeks


print("\n---------------------------------------------------\n")
# Method Overriding - Multilevel Inheritance
# GrandParent class
class Shbytes:
    def course_info(self):             # defined function
        print("Generic course info.")

# Parent class (inherits from Shbytes)
class Courses(Shbytes):
    def course_info(self):             # override function from Shbytes class
        print("Courses: Offering a variety of tech and business courses.")

# Child class (inherits from Courses)
class PythonCourse(Courses):
    def course_info(self):             # override function from Courses class
        print("Python Course: A detailed course on Python programming.")

# Creating an object of the grandchild class
python_course = PythonCourse()
python_course.course_info()    # Method of PythonCourse (Child class)
# Output => Python Course: A detailed course on Python programming.

print("\n---------------------------------------------------\n")
# Method Overriding - Using super() in Multiple Inheritance (MRO)
# GrandParent class
class Shbytes:
    def course_info(self):
        return "courses@shbytes.com"

# Parent class
class Course(Shbytes):
    def course_info(self):
        return "Course completion certification - " + super().course_info()

# Child class
class PythonCourse(Course):     # Inherits from Course
    def course_info(self):   # override course_details function from Course class
        return "Course: Python Programming\nDuration: 8 Weeks\n" + super().course_info()

python_course = PythonCourse()
print(python_course.course_info())
# Output: Course => Python Programming\nDuration: 8 Weeks\nCourse completion certification - courses@shbytes.com

print("\n---------------------------------------------------\n")
# Method Overriding - Private Methods
class Course(Shbytes):
    def __course_info(self):      # define private method for Course class
        return "Course completion certification"

    def get_course_info(self):    # method calling private method
        return self.__course_info()

class PythonCourse(Course):
    def __course_info(self):     # define private method for PythonCourse class
        return "Course: Python Programming\nDuration: 8 Weeks"

python_course = PythonCourse()
print(python_course.get_course_info())
# Output: Course completion certification (private method not overridden)
