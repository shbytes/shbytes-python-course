# dictionary built-in function - all()
print("dictionary built-in function - all()")
courses = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}
print(courses)
print(all(courses))
print(all(courses.values()))

numbers_dict = {0: "Python", 1: "AWS", 2: "Azure", 3: None}
print(numbers_dict)
print(all(numbers_dict))
print(all(numbers_dict.values()))

print("\n---------------------------------------------------\n")

# dictionary built-in function - any()
print("dictionary built-in function - any()")
numbers_dict = {0: "Python", 1: "AWS", 2: "Azure", 3: None}
print(numbers_dict)
print(any(numbers_dict))
print(any(numbers_dict.values()))

numbers_dict = {0: None, 0: None, 0: None}
print(numbers_dict)
print(any(numbers_dict))
print(any(numbers_dict.values()))


print("\n---------------------------------------------------\n")

# dictionary built-in function - len()
print("dictionary built-in function - len()")
courses = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}
print(courses)
print(len(courses))

empty_dict = {}
length = len(empty_dict)
print(length)

print("\n---------------------------------------------------\n")

# dictionary built-in function - sorted()
print("dictionary built-in function - sorted()")
courses = {"c3": "Python", "c2": "AWS", "c4": "Azure", "c1": "Java"}
print(courses)  # unsorted key-value pair
print(sorted(courses))  # sorting on keys in ascending order
print(sorted(courses, reverse=True))  # sorting on keys in descending order

print("\n---------------------------------------------------\n")

# dictionary built-in function - sorted()
print("dictionary built-in function - sorted()")
courses = {"c3": "Python", "c2": "AWS", "c4": "Azure", "c1": "Java"}
print(courses)    # unsorted key-value pair
print(sorted(courses.items(), key=lambda item: item[1]))  # sorting on values in ascending order
print(sorted(courses.items(), key=lambda item: item[1], reverse=True))  # sorting on values in descending order
