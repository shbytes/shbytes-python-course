# Dictionary Comprehension

# dictionary comprehension
print("dictionary comprehension self multiplier")
multiplier_dict = {x: x*x for x in range(5)}
print(multiplier_dict)
print(type(multiplier_dict))

# equivalent code for dictionary comprehension
multiplier_dict = {}
for x in range(5):
    multiplier_dict[x] = x*x
print(multiplier_dict)

print("\n---------------------------------------------------\n")

# dictionary comprehension square number
print("dictionary comprehension square number")
square_dict = {x: x**2 for x in [12, 15, 17, 8, 9, 3, 6]}
print(square_dict)

print("\n---------------------------------------------------\n")

# dictionary comprehension with string
print("dictionary comprehension with string")
shbytes_dict = {x: x*3 for x in "shbytes"}
print(shbytes_dict)

print("\n---------------------------------------------------\n")

# dictionary comprehension with conditions
print("dictionary comprehension with conditions")
multiply_even_dict = {x: x*2 for x in [12, 15, 17, 8, 9, 3, 6] if x % 2 == 0}
print(multiply_even_dict)

print("\n---------------------------------------------------\n")

# dictionary comprehension - with keys and values
print("dictionary comprehension - with keys and values")
course_keys = ["c1", "c2", "c3", "c4"]
course_values = ["Python", "AWS", "Azure", "ML"]  

course_dict = {k: v for (k, v) in zip(course_keys, course_values)}
print(course_dict)

print("\n---------------------------------------------------\n")

# nested dictionary comprehension
print("nested dictionary comprehension")
nested_dict = {x: {y: y**2 for y in range(1, 4)} for x in "nest"}
print(nested_dict)

