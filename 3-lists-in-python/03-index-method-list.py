# list.index(element, start, end)
# element - the element to be searched
# start (optional) - start searching from this index
# end (optional) - search the element up to this index

shbytes_list = ["DataScience", "Azure", "AWS", "Python", 14, 15, 16]

# index of an element in list
print(shbytes_list)
y = shbytes_list.index("Python")
print(y)
y = shbytes_list.index(15)
print(y)

print("\n---------------------------------------------------\n")

# index of an element, start search from given index in list
print(shbytes_list)
y = shbytes_list.index("AWS", 1)               # Use index(element, start) method
print(y)

print("\n---------------------------------------------------\n")

# index of an element, start search from given index and search upto end index in list
print(shbytes_list)
y = shbytes_list.index("AWS", 1, 3)             # Use index(element, start, end) method
print(y)
y = shbytes_list.index(14, 1, 6)
print(y)

print("\n---------------------------------------------------\n")

# index of an element, which is not present in list
print(shbytes_list)
#y = shbytes_list.index("Java")                 # Use index() method
print(y)

print("\n---------------------------------------------------\n")
course_list = [100, 'Python', 23.33, 'Power BI', "23.33"]
print(course_list.index(23.33))  # Output: 1
print(course_list.index("23.33"))     # Output: 2

print("\n---------------------------------------------------\n")
def custom_index(elements_list, element, start=0, end=None):
    if end is None:
        end = len(elements_list)

    for i in range(start, end):
        if elements_list[i] == element:
            return i
    raise ValueError(f"{element} is not in list")

course_list = ['Java', 'Python', 'Power BI', 'Machine Learning']
index = custom_index(course_list, 'Python')
print(index)     # returns: 1