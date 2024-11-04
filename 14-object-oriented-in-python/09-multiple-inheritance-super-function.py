# Object-Oriented Programming (OOP) in Python
# Class is a user-defined prototype or a blueprint for an object
# defines set of attributes that characterize any object of class
# attributes are data members (class variables and instance variables) and methods
# attributes are accessed via dot notation

# Definition of classes for overriding methods without super function
print("Definition of classes for overriding methods without super function")
class ParentLevel2:
	def method1(self):
		print("inside ParentLevel2 class method")

class Parent1Level1(ParentLevel2):
	def method1(self):
		print("inside Parent1Level1 class method")
		ParentLevel2.method1(self)

class Parent2Level1(ParentLevel2):
	def method1(self):
		print("inside Parent2Level1 class method")
		ParentLevel2.method1(self)
		
class Child1(Parent1Level1, Parent2Level1):
	def method1(self):
		print("inside Child class method")
		Parent1Level1.method1(self)
		Parent2Level1.method1(self)
		
print("\n---------------------------------------------------\n")

child1 = Child1()
child1.method1()

print("\n---------------------------------------------------\n")

# Definition of classes for overriding methods with super function
print("Definition of classes for overriding methods with super function")
class ParentLevel2:
	def method1(self):
		print("inside ParentLevel2 class method")

class Parent1Level1(ParentLevel2):
	def method1(self):
		print("inside Parent1Level1 class method")
		super().method1()

class Parent2Level1(ParentLevel2):
	def method1(self):
		print("inside Parent2Level1 class method")
		super().method1()
		
class Child1(Parent1Level1, Parent2Level1):
	def method1(self):
		print("inside Child class method")
		super().method1()
		
print("\n---------------------------------------------------\n")

child1 = Child1()
child1.method1()

print("\n---------------------------------------------------\n")

# Method Resolution Order (MRO)
print("Method Resolution Order (MRO)")
print(Child1.mro())