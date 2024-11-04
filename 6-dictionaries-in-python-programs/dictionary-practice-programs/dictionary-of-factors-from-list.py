# Program - From the given list of numbers, calculate a dictionary of factors from list
# output should be a dictionary for keys from 1 to maximum value in list.
# Every key should have value list of factor numbers from existing list

# Test Case 1
# Input: input_list = [3, 4, 7, 9, 10]
# Output: {1: [3, 4, 7, 9, 10], 2: [4, 10], 3: [3, 9], 4: [4], 5: [10], 6: [], 7: [7], 8: [], 9: [9], 10: [10]}

# Test Case 2
# Input: input_list = [2, 4, 6, 8]
# Output: {1: [2, 4, 6, 8], 2: [2, 4, 6, 8], 3: [6], 4: [4, 8], 5: [], 6: [6], 7: [], 8: [8]}

# Test Case 3
# Input: input_list = [2, 4, 5]
# Output: {1: [2, 4, 5], 2: [2, 4], 3: [], 4: [4], 5: [5]}


input_list = [2, 4, 5]

sorted_input_list = sorted(input_list)
output_dict = {}

for key_num in range(sorted_input_list[-1]):
    key_num += 1
    output_dict[key_num] = []
    for factor_num in input_list:
        if factor_num % key_num == 0:
            output_dict[key_num].append(factor_num)
    # want to remove the empty list keys
    # if len(output_dict[key_num]) == 0:
    #    output_dict.pop(key_num)

print(output_dict)