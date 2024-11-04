# Program - for a given set, get all possible differences between all elements of this set
# output should be a set of possible difference elements, except the value 0

# Test Case 1
# Input: input_set = {1, 2, 3, 4, 5}
# Output: {1, 2, 3, 4}

# Test Case 2
# Input: input_set = {1, 8, 3, 6, 9}
# Output: {1, 2, 3, 5, 6, 7, 8}

# Test Case 3
# Input: input_set = {1, 10, 12, 5, 2, 7, 8}
# Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

input_set = {1, 10, 12, 5, 2, 7, 8}
output_set = set()
for a in input_set:
    for b in input_set:
        if a != b and a < b:
            output_set.add(b - a)

print(output_set)