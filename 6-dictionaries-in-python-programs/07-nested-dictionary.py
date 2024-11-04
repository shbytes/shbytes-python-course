# dictionary of dictionaries
print("dictionary of dictionaries")
nested_dict = dict({"courses": {"c1": "Python", "c2": "AWS"}})
print(nested_dict)
print(type(nested_dict))

print("\n---------------------------------------------------\n")

# create nested dictionary
print("create nested dictionary")
course1_dict = {"name": "Python", "duration": 50}
course2_dict = {"name": "AWS", "duration": 52}
course3_dict = {"name": "Azure", "duration": 50}
courses_dict = {"c1": course1_dict, "c2": course2_dict, "c3": course3_dict}
print(courses_dict)

print("\n---------------------------------------------------\n")

# access elements in nested structure
print("access elements in nested structure")

student_dict = {
    'student_1': {
        'name': 'Johnson',
        'course': {'name': 'Data Science','subjects': ['Python', 'Data Structures', 'Machine Learning']}
    },
    'student_2': {
        'name': 'Smith',
        'course': {'name': 'Web Development', 'subjects': ['Java', 'Spring Boot', 'Microservices']}
    }
}

print(student_dict["student_1"]["course"])
print(student_dict["student_2"]["course"]["subjects"])
