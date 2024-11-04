# Exception handling in Python

print("\n---------------------------------------------------\n")

# raise exception - allows the programmer to force a specified exception to occur
print("raise exception - allows the programmer to force a specified exception to occur")

course_list = []                # declare an empty list
try:                            # try block
	if len(course_list) <= 0:   # check if length of list is less than or equal to 0
		raise ValueError("error, no course is defined") # raise ValueError with message
except ValueError as err:       # catch ValueError
	print("error", err)         # print error

print("\n---------------------------------------------------\n")

# exception chaining is default
print("exception chaining is default")

def file_operations():
	try:
		read_file()                      # call to read_file() function
	except FileNotFoundError as err:     # catch FileNotFoundError raised from read_file() function
		print("read_file error - ", err) # print error
		#raise IOError("file operations failed with error") # raise IOError

def read_file():
	raise FileNotFoundError("file with given name not found") # raise FileNotFoundError

file_operations()  # call to file_operations() function

# exception chaining is default, but can be disabled with from None clause
print("exception chaining is default, but can be disabled with from None clause")

def file_operations():
	try:
		read_file()
	except FileNotFoundError as err:
		print("read_file error - ", err)
		raise IOError("file operations failed with error") from None

def read_file():
	raise FileNotFoundError("file with given name not found") from None

file_operations()
