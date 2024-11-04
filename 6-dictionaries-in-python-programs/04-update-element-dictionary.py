omprosoft = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}

# change element using key
print("change element using key")
print(omprosoft)
omprosoft["c4"] = "Machine Learning"
print(omprosoft)

print("\n---------------------------------------------------\n")

# update element using update method
print("update element using update method")
print(omprosoft)
omprosoft.update({"c4": "Data Science"})
print(omprosoft)

print("\n---------------------------------------------------\n")

# update element using update method
courses = {1: "Python", 2: "AWS", 3: "Azure", 4: "Java"}
print("update element using update method")
print(courses)
courses.update(dict({4: "Data Science", 5: "ML"}))
print(courses)
