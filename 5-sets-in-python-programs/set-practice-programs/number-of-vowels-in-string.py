# Program - count number of vowels in a given string
# output should be a element set with maximum matching elements

# Test Case 1
# Input: input_string = "omprosoft"
# Output: 3

# Test Case 2
# Input: input_string = "omprosoft online training"
# Output: 9

# Test Case 3
# Input: input_string = "vowels in a string"
# Output: 5

input_string = "vowels in a string"

vowels_set = set("aeiouAEIOU")
vowels_count = 0

for character in input_string:
    if character in vowels_set:
        vowels_count += 1

print(vowels_count)
