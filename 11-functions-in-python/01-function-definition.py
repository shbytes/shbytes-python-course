# function => block of code to run when it is called
# function takes arguments, known as parameters to pass data
# function can return value as a result

# syntax to create a function with parameters
print("syntax to create a function with parameters")
def function_name(parameters):
	"""docstring of function_name function"""
	# statement(s)
	# return value

print("parameter => variable listed inside the parentheses in function definition")
print("argument  => value sent to the function when it is called")

print("\n---------------------------------------------------\n")

# definition of a function with parameters and docstring
print("definition of a function with parameters and docstring")
def shbytes(courses):
	"""This is the docstring of a function shbytes function takes courses as argument"""
	print(courses)    # Print the value of parameters passed

print("\n---------------------------------------------------\n")

# docstring of the function
print("docstring of the function")
print(shbytes.__doc__) # Access docstring of the function
shbytes("Python")      # Call to the function with argument

print("\n---------------------------------------------------\n")

# call a function with arguments
print("call a function with arguments")
shbytes(["AWS","Python","ML"])

print("\n---------------------------------------------------\n")

# use cases for arguments of a function
print("use cases for arguments of a function")

print("\n---------------------------------------------------\n")

# function definition with 3 parameters
def shbytes_3(c1, c2, c3):
	print(c1)
	print(c2)
	print(c3)

# call to the function with 3 arguments
print("call to the function with 3 arguments")
shbytes_3("AWS","Python","ML") # function called with 3 arguments

# function with 3 parameters, but called with 2 arguments
print("function with 3 parameters, but called with 2 arguments")
try:
	shbytes_3("AWS","Python") # function called with 2 arguments
except TypeError as err:             # raised TypeError - missing argument
	print("error", err)

print("\n---------------------------------------------------\n")

# function definition with 3 parameters, last parameter has default value
def shbytes_3(c1, c2, c3="ML"):
	print(c1)
	print(c2)
	print(c3)

# function called with 2 arguments
shbytes_3("AWS","Python") # function called with 2 arguments

print("\n---------------------------------------------------\n")

# function definition with dynamic datatype parameter and iteration inside function
def shbytes_list(courses):
	for course in courses:  # iterate over the sequence collection
		print(course)       # Print each element

shbytes_list("Python") # function called with string argument
shbytes_list(["AWS","Python","ML","DevOps"]) # function called with list argument
shbytes_list(("AWS","Python","ML","DevOps")) # function called with tuple argument
shbytes_list({"AWS","Python","ML","DevOps"}) # function called with set argument
shbytes_list({1:"AWS",2:"Python",3:"ML",4:"DevOps"}) # function called with dictionary argument