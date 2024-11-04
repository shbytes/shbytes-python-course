
# Definition of GrandParent class
class GrandParent:
    def grand_parent_method(self):
        print("inside GrandParent class method")

# Hierarchical Inheritance
# Definition of Parent1 class inherits GrandParent class
class Parent1(GrandParent):
    def method1(self):
        print("inside Parent1 class method")
        # calling GrandParent method with Parent1 class or its Child class object
        GrandParent.grand_parent_method(self)

# Hierarchical Inheritance
# Definition of Parent2 class inherits GrandParent class
class Parent2(GrandParent):
    def method1(self):
        print("inside Parent2 class method")
        # calling GrandParent method with Parent2 class or its Child class object
        GrandParent.grand_parent_method(self)

# Multiple Inheritance
# Definition of Child class inherits Parent1Level1 and Parent2Level1 class
class Child(Parent1, Parent2):
    def child_method(self):
        print("inside Child class method")
        Parent1.method1(self) # calling Parent1 method with Child class object
        Parent2.method1(self) # calling Parent2 method with Child class object

child = Child()
child.child_method()

print("\n---------------------------------------------------\n")

# GrandParent Class
class Shbytes:
    def __init__(self, institute_name):
        self.institute_name = institute_name

    def show_institute(self):
        print(f"Institution: {self.institute_name}")

# First Course Class
class PythonCourse(Shbytes):
    def __init__(self, institute_name, python_course_name):
        super().__init__(self, institute_name)
        self.python_course_name = python_course_name

    def show_python_course(self):
        print(f"Python Course: {self.python_course_name}")

# Second Course Class
class PowerBICourse(Shbytes):
    def __init__(self, institute_name, powerbi_course_name):
        super().__init__(institute_name)
        self.powerbi_course_name = powerbi_course_name

    def show_power_bi_course(self):
        print(f"Power BI Course: {self.powerbi_course_name}")

# Child Class that inherits from both PythonCourse and PowerBICourse
class Training(PythonCourse, PowerBICourse):
    def __init__(self, institute_name, python_course_name, power_bi_course_name, training_type):
        # Call constructors of both parent classes
        PythonCourse.__init__(self, institute_name, python_course_name)
        PowerBICourse.__init__(self, institute_name, power_bi_course_name)
        self.training_type = training_type

    def show_training(self):
        print(f"Training Type: {self.training_type}")
        self.show_python_course()
        self.show_power_bi_course()

# Creating an instance of the Training class
training = Training("Shbytes Academy", "Advanced Python", "Power BI Dashboards", "Online Training")

# Calling methods
training.show_institute()       # Inherited from Shbytes
training.show_training()        # Inherited from both PythonCourse and PowerBiCourse

print("\n---------------------------------------------------\n")


# GrandParent Class
class Shbytes:
    def __init__(self, institute_name):
        self.institute_name = institute_name

    def show_institute(self):
        print(f"Institution: {self.institute_name}")

# First Course Class
class PythonCourse(Shbytes):
    def __init__(self, institute_name, python_course_name):
        super().__init__(self, institute_name)
        self.python_course_name = python_course_name

    def show_python_course(self):
        print(f"Python Course: {self.python_course_name}")

# Second Course Class
class PowerBICourse(Shbytes):
    def __init__(self, institute_name, powerbi_course_name):
        super().__init__(institute_name)
        self.powerbi_course_name = powerbi_course_name

    def show_power_bi_course(self):
        print(f"Power BI Course: {self.powerbi_course_name}")

# Child Class that inherits from both PythonCourse and PowerBICourse
class Training(PythonCourse, PowerBICourse):
    def __init__(self, institute_name, python_course_name, power_bi_course_name, training_type):
        # Call constructors of both parent classes
        PythonCourse.__init__(self, institute_name, python_course_name)
        PowerBICourse.__init__(self, institute_name, power_bi_course_name)
        self.training_type = training_type

    def show_training(self):
        print(f"Training Type: {self.training_type}")
        self.show_python_course()
        self.show_power_bi_course()

# Creating an instance of the Training class
training = Training("Shbytes Academy", "Advanced Python", "Power BI Dashboards", "Online Training")
print(Training.__mro__)  # Returns tuple of class method resolution order
print(Training.mro())    # Returns list of class method resolution order
# Calling methods
training.show_institute()       # Inherited from Shbytes
training.show_training()        # Inherited from both PythonCourse and PowerBiCourse