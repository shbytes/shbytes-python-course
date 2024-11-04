#Concatenate using '+' operator
print("Concatenate using '+' operator")
x = ["Python", "Java", "AWS", "Azure"]
y = [10,20,30]
z = x + y
print("x - ", x)
print("y - ", y)
print("z - ", z)

print("\n---------------------------------------------------\n")

#Concatenate using operator plugin
print("Concatenate using operator plugin")
import operator
a = [5,6,8]
b = ["C", "C++", "Java", "Python"]
c = operator.add(a,b)
print("a - ", a)
print("b - ", b)
print("c - ", c)

print("\n---------------------------------------------------\n")

#Concatenate using itertools.chain()
print("Concatenate using itertools.chain()")
import itertools 
x = ["Python", "Java", "AWS", "Azure"]
y = [10,20,30]
z = list(itertools.chain(x, y))
print("x - ", x)
print("y - ", y)
print("z - ", z)

print("\n---------------------------------------------------\n")

# Concatenate using extend(() method
print("Concatenate using extend(() method")
x = ["Python", "NumPy", "Pandas", "Scikit-learn"]
y = [40, 50, 60]
print("x - ", x)
print("y - ", y)
y.extend(x)
print("y - ", y)

print("\n---------------------------------------------------\n")

# unpacking - (*k, *l) - using asterisk*
print("unpacking - [*k, *l] - using asterisk*")
k = [55,60,89]
l = ["AWS", "Azure", "C++", "Java"]
m = [*k , *l]
print("k - ", k)
print("l - ", l)
print("m - ", m)

print("\n---------------------------------------------------\n")
list_1 = [12, 22, 34]
list_2 = [44, 56, 64]
concat_list = list_1 + list_2     # concat_list is a new list
print(concat_list)

print("\n---------------------------------------------------\n")
list_1 = [12, 22, 34]
list_1.extend([44, 56, 64])     # updated elements of list_1
print(list_1)

print("\n---------------------------------------------------\n")
import time

list_1 = list(range(1000000))
list_2 = list(range(1000000))

# Using the + operator
start = time.time()
concat_list = list_1 + list_2
print(f"Time taken using +: {time.time() - start} seconds")

# Using extend()
start = time.time()
list_1.extend(list_2)
print(f"Time taken using extend: {time.time() - start} seconds")

print("\n---------------------------------------------------\n")
list_1 = [15, 25, 35]
list_2 = [48, 58, 68]
for item in list_2:
    list_1.append(item)
print(list_1)        # Elements in list_1: [15, 25, 35, 48, 58, 68]


