# unpacking tuple elements - without astrisk (*)
print("unpacking tuple elements - without astrisk (*)")
courses = ("AWS", "Azure", "Python")
(c1, c2, c3) = courses
print("course 1 - ", c1)
print("course 2 - ", c2)
print("course 3 - ", c3)

print("\n---------------------------------------------------\n")

# Error - unpacking tuple without astrisk (*) - extra elements
print("Error - unpacking tuple without astrisk (*) - extra elements")
courses = ("Python", "AWS", "Azure", "Java")
# (a1, a2, a3) = courses
try:
    (a1, a2, a3) = courses
except ValueError as err:
    print("error", err)

# Error - unpacking tuple with less elements
print("Error - unpacking tuple with less elements")
courses = ["Python", "NumPy"]
# (a1, a2, a3) = courses
try:
    (a1, a2, a3) = courses
except ValueError as err:
    print("error", err)

print("\n---------------------------------------------------\n")

# unpacking tuple - using asterisk* first variable
print("unpacking tuple - using asterisk* first variable")
courses = ("NumPy", "Pandas", "Python", "Java", "Data Science", "Machine Learning")
(*c1, c2, c3) = courses
print("course tuple c1 - ", c1)
print("course c2 - ", c2)
print("course c3 - ", c3)

print("\n---------------------------------------------------\n")

# unpacking tuple - using asterisk* in between
print("unpacking tuple - using asterisk* in between")
courses = ("NumPy", "Pandas", "Python", "Java", "Data Science", "Machine Learning")
(c1, *c2, c3) = courses
print("course c1 - ", c1)
print("course tuple c2 - ", c2)
print("course c3 - ", c3)

print("\n---------------------------------------------------\n")

# unpacking tuple - using asterisk* last variable
print("unpacking tuple - using asterisk* at last")
courses = ("NumPy", "Pandas", "Python", "Java", "Data Science", "Machine Learning")
(c1, c2, *c3) = courses
print("course c1 - ", c1)
print("course c2 - ", c2)
print("course tuple c3 - ", c3)

print("\n---------------------------------------------------\n")

# Error - unpacking tuple - using asterisk* multiple times
# print("Error - unpacking tuple - using asterisk* multiple times")
# courses = ("NumPy", "Pandas", "Python", "Java", "Data Science", "Machine Learning")
# try:
# 	(c1, *c2, *c3) = courses
# except SyntaxError as err:
# 	print("error", err)

print("\n---------------------------------------------------\n")

# Unpacking tuple with function arguments
print("Unpacking tuple with function arguments\n")


def fun_print_arguments(k, l, m, n):
    print("Number k - ", k)
    print("Number l - ", l)
    print("Number m - ", m)
    print("Number n - ", n)


number_tuple = (30, 40, 50, 60, 70)

# Passing tuple directly to function will give an error
print("\nPassing tuple directly to function will give an error")
try:
    fun_print_arguments(number_tuple)
except TypeError as err:
    print("error", err)

# Passing more elements than function arguments will give an error
print("\nPassing more elements than function arguments will give an error")
try:
    fun_print_arguments(*number_tuple)
except TypeError as err:
    print("error", err)

# Passing same number elements as function arguments
print("\nPassing same number elements as function arguments")
number_tuple = (30, 40, 50, 60)
fun_print_arguments(*number_tuple)

print("\n---------------------------------------------------\n")

a = 55
b = 105
# Swapping using tuple unpacking
a, b = b, a
print(a, b)  # After swap => a = 105, b = 55

print("\n---------------------------------------------------\n")

nested_tuple = (12, (22, 32), 24)
a, (b, c), d = nested_tuple
print(a, b, c, d)  # a = 12, b = 22, c = 32, d = 24

print("\n---------------------------------------------------\n")

number_list = [12, 22, 34]
number_tuple = (12, 22, 34)
a, b, c = number_list   # a = 12, b = 22, c = 34
x, y, z = number_tuple  # x = 12, y = 22, z = 34

print("\n---------------------------------------------------\n")
coordinates = [(11, 12), (33, 34), (56, 66)]
for x, y in coordinates:
    print(f"x: {x}, y: {y}")
# Following values will be printed:
# x: 11, y: 12
# x: 33, y: 34
# x: 56, y: 66

print("\n---------------------------------------------------\n")
def get_course():
    return ("Python", "Power BI", "LangChain")

course_1, course_2, course_3 = get_course()



