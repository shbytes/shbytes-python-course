
print("\n---------------------------------------------------\n")

# decorator first program
print("decorator first program")

courses_list = []

def func_add_courses(course):
	courses_list.append(course)
	print(course, "added to the course list")
	print("list of courses - ", courses_list)

def func_course_wrapper(course, add_course_arg):
	def child_func():
		print("inside child_func function")
		if len(course) > 0:
			add_course_arg(course)
		else:
			print("given course is not valid")
	return child_func
	
	
print("\n---------------------------------------------------\n")

func_add_courses = func_course_wrapper("AWS", func_add_courses)
func_add_courses()

# print("\n---------------------------------------------------\n")

# add_course_2 = func_course_wrapper("", func_add_courses)
# add_course_2()

# print("\n---------------------------------------------------\n")

# add_course_3 = func_course_wrapper("Python", func_add_courses)
# add_course_3()

print("\n---------------------------------------------------\n")

# Decorators with Arguments
def repeat(num_times):        # decorator takes argument number of times function to called
    def decorator(func):      # decorator function takes function as an argument
        def wrapper(*args, **kwargs):   # wrapper function
            for _ in range(num_times):  # loop for the number of times
                func(*args, **kwargs)   # function called in loop
        return wrapper                  # return modified wrapper function
    return decorator

@repeat(num_times=3)            # @ decorator with num_times argument 3
def introduction(name):         # function on which decorator is used
    print(f"Courses@{name}")

introduction("shbytes.com")     # call the actual function

print("\n---------------------------------------------------\n")

# Chaining Multiple Decorators
def bold_decorator(func):          # decorator takes function as an argument
    def wrapper():                 # wrapper function to add <b> tag
        return f"<b>{func()}</b>"
    return wrapper                 # return wrapper function

def italic_decorator(func):        # decorator takes function as an argument
    def wrapper():                 # wrapper function to add <i> tag
        return f"<i>{func()}</i>"
    return wrapper                 # return wrapper function

@bold_decorator                    # bold_decorator applied on function
@italic_decorator                  # italic_decorator applied on function
def say_shbytes():                 # multiple decorators (chaining) applied on function
    return "shbytes.com"

print(say_shbytes())               # call to the actual function
# Output => <b><i>shbytes.com</i></b>

print("\n---------------------------------------------------\n")
# Class-Based Decorators
class ShbytesDecorator:         # decorator class
    def __init__(self, func):   # initialize function
        self.func = func

    def __call__(self):         # __call__ makes class instance callable like a function
        print("Before the function call")
        self.func()
        print("After the function call")

@ShbytesDecorator               # class decorator used over a function
def say_shbytes():
    print("shbytes.com")

say_shbytes()

print("\n---------------------------------------------------\n")

class ShbytesClass:
    @staticmethod             # makes method static
    def say_shbytes():        # static method in Shbytes class
        print("shbytes.com")

ShbytesClass.say_shbytes()    # calling method using class name
# Output => shbytes.com

print("\n---------------------------------------------------\n")
class ShbytesClass:
    @classmethod              # makes method class level method
    def say_shbytes(cls):     # class level method
        print(f"Hello from {cls}")

ShbytesClass.say_shbytes()    # calling method using class name
# Output => Hello from <class '__main__.ShbytesClass'>

print("\n---------------------------------------------------\n")
class MyClass:
    def __init__(self, value):
        self._value = value

    @property                # getter method for value property
    def value(self):
        return self._value

    @value.setter            # setter method for value property
    def value(self, new_value):
        self._value = new_value

obj = MyClass(10)   # calls __init__ method
print(obj.value)    # calls getter method for value property; Output => 10
obj.value = 20      # calls setter method for value property
print(obj.value)    # calls getter method for value property; Output => 20

print("\n---------------------------------------------------\n")
# logging example
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def add(a, b):
    return a + b

print(add(5, 10))
# Output => Calling add with (5, 10), {}; 15

print("\n---------------------------------------------------\n")
# timing example
import time

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()        # take function start time
        result = func(*args, **kwargs)
        end_time = time.time()          # take function end time
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@calculate_execution_time
def slow_function():
    time.sleep(1)
    print("Function finished")

slow_function()
# Output => Function finished; slow_function took 1.0010 seconds to execute