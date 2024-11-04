# Program - for 2 level nested dictionary, swap the 1st level and 2nd level keys
# output will be 2 level nested dictionary, with swapped keys

# Test Case 1
# Input: input_dict = {"a": {1: ["omprosoft"]}, "b": {2: "online"}}
# Output: {1: {'a': ['omprosoft']}, 2: {'b': 'online'}}

# Test Case 2
# Input: input_dict = {"c1": {"l1": "Python"}, "c2": {"l2": "data science"}}
# Output: {'l1': {'c1': 'Python'}, 'l2': {'c2': 'data science'}}

# Test Case 3
# Input: input_dict = {"c1": {"l1": "Python"}, "b": {2: "online"}, 3: {"c": "training"}}
# Output: {'l1': {'c1': 'Python'}, 2: {'b': 'online'}, 'c': {3: 'training'}}

input_dict = {"c1": {"l1": "Python"}, "b": {2: "online"}, 3: {"c": "training"}}
output_dict = {}

for level1_keys in input_dict.keys():
    level2_dict = input_dict[level1_keys]
    for level2_keys in level2_dict.keys():
        output_dict[level2_keys] = dict({level1_keys: level2_dict[level2_keys]})

print(output_dict)