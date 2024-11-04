
print("\n---------------------------------------------------\n")

# first class functions can be passed to another function as an argument

courses_list = []

# define a function to add course into a course list
def func_add_courses(course):
	courses_list.append(course)
	print(course, "added to the course list")

# define a function to check if course is valid or not
def func_course_valid(course, add_course_function): # takes course and another function as parameter
	if len(course) > 0:
		add_course_function(course)         # call the function given as an argument
	else:
		print("given course is not valid")

# call to function with valid course and another function as argument
func_course_valid("Power BI", func_add_courses)  # func_add_courses as argument
# call to function with invalid course and another function as argument
func_course_valid("", func_add_courses)          # func_add_courses as argument
# call to function with valid course and another function as argument
func_course_valid("Python", func_add_courses)    # func_add_courses as argument

print(courses_list) # Output => ['Power BI', 'Python']