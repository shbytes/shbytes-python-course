
courses_list = ["Generative AI", "Python", "Prompt Engineering", "Power BI"]
course_iter = iter(courses_list) # create iterator over the list

# infinite while loop
while True:
    try:
        element = next(course_iter)  # access next element from iterator
        print(element)
    except StopIteration:      # catch StopIteration error raise by iterator
        break                  # break the loop

print("\n---------------------------------------------------\n")

# Using range (returns an iterator)
for i in range(4):
    print(i)  # Output => 0 1 2 3

# Using map (returns an iterator)
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
square_numbers = map(lambda x: x ** 2, number_list)
print(list(square_numbers))  # Output => [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Use filter to get words longer than 3 characters
numbers_divisble_by_3 = filter(lambda number: number % 3 == 0, number_list)
# Convert the result to a list and print it
print(list(numbers_divisble_by_3))  # Output => [3, 6, 9]

cube_of_numbers = map(lambda x: x ** 3, number_list)
# Use zip to combine names and scores
zip_cube_of_numbers = zip(number_list, list(cube_of_numbers))
# Convert the result to a list and print it
print(list(zip_cube_of_numbers))
# Output => [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125), (6, 216), (7, 343), (8, 512), (9, 729)]

