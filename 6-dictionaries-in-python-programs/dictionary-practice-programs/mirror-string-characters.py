# Program - given a small character string, mirror its characters from given index position
# input - string for characters to be mirrored, index value from where to start
# output - return a mirrored string
# mirror should be like - a - z, b - y, c - x, d - w

# Test Case 1
# Input: input_str = "originalstring", start_index = 3
# Output: "oritrmzohgirmt"

# Test Case 2
# Input: input_str = "pythondictionarydatatype", start_index = 6
# Output: "pythonwrxgrlmzibwzgzgbkv"

# Test Case 3
# Input: input_str = "onlinetraining", start_index = 1
# Output: "omormvgizrmrmt"

input_str = "onlinetraining"
start_index = 1

original_characters = "abcdefghijklmnopqrstuvwxyz"
mirrored_characters = "zyxwvutsrqponmlkjihgfedcba"
character_dict = dict(zip(original_characters,mirrored_characters))

output_str = ""
for index in range(len(input_str)):
    if index >= start_index:
        output_str += character_dict[input_str[index]]
    else:
        output_str += input_str[index]

print(output_str)
