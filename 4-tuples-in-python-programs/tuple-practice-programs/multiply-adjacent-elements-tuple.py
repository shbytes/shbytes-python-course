# Program - Multiple adjacent elements in a tuple
# output should be tuple, with each element multiplied with its adjacent element except the last element

# Test Case 1
# Input: input_tuple = (10, 20, 30, 40, 50, 60)
# Output: (200, 600, 1200, 2000, 3000)

# Test Case 2
# Input: input_tuple = (2, 4, 6, 8, 10, 12, 14)
# Output : (8, 24, 48, 80, 120, 168)

# Test Case 3
# Input: input_tuple = (3, 4, 6, 8, 10, 13)
# Output : (12, 24, 48, 80, 130)

input_tuple = (3, 4, 6, 8, 10, 13)
output_list = []
for x in range(len(input_tuple) - 1):
    output_list.append(input_tuple[x] * input_tuple[x + 1])

print(tuple(output_list))