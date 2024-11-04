
print("\n---------------------------------------------------\n")

# first class functions can be returned from another function

courses_list = []
# define a function to add course into a course list
def func_add_courses(course):
	courses_list.append(course)
	print(course, "added to the course list")

# define a function to check if course is valid or not
def func_course_valid(course):    # takes course as parameter
	if len(course) > 0:
		return func_add_courses   # return another function
	else:
		print("given course is not valid")

return_func = func_course_valid("Power BI") # This function returns another function
return_func("Power BI")                     # call to returned function

return_func = func_course_valid("Python")  # This function returns another function
return_func("Python")                      # call to returned function

return_func = func_course_valid("")         # Invalid course, will not return function
try:
	return_func("")                         # call to function will raise NameError and TypeError
except (NameError, TypeError) as err:
	print("error", err)

print(courses_list) # Output => ['Power BI', 'Python']

print("\n---------------------------------------------------\n")
# Closures in Python
def outer_function(text):
    def inner_function():
        return text  # The inner function remembers 'text' even after 'outer_function' finishes.
    return inner_function

my_closure = outer_function("courses@shbytes.com")
print(my_closure())  # Output: courses@shbytes.com


print("\n---------------------------------------------------\n")

# Higher-Order Functions
def apply_thrice(func, argument):
    return func(func(func(argument)))  # return function called 3 times

def add_ten(x):
    return x + 10

# Using 'apply_thrice' with 'add_ten'
result = apply_thrice(add_ten, 20)  # This will add 10 to 20 thrice
print(result) # Output => 50

print("\n---------------------------------------------------\n")
# Real-World Use Cases: Functions as First-Class Objects
def shbytes_decorator(func):  # function takes another function as argument
    def wrapper():            # wrapper function which calls the argument function in it
        print("Do something before the function")
        func()                # argument function called
        print("Do something after the function")
    return wrapper

@shbytes_decorator            # @ decorator function
def say_shbytes():            # function used as argument for decorator function
    print("shbytes.com")

say_shbytes()                 # call to the function, which calls decorator function
