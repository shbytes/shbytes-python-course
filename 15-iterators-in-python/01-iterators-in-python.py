
# Example of iterable and iterator
# This list is an iterable
courses_list = ["Generative AI", "Python", "Prompt Engineering", "Power BI"]

# using iter we created an iterator over the list
iterator = iter(courses_list)

# access elements from iterable - Uusing iterator next() function
print(next(iterator))  # Output => Generative AI
print(next(iterator))  # Output => Python
print(next(iterator))  # Output => Prompt Engineering

# next(iter_obj) is same as iter_obj.__next__()
print(iterator.__next__())  # Output => Power BI
# Raises StopIteration

print("\n---------------------------------------------------\n")

courses_list = ["AWS", "Python", "Azure"]

print("Create Iterator for list")

course_iter = iter(courses_list)

print("\n---------------------------------------------------\n")

print("Calling next() method - to print next element value")
print(next(course_iter))

print(next(course_iter))

print("\n---------------------------------------------------\n")

# next(iter_obj) is same as iter_obj.__next__()
print("next(iter_obj) is same as iter_obj.__next__()")

print(course_iter.__next__())

# No item is left, so this will raise StopIteration error,
next(course_iter)

print("\n---------------------------------------------------\n")