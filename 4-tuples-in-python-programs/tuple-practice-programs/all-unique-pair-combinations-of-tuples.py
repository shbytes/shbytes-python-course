# Program - Create all unique pair combinations of two tuples
# output should be a nested tuple with each element pair of two with element from each tuple
# each element of output should be unique without inclusion of order of elements

# Test Case 1
# Input: input_tuple1 = (10, 20), input_tuple2 = (30, 40)
# Output: ((10, 30), (10, 40), (20, 30), (20, 40), (30, 10), (30, 20), (40, 10), (40, 20))

# Test Case 2
# Input: input_tuple1 = (3, 5), input_tuple2 = (3, 8)
# Output: ((3, 3), (3, 8), (5, 3), (5, 8), (3, 5), (8, 3), (8, 5))

# Test Case 3
# Input: input_tuple1 = (6, 8, 8), input_tuple2 = (2, 4, 5, 5)
# Output: ((6, 2), (6, 4), (6, 5), (8, 2), (8, 4), (8, 5), (2, 6), (2, 8), (4, 6), (4, 8), (5, 6), (5, 8))

# input_tuple1 = (6, 8, 8)
# input_tuple2 = (2, 4, 5, 5)
# unique_input_tuple1 = tuple(set(input_tuple1))
# unique_input_tuple2 = tuple(set(input_tuple2))
#
# output_list = []
#
# for m in unique_input_tuple1:
#     for n in unique_input_tuple2:
#         output_list.append(tuple((m, n)))
#
# for n in unique_input_tuple2:
#     for m in unique_input_tuple1:
#         if m != n:
#             output_list.append(tuple((n, m)))
#
# print(tuple(output_list))


input_tuple1 = (6, 8, 8)
input_tuple2 = (2, 4, 5, 5)

unique_temp_list = []
for x in input_tuple1:
    if x not in unique_temp_list:
        unique_temp_list.append(x)
unique_input_tuple1 = tuple(unique_temp_list)

unique_temp_list = []
for x in input_tuple2:
    if x not in unique_temp_list:
        unique_temp_list.append(x)
unique_input_tuple2 = tuple(unique_temp_list)

output_list = []

for m in unique_input_tuple1:
    for n in unique_input_tuple2:
        output_list.append(tuple((m, n)))

for n in unique_input_tuple2:
    for m in unique_input_tuple1:
        if m != n:
            output_list.append(tuple((n, m)))

print(tuple(output_list))