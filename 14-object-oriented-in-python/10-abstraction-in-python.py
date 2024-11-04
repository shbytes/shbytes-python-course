# Object-Oriented Programming (OOP) in Python
# abstract class is not a complete class in itself
# abstract class can be considered as blueprint for other classes
# set of methods that must be created within any child classes built from abstract class

# By default, Python does not provide abstract classes
# module that provides the base for defining Abstract Base classes(ABC)

print("\n---------------------------------------------------\n")

# import ABC (Abstract Base Class) and abstractmethod from the abc module
from abc import ABC, abstractmethod

# abstract class
class Shbytes(ABC):
	def instituteName(self):
		(print("shbytes")

	@abstractmethod)             # annotation used on abstract method
	def trainingCourse(self):    # abstract method
		print("TrainingCourse@shbytes")

print("\n---------------------------------------------------\n")

# Abstract Base Classes(ABC)
# Definition of abstract class and its child classes
print("Definition of abstract class and its child classes")

# import ABC (Abstract Base Class) and abstractmethod from the abc module
from abc import ABC, abstractmethod

# abstract class with ABC as parent class
class Shbytes(ABC):
	def instituteName(self):
		print("shbytes")
	
	@abstractmethod
	def trainingCourse(self):            # abstract method
		print("TrainingCourse@shbytes")

class PowerBITraining(Shbytes):          # class inherits from Shbytes class
	# overriding abstract method
	def trainingCourse(self):            # define trainingCourse() abstract method from parent class
		print("Training Course - Power BI")

class PythonTraining(Shbytes):           # class inherits from Shbytes class
	# overriding abstract method
	def trainingCourse(self):            # define trainingCourse() abstract method from parent class
		print("Training Course - Python")
 
class MLTraining(Shbytes):               # class inherits from Shbytes class
	# overriding abstract method
	def trainingCourse(self):            # define trainingCourse() abstract method from parent class
		print("Training Course - ML")

print("\n---------------------------------------------------\n")

powerbi_training = PowerBITraining()  # create an object and instance of PowerBITraining class
powerbi_training.trainingCourse()     # call trainingCourse() method from PowerBITraining class
powerbi_training.instituteName()      # call instituteName() method from parent Shbytes abstract class

print("\n---------------------------------------------------\n")

python_training = PythonTraining()  # create an object and instance of PythonTraining class
python_training.trainingCourse()    # call trainingCourse() method from PythonTraining class
python_training.instituteName()     # call instituteName() method from parent Shbytes abstract class

print("\n---------------------------------------------------\n")

ml_training = MLTraining()      # create an object and instance of MLTraining class
ml_training.trainingCourse()    # call trainingCourse() method from MLTraining class
ml_training.instituteName()     # call instituteName() method from parent Shbytes abstract class

print("\n---------------------------------------------------\n")

# object of an abstract class cannot be created
print("object of an abstract class cannot be created")
try:
	training1 = Shbytes()   # Will give error - cannot create an object of abstract class
except TypeError as err:
	print("error", err)
