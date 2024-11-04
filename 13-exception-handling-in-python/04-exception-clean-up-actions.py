# Exception handling in Python

# finally clause is used for clean-up actions
print("finally clause is used for clean-up actions")

print("\n---------------------------------------------------\n")

# try except finally clause - finally is always executed, whether exception is raised or not
print("try except finally clause - finally is always executed, whether exception is raised or not")

try:
	del number
except NameError as err:
	print("error", err)
finally:
	print("finally statement is always executed, irrespective of error raised or not")

print("\n---------------------------------------------------\n")

# finally clause is always called, even after execution of with break, continue, return statements
print("finally clause is always called, even after execution of with break, continue, return statements")

try:
	for x in range(10):
		if x > 3:
			break
except NameError as err:
	print("error", err)
finally:
	print("finally statement is always executed, irrespective of error raised or not")

print("\n---------------------------------------------------\n")

def method1():
	return "shbytes"
try:
	method1()
except NameError as err:
	print("error", err)
finally:
	print("finally statement is always executed, irrespective of error raised or not")
	
print("\n---------------------------------------------------\n")

# try except finally nested clause
print("try except finally nested clause")

try:
	course_file = open("course_details.txt")
except FileNotFoundError as err:
	print("error", err)
finally:
	print("finally statement is always executed, irrespective of error raised or not")
	try:
		course_file.close()
	except NameError as err:
		print("error", err)
