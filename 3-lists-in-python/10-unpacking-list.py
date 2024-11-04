# unpacking list elements
print("unpacking list elements")
courses = ["NumPy", "Pandas", "Python"]
(c1, c2, c3) = courses
print("course 1 - ", c1)
print("course 2 - ", c2)
print("course 3 - ", c3)

print("\n---------------------------------------------------\n")

# Error - unpacking list with extra elements
print("Error - unpacking list with extra elements")
courses = ["Python", "NumPy", "Pandas", "Java"]
try:
	(a1, a2, a3) = courses
except ValueError as err:
	print("error", err)

# Error - unpacking list with less elements
print("Error - unpacking list with less elements")
courses = ["Python", "NumPy"]
try:
	(a1, a2, a3) = courses
except ValueError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

# unpacking list - using asterisk* first variable
print("unpacking list - using asterisk* first variable")
courses = ["NumPy", "Pandas", "Python", "Java", "Data Science", "Machine Learning"]
(*c1, c2, c3) = courses
print("course list c1 - ", c1)
print("course c2 - ", c2)
print("course c3 - ", c3)

print("\n---------------------------------------------------\n")

# unpacking list - using asterisk* in between
print("unpacking list - using asterisk* in between")
courses = ["NumPy", "Pandas", "Python", "Java", "Data Science", "Machine Learning"]
(c1, *c2, c3) = courses
print("course c1 - ", c1)
print("course list c2 - ", c2)
print("course c3 - ", c3)

print("\n---------------------------------------------------\n")

# unpacking list - using asterisk* last variable
print("unpacking list - using asterisk* at last")
courses = ["NumPy", "Pandas", "Python", "Java", "Data Science", "Machine Learning"]
(c1, c2, *c3) = courses
print("course c1 - ", c1)
print("course c2 - ", c2)
print("course list c3 - ", c3)

print("\n---------------------------------------------------\n")

# Error - unpacking list - using asterisk* multiple times
# print("Error - unpacking list - using asterisk* multiple times")
# courses = ["NumPy", "Pandas", "Python", "Java", "Data Science", "Machine Learning"]
# try:
# 	(c1, *c2, *c3) = courses
# except SyntaxError as err:
# 	print("error", err)

print("\n---------------------------------------------------\n")

# Unpacking list with function arguments
print("Unpacking list with function arguments\n")
def fun_print_arguments(k, l, m, n):
	print("Number k - ", k)
	print("Number l - ", l)
	print("Number m - ", m)
	print("Number n - ", n)

print("\n---------------------------------------------------\n")
number_list = [30, 40, 50, 60, 70]

# Passing list directly to function will give an error
print("\nPassing list directly to function will give an error")
try:
	fun_print_arguments(number_list)
except TypeError as err:
	print("error", err)

print("\n---------------------------------------------------\n")
# Passing more elements than function arguments will give an error
print("\nPassing more elements than function arguments will give an error")
try:
	fun_print_arguments(*number_list)
except TypeError as err:
	print("error", err)

print("\n---------------------------------------------------\n")
# Passing same number elements as function arguments
print("\nPassing same number elements as function arguments")
number_list = [30, 40, 50, 60]
fun_print_arguments(*number_list)


print("\n---------------------------------------------------\n")
nested_list = [11, [21, 23, 34], [34, 45, 56]]

a, (*b, c), (d, *e) = nested_list

print(a)  # value of a = 11
print(b)  # value of b = [21, 23]
print(c)  # value of c = 34
print(d)  # value of d = 34
print(e)  # value of e = [45, 56]

print("\n---------------------------------------------------\n")
def func(*args):
    print(args)

func(11, 12, 34)     # print from func argumenets = (11, 12, 34)

print("\n---------------------------------------------------\n")
def add(x, y, z):
    return x + y + z

values = [11, 21, 34]
result = add(*values)  # Unpacks list into 3 arguments
print(result)    # Total sum of elements: 66

print("\n---------------------------------------------------\n")
def func(**kwargs):
    print(kwargs)

func(a=12, b=22, c=32)  # kwargs elements - {'a': 12, 'b': 22, 'c': 32}

print("\n---------------------------------------------------\n")
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(12, 22, 32, a=44, b=54)  # args elements - (1, 2, 3)
                              # kwargs elements - {'a': 4, 'b': 5}

