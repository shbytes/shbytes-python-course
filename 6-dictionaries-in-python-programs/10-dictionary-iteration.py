# dictionary membership test
# dictionary iteration

# dictionary membership test
print("dictionary membership test")
courses = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}
print("c1" in courses)
print("c5" in courses)
print("c2" not in courses)

print("\n---------------------------------------------------\n")

# dictionary iteration
print("dictionary iteration")
courses = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}
for key in courses:
    print("key - ", key, "value - ", courses[key])
