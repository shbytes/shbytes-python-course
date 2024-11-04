# Object-Oriented Programming (OOP) in Python
# Class is a user-defined prototype or a blueprint for an object
# defines set of attributes that characterize any object of class
# attributes are data members (class variables and instance variables) and methods
# attributes are accessed via dot notation

# Definition of classes
print("Definition of classes")
class ParentLevel2:
	def parent_level2_method(self):
		print("inside ParentLevel2 class method")

class Parent1Level1(ParentLevel2):
	def parent1_level1_method(self):
		print("inside Parent1Level1 class method")

class Parent2Level1(ParentLevel2):
	def parent2_level1_method(self):
		print("inside Parent2Level1 class method")
		
class Child(Parent1Level1, Parent2Level1):
	def child_method(self):
		print("inside Child class method")

print("\n---------------------------------------------------\n")		

child1 = Child()
child1.child_method()
child1.parent1_level1_method()
child1.parent2_level1_method()
child1.parent_level2_method()
ParentLevel2.parent_level2_method(child1)
Parent1Level1.parent_level2_method(child1)
Parent2Level1.parent_level2_method(child1)

print("\n---------------------------------------------------\n")

# Definition of classes for overriding methods
print("Definition of classes for overriding methods")
class ParentLevel2:
	def method3(self):
		print("inside ParentLevel2 class method")

class Parent1Level1(ParentLevel2):
	def method2(self):
		print("inside Parent1Level1 class method")

class Parent2Level1(ParentLevel2):
	def method2(self):
		print("inside Parent2Level1 class method")
		
class Child1(Parent1Level1, Parent2Level1):
	def method1(self):
		print("inside Child class method")

class Child2(Parent2Level1, Parent1Level1):
	def method1(self):
		print("inside Child class method")
		
print("\n---------------------------------------------------\n")

child1 = Child1()
child1.method1()
child1.method2()
child1.method3()
Parent1Level1.method2(child1)
Parent2Level1.method2(child1)

print("\n---------------------------------------------------\n")

child2 = Child2()
child2.method1()
child2.method2()
child2.method3()
Parent1Level1.method2(child1)
Parent2Level1.method2(child1)