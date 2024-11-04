
# using intersection_update() method
print("intersection_update() method")
set_1 = {'Python','AWS','Java','Azure','ML'}
set_2 = {'Python', 'AWS', 'NumPy', 'Pandas', 'Matplotlib'}
set_intersection = set_1.intersection_update(set_2)
print(set_1)
print(set_2)
print(set_intersection)

print("\n---------------------------------------------------\n")

# using intersection() method
print("intersection() method")
set_1 = {'Python','AWS','Java','Azure','ML'}
set_2 = {'Python', 'AWS', 'NumPy', 'Pandas', 'Matplotlib'}
course_intersection = set_1.intersection(set_2)
print(set_1)
print(set_2)
print(course_intersection)

print("\n---------------------------------------------------\n")
# using intersection() method with three sets
print("using intersection() method with three sets")
set_1 = {10, 20, 30, 40}
set_2 = {20, 30, 40, 50, 60}
set_3 = {40, 50, 60, 70, 80, 90}
number_intersection_1 = set_1.intersection(set_2).intersection(set_3)
print("set_1 intersection set_2 intersection set_3 - ", number_intersection_1)

number_intersection_2 = set_1.intersection(set_2, set_3)
print("set_1 intersection set_2 intersection set_3 - ", number_intersection_2)

print("\n---------------------------------------------------\n")

# intersection using & operator
print("join of sets - intersection using & operator")
set_1 = {10, 20, 30, 40}
set_2 = {20, 30, 40, 50, 60}
set_3 = {30, 40, 50, 60, 70, 80, 90}
number_intersection_1 = set_1 & set_2
print("number_set_1 U number_set_2 - ", number_intersection_1)

number_intersection_2 = set_1 & set_2 & set_3
print("set_1 intersection set_2 intersection set_3 - ", number_intersection_2)

print("\n---------------------------------------------------\n")

set_1 = {10, 20, 30, 40}
set_2 = {54, 66, 78}

intersection_set = set_1 & set_2
print(intersection_set)  # Empty intersection_set = >set()

print("\n---------------------------------------------------\n")
set_1 = {32, "shbytes", (45, 78)}
set_2 = {"shbytes", 42, (45, 78)}

intersection_set = set_1 & set_2
print(intersection_set)  # Elements of intersection_set => {(45, 78), 'shbytes'}

print("\n---------------------------------------------------\n")
set_1 = {10, 20, 30, 40}
list_1 = [20, 30, 40]

#intersection_set_list = set_1 & list_1  # Direct intersection would raise TypeError:
# TypeError: unsupported operand type(s) for &: 'set' and 'list'

# Convert list to set
intersection_set = set_1 & set(list_1)
print(intersection_set)  # Elements in intersection_set => {40, 20, 30}
