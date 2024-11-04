# Program - Write a program to calculate the result for set mathematical operations
# print set operation result for operations - union, intersection, difference, symmetric difference

# Test Case 1
# Input: input_set1 = {1, 2, 3, 4, 5}, input_set2 = {4, 5, 6, 7, 8}
# Output:
# union_set = {1, 2, 3, 4, 5, 6, 7, 8}
# intersection_set = {4, 5}
# difference_set = {1, 2, 3}
# symmetric_difference_set = {1, 2, 3, 6, 7, 8}

# Test Case 2
# Input: input_set1 = {'a', 'b', 'c', 'd', 'e'}, input_set2 = {'d', 'e', 'f', 'g'}
# Output:
# union_set = {'b', 'f', 'c', 'd', 'e', 'g', 'a'}
# intersection_set = {'d', 'e'}
# difference_set = {'b', 'c', 'a'}
# symmetric_difference_set = {'b', 'f', 'c', 'g', 'a'}

input_set1 = {'a', 'b', 'c', 'd', 'e'}
input_set2 = {'d', 'e', 'f', 'g'}

union_set = input_set1.union(input_set2)
print(union_set)

intersection_set = input_set1.intersection(input_set2)
print(intersection_set)

difference_set = input_set1.difference(input_set2)
print(difference_set)

symmetric_difference_set = input_set1.symmetric_difference(input_set2)
print(symmetric_difference_set)