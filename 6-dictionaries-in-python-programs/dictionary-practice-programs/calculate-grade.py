# Program - for a given dictionary students list of score, calculate grade based on average score
# output should be a dictionary with student and its grade
# grade criteria:
# A - for score >= 90%
# B - for score >= 80%
# C - for score >= 70%
# D - for score >= 60%
# E - for score < 60%

# Test Case 1
# Input: input_dict = {"stu1": [76, 87, 65, 77], "stu2": [87, 57, 69, 74]}
# Output: {'stu1': 'C', 'stu2': 'C'}

# Test Case 2
# Input: input_dict = {"stu1": [76, 87, 85, 77], "stu2": [87, 67, 89, 74], "stu3": [87, 77, 89, 94]}
# Output: {'stu1': 'B', 'stu2': 'C', 'stu3': 'B'}

# Test Case 3
# Input: input_dict = {"stu1": [93, 87, 85, 97], "stu2": [82, 97, 83, 74], "stu3": [77, 74, 88, 93]}
# Output: {'stu1': 'A', 'stu2': 'B', 'stu3': 'B'}

# Test Case 4
# Input: input_dict = {"stu1": [73, 57, 55, 47], "stu2": [52, 77, 63, 54], "stu3": [87, 44, 58, 63]}
# Output: {'stu1': 'E', 'stu2': 'D', 'stu3': 'D'}

input_dict = {"stu1": [76, 87, 85, 77], "stu2": [87, 67, 89, 74], "stu3": [87, 77, 89, 94]}
output_dict = {}
for key in input_dict:
    stu_list = input_dict[key]
    total_score = 0
    for m in stu_list:
        total_score += m
    average_score = total_score / len(stu_list)

    if average_score >= 90:
        output_dict[key] = "A"
    elif average_score >= 80:
        output_dict[key] = "B"
    elif average_score >= 70:
        output_dict[key] = "C"
    elif average_score >= 60:
        output_dict[key] = "D"
    else:
        output_dict[key] = "E"

print(output_dict)

