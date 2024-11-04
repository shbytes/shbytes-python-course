# count() elements in tuple
# tuple.count(object)

# count of numeric element
print("count of numeric element")
a = (4,2,3,4,9,4,2)
print(a)
print(a.count(4))

print("\n---------------------------------------------------\n")

# count of string element
print("count of string element")
b = ("AWS","Azure","Python","Python","DataScience","Java Advanced")
print(b)
print(b.count("Python"))

print("\n---------------------------------------------------\n")

# count of case-sensitive string element
print("count of case-sensitive string element")
shbytes_tuple = ("AWS","Azure","Python","Python","DataScience","Java Advanced")
print(shbytes_tuple)
print(shbytes_tuple.count("python"))

print("\n---------------------------------------------------\n")

# count of collection element
print("count of collection element")
nested_tuple = (1,'Python','Azure', ['AWS',2])
print(nested_tuple)
print("count of collection - ", nested_tuple.count(['AWS',2]))    # count of collection object
print("count of empty tuple - ", nested_tuple.count(()))			# count of empty tuple

print("\n---------------------------------------------------\n")

# Error when two parameters are passed
print("error when two parameters are passed")
e = ("AWS","Azure","Python","Python")
print(e)
#print(e.count("Python", 2))

print("\n---------------------------------------------------\n")
mixed_tuple = (15, 'Python', 38.78, 'Power BI', {23, 45})
count_value = mixed_tuple.count(38.78)
print(count_value)