course_list = ['Python', 'AWS', 'Java', 'Azure', 'Data Science']
for course in course_list:
    print(course)

print("\n---------------------------------------------------\n")

for number in range(10):
    if number % 2 == 0:
        print(number)

print("\n---------------------------------------------------\n")
for letter in "shbytes":
    print(letter)

print("\n---------------------------------------------------\n")
print("dictionary iteration")
courses = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}
for key in courses:
    print("key - ", key, "value - ", courses[key])

print("\n---------------------------------------------------\n")
course_tuple = ('Python', 'Java', 'Data Science')
for course in course_tuple:
    print(course)
else:
    print("for loop completed")


print("\n---------------------------------------------------\n")
print("Nested for loop")
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")


print("\n---------------------------------------------------\n")
for num in range(8):
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)

print("\n---------------------------------------------------\n")
for num in range(6):
    if num == 2:
        continue  # Skip the iteration when num is 2
    print(num)

print("\n---------------------------------------------------\n")
for num in range(4):
    if num == 2:
        pass  # Do nothing, just pass
    print(num)
