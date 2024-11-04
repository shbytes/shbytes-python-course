
shbytes_list = ['Python', 'AWS', 'Java', 'Azure', 'Machine Learning', 'Java']

# remove elements from list - using remove function
print("remove elements from list - using remove function")
print(shbytes_list)
shbytes_list.remove('Java')
print(shbytes_list)

print("\n---------------------------------------------------\n")

# remove in mutable elements in list
nested_list = ['Python', 'AWS', 'Azure', [1, 2, 3]]
print("original nested list", nested_list)
nested_list[3].remove(2)
print("changed mixed list", nested_list)

print("\n---------------------------------------------------\n")

# Error - Case-sensitive element not in list
shbytes_list = ['Python', 'AWS', 'JAVA', 'Azure', 'Machine Learning']
print(shbytes_list)
#shbytes_list.remove('java')
print(shbytes_list)
print("\n---------------------------------------------------\n")

# Error - element not in list
shbytes_list = ['Python', 'AWS', 'Java', 'Azure', 'Machine Learning', 'Java']
print(shbytes_list)
#shbytes_list.remove('GoLang')
print(shbytes_list)
print("\n---------------------------------------------------\n")
del nested_list
#print(nested_list) 	#raise an error, new_list no longer exists

print("\n---------------------------------------------------\n")
number_list = [1, 2, 3, 2, 4, 2]
while 2 in number_list:
    number_list.remove(2)
print(number_list)  # Output: [1, 3, 4]

print("\n---------------------------------------------------\n")
number_list = [1, 2, 3, 2, 3]
# number_list.remove(4)  # Raises ValueError: list.remove(x): x not in list
# number_list.pop(5)     # Raises IndexError: pop index out of range
# del number_list[5]     # Raises IndexError: list index out of range

print("\n---------------------------------------------------\n")
original_list = [10, 12, 13, 14, 15]
new_list = [x for x in original_list if x % 2 == 0]
# original_list remains unchanged
print(original_list)  # Elements in original_list: [10, 12, 13, 14, 15]
print(new_list)       # Elements in new_list: [10, 12, 14]

print("\n---------------------------------------------------\n")
number_list = [10, 12, 13, 14, 15]
for index, value in enumerate(number_list[:]):  # Iterate over a copy
    if value % 2 == 0:
        number_list.remove(value)
print(number_list)  # Final elements in number_list: [13, 15]



