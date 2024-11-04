# function => block of code to run when it is called
# function takes arguments, known as parameters to pass data
# function can return value as a result

print("parameter => variable listed inside the parentheses in function definition")
print("argument  => value sent to the function when it is called")

# function arguments - pass by reference or pass by value
print("function arguments - pass by reference or pass by value")
def courses_reference(courses_list, course):
	print(len(courses_list))
	courses_list.append(course)   # modify mutable object - will affect original object

courses = ["AWS","Python","ML","DevOps"]    # list - mutable object
print("courses list before function call - ", courses)
courses_reference(courses, "Azure")  # list (mutable object) - pass by reference as function argument
print("courses list after function call - ", courses)  # courses elements after append
print("course added to - same reference of courses list")

print("\n---------------------------------------------------\n")

def modify_number(n):
    n += 10  # Creates a new integer, does not affect the original

number = 5
modify_number(number) # number (immutable) argument - pass by value
print(number)  # Output => 5

print("\n---------------------------------------------------\n")

# function arguments - pass by reference, with broken reference
print("function arguments - pass by reference, with broken reference")
def courses_broken_reference(courses_list, course):
	print(len(courses_list))   # length of original list
	# creating local variable with same name. This will break the reference to argument object
	courses_list = ["AWS","Python","ML","DevOps"]
	courses_list.append(course) # element added to the local list object, argument object remains unchanged

courses = ["AWS","Python","ML","DevOps"]    # list - mutable object
print("courses list before function call - ", courses)
courses_broken_reference(courses, "Azure") # list (mutable object) - pass by reference as function argument
print("courses list after function call - ", courses) # courses elements after append
print("course added was in - broken reference of courses list")

print("\n---------------------------------------------------\n")

# pass by reference - with wrapping immutable object
print("pass by reference - with wrapping immutable object")
def modify_number(n):
    n[0] += 10  # Modifies the element inside the list

number = [5]  # Integer wrapped in a list
modify_number(number)
print(number[0])  # Output => 15
