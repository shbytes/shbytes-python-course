# Program - for a given list with set elements and another matching set,
# find the set element with maximum matching elements
# output should be a element set with maximum matching elements

# Test Case 1
# Input: input_set = [{1, 2, 3}, {1, 4, 5}, {1, 2, 5, 6}] and match_set = {1, 2, 6}
# Output: {1, 2, 5, 6}

# Test Case 2
# Input: input_set = [{21, 32, 12}, {1, 8, 5, 12}, {1, 7, 10, 5}, {11, 47, 70, 95}] and match_set = {1, 5, 12}
# Output: {1, 8, 5, 12}

# Test Case 3
# Input: input_set = [{21, 32, 12}, {1, 8, 5, 12}, {1, 17, 13, 5}] and match_set = {1, 5, 13, 17}
# Output: {1, 5, 13, 17}

# Test Case 4
# Input: input_set = [{121, 312, 132}, {11, 81, 54, 142}, {16, 187, 143, 52}] and match_set = {19, 95, 913, 917}
# Output: set()

input_list = [{1, 2, 3}, {1, 4, 5}, {1, 2, 5, 6}]
match_set = {1, 2, 6}

max_match_count = 0
max_match_count_element = set()
for element in input_list:
    intersection_set = element.intersection(match_set)
    element_count = len(intersection_set)
    if element_count > max_match_count:
        max_match_count = element_count
        max_match_count_element = element

print(max_match_count_element)


input_list = [{21, 32, 12}, {1, 8, 5, 12}, {1, 7, 10, 5}, {11, 47, 70, 95}]
match_set = {1, 5, 12}

max_match_count = 0
max_match_count_element = set()
index = 0
while index < len(input_list):
    intersection_set = input_list[index].intersection(match_set)
    element_count = len(intersection_set)
    if element_count > max_match_count:
        max_match_count = element_count
        max_match_count_element = input_list[index]
    index += 1

print(max_match_count_element)



input_list = [{121, 312, 132}, {11, 81, 54, 142}, {16, 187, 143, 52}]
match_set = {19, 95, 913, 917}

max_match_count = 0
max_match_count_element = set()
for element in input_list:
    element_count = 0
    for num in element:
        if num in match_set:
            element_count += 1
    if element_count > max_match_count:
        max_match_count = element_count
        max_match_count_element = element

print(max_match_count_element)