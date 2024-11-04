# Object-Oriented Programming (OOP) in Python
# python does not support method overloading by default
# we can overload the methods but only latest defined method can be used

print("\n---------------------------------------------------\n")

# definition of overloaded methods
print("definition of overloaded methods")
def sum(k, l):
	s = k + l
	print(s)

def sum(k, l, m):
	s = k + l + m
	print(s)

print("\n---------------------------------------------------\n")

sum(3, 4, 5)

print("\n---------------------------------------------------\n")

# overloaded method defined earlier is overridden by later defined method
print("overloaded method defined earlier is overridden by later defined method")
try:
	sum(3, 4)
except TypeError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

# pip3 install multipledispatch
from multipledispatch import dispatch

# define method with two and three parameters using dispatch
print("define method with two and three parameters using dispatch")

@dispatch(int,int)
def sum(k, l):
	s = k + l
	print(s)

@dispatch(int,int,int)
def sum(k, l, m):
	s = k + l + m
	print(s)

# overloaded method with different datatypes
@dispatch(float,float,float)
def sum(k, l, m):
	s = k + l + m
	print(s)
  
print("\n---------------------------------------------------\n")

sum(4, 5)
sum(3, 4, 5)
sum(3.2, 4.4, 5.6)

print("\n---------------------------------------------------\n")
# Method Overloading - Using Default Arguments

class MathOperations:
    def add(self, a, b=0, c=0):         # default values to b & c parameters
        return a + b + c

math_op = MathOperations()
print(math_op.add(15))                  # Output => 15 (one argument)
print(math_op.add(5, 30))         # Output => 35 (two arguments)
print(math_op.add(5, 30, 25))  # Output => 60 (three arguments)

print("\n---------------------------------------------------\n")
# Method Overloading - Using Variable-Length Arguments (*args and **kwargs)

class MathOperations:
    def add(self, *args):            # *args allows variable number of arguments
        sum = 0
        for num in args:
            sum += num
        return sum

math_op = MathOperations()
print(math_op.add(15))               # Output => 15 (one argument)
print(math_op.add(5, 30))      # Output => 35 (two arguments)
print(math_op.add(5, 30, 25))  # Output => 60 (three arguments)


class MathOperations:
    def operation(self, *args, **kwargs):      # **kwargs allows variable number of keyword arguments
        if kwargs.get('operation') == 'multiply':  # Perform multiplication
            result = 1
            for num in args:
                result *= num
            return result
        else:                                     # Default to addition
            result = 0
            for num in args:
                result += num
            return result

math_op = MathOperations()
print(math_op.operation(2, 3))                        # Output => 5 (default: sum)
print(math_op.operation(2, 3, operation='multiply'))  # Output => 6 (multiplication)

print("\n---------------------------------------------------\n")

# Method Overloading - Using Type Checking (isinstance)
class InstanceOperations:
    def concat_or_multiply(self, a, b):
        if isinstance(a, str) and isinstance(b, str):   # check for both parameter value as str
            return a + b     # If str, perform concatenation
        elif isinstance(a, int) and isinstance(b, int): # check for both parameter value as int
            return a * b     # If int, perform multiplication
        else:
            raise "UnsupportedTypesError"  # error, if both parameters are of different type

instance_op = InstanceOperations()
print(instance_op.concat_or_multiply(5, 10))                     # Output: 50
print(instance_op.concat_or_multiply("Python", "@shbytes.com"))  # Output: Python@shbytes.com

print("\n---------------------------------------------------\n")

# Method Overloading - Using Function Dispatching (functools.singledispatch)
from functools import singledispatch  # import singledispatch from functools module

@singledispatch  # Single-dispatch generic function decorator
def add(a):      # define default definition for add(a) function
    raise NotImplementedError("Unsupported type")

@add.register(int)  # register add(variable) function for int datatype argument
def _(a):           # function definition for int datatype argument
    return a + 10

@add.register(str)  # register add(variable) function for str datatype argument
def _(a):           # function definition for str datatype argument
    return a + "@shbytes.com"

print(add(15))         # Output: 25
print(add("PowerBI"))  # Output: PowerBI@shbytes.com

print("\n---------------------------------------------------\n")

# Method Overloading - Using Custom Logic
class MathOperations:
    def add(self, a, b=None, c=None):  # function definition with b & c default to None
        if b is None and c is None:    # check if b & c both are None
            return a
        elif c is None:                # check if c is None
            return a + b               # addition of 2 parameters
        else:
            return a + b + c           # addition of 3 parameters

math_op = MathOperations()
print(math_op.add(50))                   # Output: 50 (one argument)
print(math_op.add(50, 20))         # Output: 75 (two arguments)
print(math_op.add(50, 20, 45))  # Output: 115 (three arguments)

print("\n---------------------------------------------------\n")

# Method Overloading - Using External Libraries (multipledispatch)
from multipledispatch import dispatch  # import dispatch from multipledispatch module

class MathOperations:
    @dispatch(int, int)  # define function for both parameters int
    def add(self, a, b):        # function definition for both parameters int
        return a + b

    @dispatch(str, str)  # define function for both parameters str
    def add(self, a, b):        # function definition for both parameters str
        return a + " " + b

    @dispatch(int, str)  # define function for parameters int & str
    def add(self, a, b):        # function definition for parameters int & str
        return "Unsupported datatype"

math_op = MathOperations()
print(math_op.add(50, 10))                      # Output: 60
print(math_op.add("PowerBI", "@shbytes.com"))   # Output => PowerBI @shbytes.com
print(math_op.add(10, "random"))                # Output => Unsupported datatype
