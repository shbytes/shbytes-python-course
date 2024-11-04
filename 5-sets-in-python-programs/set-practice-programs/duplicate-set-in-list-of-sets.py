# Program - find the duplicate sets in a list of sets
# output should be a element set duplicate in list elements

# Test Case 1
# Input: input_list = [{4, 9, 6, 1}, {6, 4, 1, 9}, {1, 3, 4, 3}, {1, 4, 3}, {7, 8, 9}]
# Output: {6, 4, 1, 9}

# Test Case 2
# Input: input_list = [{8, 9, 6, 3}, {6, 4, 10, 19}, {6, 9, 8, 3}, {1, 4, 3}]
# Output: {6, 9, 8, 3}

# Test Case 3
# Input: input_list = [{14, 9, 16}, {2, 4, 1, 7}, {1, 14, 3}, {16, 14, 9}]
# Output: {16, 9, 14}

# Test Case 4
# Input: input_list = [{24, 19, 26}, {12, 14, 41, 17}, {18, 314, 53}, {156, 184, 79}]
# Output: set()

input_list = [{14, 9, 16}, {2, 4, 1, 7}, {1, 14, 3}, {16, 14, 9}]
duplicate_set = set()

list_length = len(input_list)
for index in range(list_length):
    for n_index in range(index + 1, list_length):
        if len(input_list[index]) == len(input_list[n_index]):
            difference_set = input_list[index].difference(input_list[n_index])
            if len(difference_set) == 0:
                duplicate_set = input_list[index]
                break
    if len(duplicate_set) > 0:
        break

print(duplicate_set)



input_list = [{8, 9, 6, 3}, {6, 4, 10, 19}, {6, 9, 8, 3}, {1, 4, 3}]
duplicate_set = set()

list_length = len(input_list)
index = 0
while index < list_length:
    n_index = index + 1
    while n_index < list_length:
        if len(input_list[index]) == len(input_list[n_index]):
            difference_set = input_list[index].difference(input_list[n_index])
            if len(difference_set) == 0:
                duplicate_set = input_list[index]
                break
        n_index += 1
    if len(duplicate_set) > 0:
        break
    index += 1

print(duplicate_set)


input_list = [{24, 19, 26}, {12, 14, 41, 17}, {18, 314, 53}, {156, 184, 79}]
duplicate_set = set()

list_length = len(input_list)
for index in range(list_length):
    for n_index in range(index + 1, list_length):
        if len(input_list[index]) == len(input_list[n_index]):
            different_element_count = 0
            for element in input_list[index]:
                if element not in input_list[n_index]:
                    different_element_count += 1
                    break;
            if different_element_count == 0:
                duplicate_set = input_list[index]
                break
    if len(duplicate_set) > 0:
        break

print(duplicate_set)
