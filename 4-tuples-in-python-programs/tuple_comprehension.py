shbytes_tuple = ('Python', 'AWS', 'Java', 'Azure', 'DataScience')

# creating a new tuple using condition
temp_list = []                   # Defined a new empty list
for element in shbytes_tuple:
  if "z" in element:                      # checking for condition
    temp_list.append(element)      # condition passed elements added to new list

new_shbytes_tuple = tuple(temp_list)    # new tuple is created from list
print(new_shbytes_tuple)                   # print elements in new filtered tuple

print("\n........................................")

# comprehension syntax =>
# new_shbytes_tuple = tuple(expression for item in iterable if condition == True)
# creating a new tuple using tuple comprehension without if condition
new_shbytes_tuple_4 = tuple(element for element in shbytes_tuple)
print(new_shbytes_tuple_4)

print("\n........................................")

# creating a new tuple using tuple comprehension with if-in condition
print("creating a new tuple using tuple comprehension with if-in condition")
new_shbytes_tuple_2 = tuple(element for element in shbytes_tuple if "z" in element)
print(new_shbytes_tuple_2)

# creating a new tuple using tuple comprehension with if-not condition
print("creating a new tuple using tuple comprehension with if-not condition")
new_shbytes_tuple_3 = tuple(element for element in shbytes_tuple if element != "Java")
print(new_shbytes_tuple_3)

# creating a new tuple using tuple comprehension and range function
print("creating a new tuple using tuple comprehension and range function")
new_shbytes_tuple_5 = tuple(element for element in range(10) if element > 3)
print(new_shbytes_tuple_5)

print("\n........................................")
gen = (x**2 for x in range(5))
tuple_obj = tuple(gen)
print(tuple_obj)  # Elements in tuple_obj => (0, 1, 4, 9, 16)

print("\n........................................")
tuple_obj = tuple((x, y) for x in range(2) for y in range(3))

# Elements in tuple => ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2))
print(tuple_obj)

print("\n........................................")
gen_expr = (x**2 for x in range(5))  # This creates a generator object
tuple_gen = tuple(gen_expr)  # tuple() converts generator to tuple
comprehension_list = [x**2 for x in range(5)]  # Comprehension directly creates a list

print("\n........................................")
tuple_obj = ('a', 'b', 'c', 'd')
enumerated_tuple = tuple(enumerate(tuple_obj))
# Elements in enumerated tuple => ((0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'))
print(enumerated_tuple)
