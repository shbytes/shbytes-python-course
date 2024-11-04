# Concatenate using '+' operator
print("Concatenate using '+' operator")
x = ("Python", "Java", "AWS", "Azure")
y = (10,20,30)
z = x + y
print("x - ", x)
print("y - ", y)
print("z - ", z)

print("\n---------------------------------------------------\n")

# Concatenate by importing operator
print("Concatenate by importing operator")
import operator
a = (5,6,8)
b = ("C", "C++", "Java", "Python")
c = operator.add(a,b)
print("a - ", a)
print("b - ", b)
print("c - ", c)

print("\n---------------------------------------------------\n")

# Concatenate using itertools.chain()
print("Concatenate using itertools.chain()")
import itertools 
x = ("Python", "Java", "AWS", "Azure")
y = (10,20,30)
z = tuple(itertools.chain(x, y))
print("x - ", x)
print("y - ", y)
print("z - ", z)

print("\n---------------------------------------------------\n")

# unpacking - (*k, *l) - using asterisk*
print("unpacking - (*k, *l) - using asterisk*")
k = (55,60,89)
l = ("AWS", "Azure", "C++", "Java")
m = (*k , *l)
print("k - ", k)
print("l - ", l)
print("m - ", m)

print("\n---------------------------------------------------\n")

# multiply elements in tuple
print("multiply elements in tuple")
multiply_tuple = ("Python","AWS")*3
print(multiply_tuple)

print("\n---------------------------------------------------\n")
number_tuple = (14, 24, 36)
number_list = [46, 56, 68]

# This will raise a TypeError
# result = number_tuple + number_list   # TypeError: can only concatenate tuple (not "list") to tuple

print("\n---------------------------------------------------\n")
number_tuple_1 = (14, 24, 36)
number_tuple_2 = (64, 28, 39)

# Concatenating tuples
concat_tuple = number_tuple_1 + number_tuple_2

print(number_tuple_1)  # Elements in number_tuple_1 => (14, 24, 36)
print(number_tuple_2)  # Elements in number_tuple_2 => (64, 28, 39)
print(concat_tuple)    # Elements in concat_tuple => (14, 24, 36, 64, 28, 39)

print("\n---------------------------------------------------\n")
number_tuple = (14, 24, 36)

# Concatenating the tuple with itself 3 times
concat_tuple = number_tuple * 3

print(concat_tuple)  # Elements in concat_tuple => (14, 24, 36, 14, 24, 36, 14, 24, 36)


