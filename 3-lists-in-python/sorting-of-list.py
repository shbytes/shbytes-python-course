# sorting of alphanumeric list
alphanumeric_list = ['Python', 'AWS', 'Java', 'Azure', 'DataScience']
print(alphanumeric_list)
alphanumeric_list.sort()
print(alphanumeric_list)

print("\n---------------------------------------------------\n")
# sorting of numeric list
numeric_list = [23,45,78,13, 34, 89, 67]
print(numeric_list)
numeric_list.sort()
print(numeric_list)

print("\n---------------------------------------------------\n")
# sorting of alphanumeric list in descending order
alphanumeric_list = ['Python', 'AWS', 'Java', 'Azure', 'DataScience']
print(alphanumeric_list)
alphanumeric_list.sort(reverse = True)
print(alphanumeric_list)

print("\n---------------------------------------------------\n")
# sorting of numeric list in descending order
numeric_list = [23,45,78,13, 34, 89, 67]
print(numeric_list)
numeric_list.sort(reverse = True)
print(numeric_list)

print("\n---------------------------------------------------\n")
numbers_list = [42, 22, 27, 11, 34]
sorted_numbers = sorted(numbers_list)
print(numbers_list)         # original order of elements: [42, 22, 27, 11, 34]
print(sorted_numbers)  # sorted elements: [11, 22, 27, 34, 42]

print("\n---------------------------------------------------\n")
mixed_list = [32, 'shbytes', 22]
try:
    mixed_list.sort()
except TypeError as e:
    print(f"Error: {e}")  # Error: '<' not supported between instances of 'str' and 'int'

print("\n---------------------------------------------------\n")
courses_list = ['Python', 'Power BI', 'Java']
courses_list.sort(key=lambda x: len(x))   # sorting based on length of string
print(courses_list)  # sorted list - ['Java', 'Python', 'Power BI'] (sorted by length)

