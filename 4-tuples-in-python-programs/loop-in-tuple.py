shbytes_tuple = ('Python', 'AWS', 'Java', 'Azure', 'DataScience')

# loop in tuple element one-by-one using for loop
for element in shbytes_tuple:
    print(element)


# loop in tuple using element index within for loop
for index in range(len(shbytes_tuple)):
    print(shbytes_tuple[index])


# loop in tuple using while loop
index = 0
while index < len(shbytes_tuple):
    print(shbytes_tuple[index])
    index += 1


# creating a new tuple using condition
shbytes_tuple = ('Python', 'AWS', 'Java', 'Azure', 'DataScience')
temp_list = []                   # Defined a new empty list

for element in shbytes_tuple:
  if "z" in element:                      # checking for condition
    temp_list.append(element)      # condition passed elements added to new list

new_shbytes_tuple = tuple(temp_list)    # new tuple is created from list
print(new_shbytes_tuple)                   # print elements in new filtered tuple

# loop through the tuple usng tuple comprehension
[print(x) for x in shbytes_tuple]