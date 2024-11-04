
shbytes_list = ['Python', 'AWS', 'Java', 'Azure']

# change list values
print(shbytes_list)
shbytes_list[2] = 'Machine Learning'
print(shbytes_list)

print("\n---------------------------------------------------\n")

# change mutable elements in list
print("change mutable elements in list")
nested_list = ['Python', 'AWS', 'Azure', [1, 2, 3]]
print("original nested list", nested_list)
nested_list[3][2] = 4
print("changed mixed list", nested_list)

print("\n---------------------------------------------------\n")
number_list = [10, 20, 30, 40, 50]
number_list[1:4] = [200, 300, 400]
print(number_list)     # Final number_list elements: [10, 200, 300, 400, 50]

print("\n---------------------------------------------------\n")
number_list = [10, 20, 30, 20, 40]
for index in range(len(number_list)):
    if number_list[index] == 20:
        number_list[index] = 100
print(number_list)  # Output: [10, 100, 30, 100, 40]

print("\n---------------------------------------------------\n")
mixed_list = [10, '20', 30, 'forty']
# Replace only integers equal to 10
for index in range(len(mixed_list)):
    if isinstance(mixed_list[index], int) and mixed_list[index] == 10:
        mixed_list[index] = 100
print(mixed_list)      # Final elements in mixed_list: [100, '20', 30, 'forty']

print("\n---------------------------------------------------\n")
number_list = [6,13,22,40]
for index in reversed(range(len(number_list))):
    if index > 0:
        number_list[index] = number_list[index] - number_list[index - 1]
print(number_list)