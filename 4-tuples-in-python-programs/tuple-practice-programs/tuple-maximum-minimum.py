
# Program - Maximum and Minimum N number of elements in Tuple
# output should be tuple, with first N maximum numbers and next N minimum numbers
# Test Case 1
# Input: input_tuple = (3, 7, 11, 128, 92, 56), N = 2
# Output: (128, 92, 7, 3)

# Test Case 2
# Input: input_tuple = (13, 27, 21, 43, 56), N=1
# Output : (56, 13)

# Test Case 3
# Input: input_tuple = (113, 227, 21, 453, 566), N=2
# Output : (566, 453, 113, 21)

input_tuple = (113, 227, 21, 453, 566)
N = 2
input_tuple = sorted(input_tuple, reverse=True)
print(input_tuple)
output_tuple = input_tuple[0:N] + input_tuple[-N:]

print(output_tuple)

