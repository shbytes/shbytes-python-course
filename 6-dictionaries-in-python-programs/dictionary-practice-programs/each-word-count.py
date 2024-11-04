# Program - for a given sentence, return a dictionary for each word count
# dictionary with word as key and its count as value

# Test Case 1
# Input: input_str = "sample string for string"
# Output: {'sample': 1, 'string': 2, 'for': 1}

# Test Case 2
# Input: input_str = "Shbytes Online Training in Python"
# Output: {'Shbytes': 1, 'Online': 1, 'Training': 1, 'in': 1, 'Python': 1}

# Test Case 3
# Input: input_str = "Python dictionary datatype"
# Output: {'Python': 1, 'dictionary': 1, 'datatype': 1}

input_str = "Python dictionary datatype"
output_dict = {}
for word in input_str.split(" "):
    try:
        current_count = output_dict[word]
    except KeyError as err:
        current_count = None

    if current_count is None:
        output_dict[word] = 1
    else:
        output_dict[word] += 1

print(output_dict)