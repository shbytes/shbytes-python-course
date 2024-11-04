# Program - add minimum value from nested tuple to each element of that nested element except the maximum value element
# output should be a nested tuple as per the input but with each element increment with minimum value
# Test Case 1
# Input: input_tuple = ((10, 20), (30, 40), (50, 60))
# Output: ((20, 20), (60, 40), (100, 60))

# Test Case 2
# Input: input_tuple = ((3, 5, 8), (6, 9, 10), (12, 14, 8))
# Output: ((6, 8, 8), (12, 15, 10), (20, 14, 16))

# Test Case 3
# Input: input_tuple = ((30, 15, 8), (86, 39, 20), (312, 45, 25))
# Output: ((30, 23, 16), (86, 59, 40), (312, 70, 50))

# input_tuple = ((30, 15, 8), (86, 39, 20), (312, 45, 25))
# output_list = []
# for n_element in input_tuple:
#     sorted_tuple = sorted(n_element)
#     minimum_value = sorted_tuple[0]
#     maximum_value = sorted_tuple[-1]
#     n_list = []
#     for x in n_element:
#         if x != maximum_value:
#             x += minimum_value
#         n_list.append(x)
#     output_list.append(tuple(n_list))
#
# print(tuple(output_list))

# input_tuple = ((30, 15, 8), (86, 39, 20), (312, 45, 25))
# output_list = []
# for n_element in input_tuple:
#     minimum_value = min(n_element)
#     maximum_value = max(n_element)
#     n_list = []
#     for x in n_element:
#         if x != maximum_value:
#             x += minimum_value
#         n_list.append(x)
#     output_list.append(tuple(n_list))
#
# print(tuple(output_list))

import sys
input_tuple = ((30, 15, 8), (86, 39, 20), (312, 45, 25))
output_list = []
for n_element in input_tuple:
    minimum_value = sys.maxsize
    maximum_value = -sys.maxsize - 1
    for x in n_element:
        if x < minimum_value:
            minimum_value = x
        if x > maximum_value:
            maximum_value = x
    n_list = []
    for x in n_element:
        if x != maximum_value:
            x += minimum_value
        n_list.append(x)
    output_list.append(tuple(n_list))

print(tuple(output_list))