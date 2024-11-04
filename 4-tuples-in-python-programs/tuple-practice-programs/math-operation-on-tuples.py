# Program - addition & multiplication on the number of elements in Tuple
# output should be a number as per the given operation on tuple elements
# Test Case 1
# Input: input_tuple = (10, 20, 30, 40, 50), operation = addition
# Output: 150

# Test Case 2
# Input: input_tuple = (10, 20, 30, 40, 50), operation = multiply
# Output: 12000000

# Test Case 3
# Input: input_tuple = (1, 2, 3, 4, 5), operation = addition
# Output: 15

# Solution - math-operation-on-tuples

import sys

complete_execution = "no"

while complete_execution == "no":

    print('Enter tuple element values')
    input_string = sys.stdin.readline().strip()
    input_tuple = tuple(int(x.strip()) for x in input_string.split(","))

    print('Enter operation')
    operation = str(sys.stdin.readline().strip())

    result = 0

    if operation == "addition":
        for x in input_tuple:
            result += int(x)
    else:
        result = 1
        for x in input_tuple:
            result *= int(x)
    print(result)

    print('complete the program execution - yes or no')
    complete_execution = sys.stdin.readline().strip()