
# join of sets - using union() method - remove duplicates
print("join of sets - using union() method - remove duplicates")
course_set_1 = {'Python','AWS','Java','Azure','ML'}
course_set_2 = {'Python', 'NumPy', 'Pandas', 'Matplotlib'}
courses = course_set_1.union(course_set_2)
print(course_set_1)
print(course_set_2)
print("course_set_1 U course_set_2 - ", courses)

print("\n---------------------------------------------------\n")

# using union() method with three sets
print("join of sets - using union() method with three sets")
number_set_1 = {10, 20, 30, 40}
number_set_2 = {30, 40, 50, 60}
number_set_3 = {60, 70, 80, 90}
number_union_1 = number_set_1.union(number_set_2).union(number_set_3)
print("number_set_1 U number_set_2 U number_set_3 - ", number_union_1)

number_union_2 = number_set_1.union(number_set_2, number_set_3)
print("number_set_1 U number_set_2 U number_set_3 - ", number_union_2)

print("\n---------------------------------------------------\n")

# union using | operator
print("join of sets - union using | operator")
number_set_1 = {10, 20, 30, 40}
number_set_2 = {30, 40, 50, 60}
number_set_3 = {60, 70, 80, 90}
number_union_1 = number_set_1 | number_set_2
print("number_set_1 U number_set_2 - ", number_union_1)

number_union_2 = number_set_1 | number_set_2 | number_set_3
print("number_set_1 U number_set_2 U number_set_3 - ", number_union_2)

print("\n---------------------------------------------------\n")
number_set = {10, 20, 30, 40}
empty_set = set()

union_set = number_set.union(empty_set)
print(union_set)  # Elements in union_set {10, 20, 30, 40}

print("\n---------------------------------------------------\n")
empty_set_1 = set()
empty_set_2 = set()

union_set = empty_set_1.union(empty_set_2)
print(union_set)  # union_set will be empty

print("\n---------------------------------------------------\n")
set_1 = {12, 22, 32}
set_2 = {32, 44, 55}
union_set = set_1.union(set_2)
# Verification
assert union_set == {12, 22, 32, 44, 55}, "Union operation failed"
print("Union operation successful!")
