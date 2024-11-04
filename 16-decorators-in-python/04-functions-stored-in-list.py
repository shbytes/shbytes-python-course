
print("\n---------------------------------------------------\n")

# first class functions can be stored in data structures like list, set, dictionary etc.

courses_list = []
# define a function to add course into a course list
def func_add_courses(course):
	courses_list.append(course)
	print(course, "added to the course list")

# create a key-value pair dictionary
func_dict = {func_add_courses:["Python", "Power BI", "Generative AI"]} # function as a key and list of courses
print(func_dict)
# Output => {<function func_add_courses at 0x000001E75835A2A0>: ['Python', 'Power BI', 'Generative AI']}

# loop through the keys of dictionary
for key in func_dict:             # Here key is the function in dictionary
	for course in func_dict[key]: # loop list stored at dictionary key
		key(course)               # call the function to add course to the course_list

print(courses_list) # Output => ['Python', 'Power BI', 'Generative AI']