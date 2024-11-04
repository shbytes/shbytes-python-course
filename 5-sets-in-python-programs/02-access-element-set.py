shbytes = {"Java","Azure","AWS","Python"}

# access element with for loop
print("access element with for loop");
print(shbytes)
for course in shbytes:
	print(course)

print("\n---------------------------------------------------\n")

# check for an element in a set
print("check for an element in a set");
print("AWS" in shbytes)
print("AWS" not in shbytes)

print("\n---------------------------------------------------\n")

# copy set to create another set
print("copy set to create another set");
print(shbytes)
courses = shbytes.copy()
print(courses)