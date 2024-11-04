# function => block of code to run when it is called
# function takes arguments, known as parameters to pass data
# function can return value as a result

# function with 2 parameters
def shbytes_course(course, description):
	print("course => ", course)
	print("description => ", description)

# function call with keyword arguments
shbytes_course(description="Python Programming - Beginner to Master", course="Python")


print("parameter => variable listed inside the parentheses in function definition")
print("argument  => value sent to the function when it is called")

# arbitrary arguments - *args parameters of a function
print("arbitrary arguments - *args parameters of a function")
def star_args(*courses):  # function parameter with astrisk
	print(len(courses))
	print(courses)
	
star_args("AWS","Python","ML")  # function called with 3 arguments
star_args("AWS","Python")       # function called with 2 arguments
star_args("AWS","Python","ML","Power BI") # function called with 4 arguments

print("\n---------------------------------------------------\n")

# arbitrary keyword arguments - **args parameters of a function
print("arbitrary keyword arguments - **args parameters of a function")
def keyword_args(**courses):  # parameter with double astrisk accepts key-value pair elements
	print(len(courses))
	print(courses)

print("\n---------------------------------------------------\n")
# Scenario 1 - arbitrary keyword arguments - **args - no error when all arguments in key=value pair
print("arbitrary keyword arguments - **args - no error when all arguments in key=value pair")
keyword_args(c1="AWS",c2="Python",c3="ML")  # function called with 3 key-value pair arguments
keyword_args(c1="AWS",c2="Python")          # function called with 2 key-value pair arguments
keyword_args(c1="AWS",c2="Python",c3="ML",c4="Power BI")  # function called with 4 key-value pair arguments

print("\n---------------------------------------------------\n")
# Scenario 2 - arbitrary keyword arguments - **args - error when argument not assigned in key=value pair
print("arbitrary keyword arguments - **args - error when argument not assigned in key=value pair")
try:
	keyword_args("AWS",c2="Python",c3="ML") # function called when arguments not assigned in key=value pair
except TypeError as err:  # Raise TypeError
	print("error", err)
