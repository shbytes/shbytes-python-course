sybytes_list = ['Python', 'AWS', 'Java', 'Azure', 'DataScience']

# creating a new list using condition
new_shbytes_list = []
for element in sybytes_list:
  if "z" in element:
    new_shbytes_list.append(element)

print(new_shbytes_list)

print("\n---------------------------------------------------\n")

# creating a new list using list comprehension without if condition
new_shbytes_list_4 = [element for element in sybytes_list]
print(new_shbytes_list_4)

print("\n---------------------------------------------------\n")

# creating a new list using list comprehension with if condition
# comprehension syntax =>
# new_shbytes_list = [expression for item in iterable if condition == True]
print("\ncreate a new list using list comprehension and if-in condition")
new_shbytes_list_2 = [element for element in sybytes_list if "z" in element]
print(new_shbytes_list_2)

print("\n---------------------------------------------------\n")

print("\ncreate a new list using list comprehension and if condition")
new_shbytes_list_3 = [element for element in sybytes_list if element != "Java"]
print(new_shbytes_list_3)

print("\n---------------------------------------------------\n")

# create a new list using list comprehension and range function
print("\ncreate a new list using list comprehension and range function")
new_shbytes_list_5 = [element for element in range(10) if element > 3]
print(new_shbytes_list_5)

print("\n---------------------------------------------------\n")

result = [course.upper() for course in ['Python','PowerBI','ML','AI'] if len(course) < 8]
print(result)

print("\n---------------------------------------------------\n")

nested_list = [[x, y] for x in [2, 4, 6] for y in [4, 16, 36]]
print(nested_list)

nested_list = []
for x in [2, 4, 6]:
    for y in [4, 16, 36]:
        nested_list.append([x, y])

print("\n---------------------------------------------------\n")
list_of_lists = [[2, 4, 6], [8, 10, 12], [14, 16, 19]]
flatten_list = [item for sub_list in list_of_lists for item in sub_list]
print(flatten_list)

print([x**2 for x in range(10)])
print((x**2 for x in range(10)))

