# Exception handling in Python

class CustomError(Exception):        # CustomErro class inherits Exception class
    def __init__(self, message):     # init function for CustomError class
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This is a custom error.") # raise CustomError with message
except CustomError as e:                         # catch CustomError
    print(e)


print("\n---------------------------------------------------\n")

# user defined exception
print("user defined exception")

class Error(Exception):                  # base Error class for Exception
	"""Base class for exceptions in this module."""
	pass

class CourseNotFoundError(Error):        # CourseNotFoundError inherits Error class
    """Exception raised when course is not found.   # Docstring for CourseNotFoundError class

    Attributes:
        name -- input name for which the exception raised
        message -- explanation of the error
    """

    def __init__(self, name, message):             # init method for CourseNotFoundError class
        self.name = name
        self.message = message

class CourseNameError(Error):           # CourseNameError inherits Error class
    """Raised when an training is not in progress. # Docstring for CourseNotFoundError class

    Attributes:
        id -- id for the training
        status -- status of training
        message -- explanation of why the training is not in progress
    """

    def __init__(self, id, name, message):        # init method for CourseNameError class
        self.id = id
        self.name = name
        self.message = message

print("\n---------------------------------------------------\n")

try:
	raise(CourseNotFoundError("PHP", "Course is not started")) # raise CourseNotFoundError
except CourseNotFoundError as error:
	print("exception occur for - ", error.name, " with message - ", error.message)

print("\n---------------------------------------------------\n")

try:
	raise(CourseNameError("C5", "PHP4", "Name fo course provided is wrong")) # raise CourseNameError
except CourseNameError as error:
	print("exception occur for - ", error.id, error.name, " with message - ", error.message)
	
print("\n---------------------------------------------------\n")

# exception class in sequence from child to parent
print("exception class in sequence from child to parent")
class BaseError(Exception):       # BaseError class inherits Exception class
	print("in Parent2 class")

class ParentError(BaseError):
	print("in Parent1 class")     # ParentError class inherits BaseError class

class ChildError(ParentError):
	print("in Child class")       # ChildError class inherits ParentError class

for class_type in [ChildError, ParentError, BaseError]:  # for loop to raise all three exception
	try:
		raise class_type()
	except ChildError:                 # catch ChildError
		print("error in Child class")
	except ParentError:                # catch ParentError
		print("error in Parent class")
	except BaseError:                  # catch BaseError
		print("error in Base class")

# if order of exception handling is reversed, then output will be different