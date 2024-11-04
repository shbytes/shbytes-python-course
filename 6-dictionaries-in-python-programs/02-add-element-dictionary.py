
# add element using key
print("add element using key")
shbytes_dict = {"c1": "Python", "c2": "NumPy", "c3": "Pandas", "c4": "Java"}
print(shbytes_dict)    # print dictionary before add or update key-value
shbytes_dict["c5"] = "Machine Learning"  # add key-value pair, c5 key does not exists
print(shbytes_dict)    # print dictionary after add key-value
shbytes_dict["c4"] = "AI"  # update key-value pair, c4 key already exists
print(shbytes_dict)    # print dictionary after update key-value

print("\n---------------------------------------------------\n")

# add element using update method
print("add element using update method")
courses = {1: "Python", 2: "NumPy", 3: "Pandas", 4: "Java"}
print(courses)     # print dictionary before add or update key-value
courses.update({5: "Data Science"})   # add key-value pair, 5 key does not exists
print(courses)     # print dictionary after add key-value
courses.update({4: "AI"})    # update key-value pair, 4 key already exists
print(courses)     # print dictionary after update key-value

print("\n---------------------------------------------------\n")

# add & update multiple elements using update method
print("add & update multiple elements using update method")
courses = {1: "Python", 2: "NumPy", 3: "Pandas"}
print(courses)
courses.update(dict({4: "Data Science", 5: "ML"}))        # add multiple key-value pairs
print(courses)        # print dictionary after add key-value
courses.update(dict({2: "Machine Learning", 3: "AI"}))    # update multiple key-value pairs
print(courses)        # print dictionary after update key-value

print("\n---------------------------------------------------\n")

# add collection element
print("add collection element")
shbytes_dict = {1: "Python"}
print(shbytes_dict)
shbytes_dict["courses"] = "AWS", "Azure"    # add element with tuple value
print(shbytes_dict)

print("\n---------------------------------------------------\n")

# add nested Key value to a dictionary
print("add nested Key value to a dictionary")
shbytes_dict = {}
print(shbytes_dict)
shbytes_dict["courses"] = {"AWS", "Azure", "Python"}    # add element with set value
shbytes_dict["programs"] = ["online", "learning"]     # add element with list value
print(shbytes_dict)

print("\n---------------------------------------------------\n")

courses_dict = {1: "Python", 2: "NumPy", 3: "Pandas", 4: "Java"}
courses_dict.setdefault(2, "Power BI")  # does not add, as key 2 already exists
courses_dict.setdefault(5, "Power BI")  # Add key 5 with value
print(courses_dict)
# Elements in courses_dict => {1: 'Python', 2: 'NumPy', 3: 'Pandas', 4: 'Java', 5: 'Power BI'}

print("\n---------------------------------------------------\n")
import threading

courses_dict = {}
lock = threading.Lock()

def add_to_dictionary(key, value):
    with lock:
        courses_dict[key] = value

add_to_dictionary(1, "Python")
