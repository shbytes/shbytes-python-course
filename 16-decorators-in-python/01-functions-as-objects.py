
print("\n---------------------------------------------------\n")

# first class functions can be stored in a variable
courses_list = []

# define a function to add course into a course list
def func_add_courses(course):
	courses_list.append(course)
	print(course, "added to the course list")

func_add_courses("Power BI")             # direct call to a function

variable_1 = func_add_courses  # function reference assigned to a variable
variable_1("Python")           # call to a function using variable reference

variable_2 = variable_1        # variable reference assigned to second variable
variable_2("Generative AI")    # call to a function using second variable reference

print(courses_list)  # Output => ['Power BI', 'Python', 'Generative AI']
