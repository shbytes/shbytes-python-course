# append element in the list using append method
sybytes_list = ['Python', 'AWS', 'Java', 'Azure']
print(sybytes_list)
sybytes_list.append("Machine Learning")
print(sybytes_list)

print("\n---------------------------------------------------\n")

# append element in nested element of a list
print("append in mutable elements in list")
nested_list = ['Python', 'AWS', 'Azure', [1, 2, 3]]
print("original nested list", nested_list)
nested_list[3].append(4)							# access index 3 element in list and append 4 in that list element
print("changed mixed list", nested_list)

print("\n---------------------------------------------------\n")

number_list = [1, 2, 3]
for item in number_list:
    number_list.append(item + 1)
    if len(number_list) > 6:
        break
print(number_list)  # Output: [1, 2, 3, 2, 3, 4, 3]

print("\n---------------------------------------------------\n")

number_list = []
sub_list = [1, 2, 3]
number_list.append(sub_list)
print(number_list)  # number_list will have [[1, 2, 3]]

sub_list.append(4)  # append element in sub_list
print(number_list)  # new element will also append to number_list [[1, 2, 3, 4]]

print("\n---------------------------------------------------\n")
datatype_list = []
datatype_list.append(23)         # Integer
datatype_list.append(43.54)      # Float
datatype_list.append("shbytes")   # String
datatype_list.append([53, 12, 0]) # List
datatype_list.append(True)      # Boolean
print(datatype_list)            # Final list: [23, 43.54, 'shbytes', [53, 12, 0], True]



