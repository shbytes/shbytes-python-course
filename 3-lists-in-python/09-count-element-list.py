#count() elements in list
#list.count(object)

#count of numeric element
print("count of numeric element")
a = [4,2,3,4,9,4,2]
print(a)
print("count of 4 in list - ", a.count(4))

print("\n---------------------------------------------------\n")

#count of string element
print("count of string element")
b = ["AWS","Azure","Python","Python","Data Science","Java Advanced"]
print(b)
print("count of 'Python' in list - ", b.count("Python"))

print("\n---------------------------------------------------\n")

# count of case-sensitive string element
print("count of case-sensitive string element")
b = ["AWS","Azure","Python","Python","DataScience","Java Advanced"]
print(b)
print("count of case-sensitive 'python' in list - ", b.count("python"))

print("\n---------------------------------------------------\n")

# count of collection element
print("count of collection element")
c = [1,'Python','Azure', ['AWS',2]]
print(c)
print(c.count(['AWS',2]))
print(c.count([]))			#count of empty list

print("\n---------------------------------------------------\n")

# Error - count method passed with two parameters
print("Error - count method passed with two parameters")
e = ["AWS","Azure","Python","Python"]
print(e)
#print(e.count("Python", 2))

print("\n---------------------------------------------------\n")
elements_to_count = [22, 32, 22, 22, 52, 32]
counts = {element: elements_to_count.count(element) for element in elements_to_count}
print(counts)  # count of elements: {22: 3, 32: 2, 52: 1}
