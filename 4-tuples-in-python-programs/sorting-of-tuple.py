# sorting of alphanumeric tuple
alphanumeric_tuple = ('Python', 'AWS', 'Java', 'Azure', 'DataScience')
print(alphanumeric_tuple)
temp_list = list(alphanumeric_tuple)
temp_list.sort()
alphanumeric_tuple = tuple(temp_list)
print(alphanumeric_tuple)

# sorting of numeric tuple
numeric_tuple = (23,45,78,13, 34, 89, 67)
print(numeric_tuple)
temp_list = list(numeric_tuple)
temp_list.sort()
numeric_tuple = tuple(temp_list)
print(numeric_tuple)

# sorting of alphanumeric tuple in descending order
alphanumeric_tuple = ('Python', 'AWS', 'Java', 'Azure', 'DataScience')
print(alphanumeric_tuple)
temp_list = list(alphanumeric_tuple)
temp_list.sort(reverse = True)
alphanumeric_tuple = tuple(temp_list)
print(alphanumeric_tuple)

# sorting of numeric tuple in descending order
numeric_tuple = (23,45,78,13, 34, 89, 67)
print(numeric_tuple)
temp_list = list(numeric_tuple)
temp_list.sort(reverse = True)
numeric_tuple = tuple(temp_list)
print(numeric_tuple)

print("\n---------------------------------------------------\n")
# Define a tuple
original_tuple = (42, 11, 31, 21, 52)

# Convert the tuple to a list
sorted_list = sorted(original_tuple)

# Convert the sorted list back to a tuple
sorted_tuple = tuple(sorted_list)

# Convert the tuple to a list and sort it in descending order
desc_sorted_list = tuple(sorted(original_tuple, reverse=True))

print(f"Original tuple: {original_tuple}")  # (42, 11, 31, 21, 52)
print(f"Sorted tuple: {sorted_tuple}")  # (11, 21, 31, 42, 52)
print(f"Descending sorted tuple: {desc_sorted_list}")  # (52, 42, 31, 21, 11)

print("\n---------------------------------------------------\n")
# Define a tuple with mixed types
mixed_tuple = (15, 'Python', 38.78, 'Power BI')

try:
    # Attempt to sort the tuple directly
    sorted_mixed_tuple = tuple(sorted(mixed_tuple))
    print(f"Sorted mixed tuple: {sorted_mixed_tuple}")
except TypeError as e:
    print(f"Error occurred: {e}")

# Sort by converting all elements to strings
sorted_mixed_tuple = tuple(sorted(mixed_tuple, key=str))
print(f"Sorted mixed tuple as strings: {sorted_mixed_tuple}")




