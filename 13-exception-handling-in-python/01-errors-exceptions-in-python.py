# Exception handling in Python
# Two distinguishable kinds of errors: syntax errors and exceptions

# Syntax Errors
# if True print('Hello shbytes')
print("if True print('Hello shbytes') - Syntax Error")

try:
    result = 12 / 0 # attempt to divide by zero will raise ZeroDivisionError
except ZeroDivisionError: # except block can handle the error
    print("Cannot divide by zero!")

print("\n---------------------------------------------------\n")

# Exceptions
# 5 * (2/0) - ZeroDivisionError: division by zero
print("5 * (2/0) - ZeroDivisionError: division by zero")

print("\n---------------------------------------------------\n")

# Exception Handling
# try ...except clause
print("try ...except clause")
print("many errors can be handled with multiple except clause")

try:
    num = int(input("Enter a number: "))  # Take user input from the console
    result = 12 / num
except ValueError:                        # Raise ValueError is user input is not number
    print("Invalid input! Please enter a valid number.") # Statement to execute for ValueError
except ZeroDivisionError:                 # Raise ZeroDivisionError is user input is zero
    print("You cannot divide by zero!")   # Statement to execute for ZeroDivisionError


try:
	del number                  # Delete the variable number
except AttributeError as err:   # handle AttributeError
	print("error", err)         # Statement to execute for AttributeError
except (TypeError, NameError) as err: # handle TypeError and NameError
	print("error", err)         # Statement to execute for either TypeError or NameError


try:
    result = 10 / 0  # raise ZeroDivisionError
except:              # will catch all exceptions
    print("An error occurred.")

print("\n---------------------------------------------------\n")

# try except else clause - else is executed when no exception is raised
print("try except else clause - else is executed when no exception is raised")

try:
    result = 12 / 2            # number division
except ZeroDivisionError:      # catch ZeroDivisionError
    print("Cannot divide by zero!")  # statement to execute, for ZeroDivisionError
else:                          # else block, execute when no error occurs
    print(f"Result is: {result}") # else block statement to execute


try:
	number = 10                # declare and initialize a number
	del number                 # delete the number
except AttributeError as err:  # catch AttributeError
	print("error", err)        # statement to execute, for AttributeError
except NameError as err:       # catch NameError
	print("error", err)        # statement to execute, for NameError
else:                          # else block, execute when no error occurs
	print("else executed - only when no error is raised")

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

# try except finally nested clause
print("try except finally nested clause")

try:
    f = open("description.txt", "r")    # open file in read and text mode
except FileNotFoundError:               # catch FileNotFoundError
    print("File not found!")            # statement to execute, for FileNotFoundError
finally:                                # finally block, execute either error raised or not
    print("This runs whether an exception occurs or not.") # finally block statement


try:
	course_file = open("course_details.txt")
except FileNotFoundError as err:
	print("error", err)
finally:
	print("finally statement is always executed, irrespective of error raised or not")
	try:                       # try-catch block in finally block
		course_file.close()
	except NameError as err:
		print("error", err)
