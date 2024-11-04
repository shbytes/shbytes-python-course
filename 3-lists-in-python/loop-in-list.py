sybytes_list = ['Python', 'AWS', 'Java', 'Azure', 'Data Science']

# for loop with list elements
for element in sybytes_list:
    print(element)

print("\n...............................\n")

# for loop with list using index
for index in range(len(sybytes_list)):
    print(sybytes_list[index])

print("\n...............................\n")

# while loop with list using index
index = 0
while index < len(sybytes_list):
    print(sybytes_list[index])
    index += 1

print("\n...............................\n")

# loop through the list using list comprehension
[print(x) for x in sybytes_list]

print("\n...............................\n")

# creating lists in a loop
shbytes_list = ['Python']
for i in range(5):
    shbytes_list = [shbytes_list]
    print(shbytes_list)


# creating a new list using condition
sybytes_list = ['Python', 'AWS', 'Java', 'Azure', 'DataScience']
new_shbytes_list = []                     # Defined a new empty list

for element in sybytes_list:
  if "z" in element:                      # checking for condition
    new_shbytes_list.append(element)      # condition passed elements added to new list

print(new_shbytes_list)                   # print elements in new filtered list

print("\n...............................\n")
id_list = [1, 2, 3, 4, 5]
sybytes_list = ['Python', 'AWS', 'Java', 'Azure', 'Data Science']

for element_1, element_2 in zip(id_list, sybytes_list):
    print(element_1, element_2)

print("\n...............................\n")
id_list = [1, 2, 3, 4, 5]
sybytes_list = ['A', 'B', 'D', 'C', 'E']
for element in id_list:
    print(element)
    for element_3 in shbytes_list:
        print(element_3)