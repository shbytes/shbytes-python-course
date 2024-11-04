
# using difference_update() method
print("using difference_update() method")
set_1 = {'Python','AWS','ML','Java','Azure'}
set_2 = {'Python', 'AWS', 'NumPy', 'Pandas', 'Matplotlib'}
set_difference = set_1.difference_update(set_2)
print(set_1)
print(set_2)
print(set_difference)

print("\n---------------------------------------------------\n")

# using difference() method
print("using difference() method")
set_1 = {'Python','AWS','ML','Java','Azure'}
set_2 = {'Python', 'AWS', 'NumPy', 'Pandas', 'Matplotlib'}
set1_difference_set2 = set_1.difference(set_2)
set2_difference_set1 = set_2.difference(set_1)
print(set_1)
print(set_2)
print(set1_difference_set2)
print(set2_difference_set1)

print("\n---------------------------------------------------\n")

# using negative (-) operator
print("using negative (-) operator")
set_1 = {'Python','AWS','ML','Java','Azure'}
set_2 = {'Python', 'AWS', 'NumPy', 'Pandas', 'Matplotlib'}
set1_difference_set2 = set_1 - set_2
set2_difference_set1 = set_2 - set_1
print(set_1)
print(set_2)
print(set1_difference_set2)
print(set2_difference_set1)

print("\n---------------------------------------------------\n")
set_1 = {16, 24, 38, 34, 35}
set_2 = {24, 35}
set_3 = {34, 35}
difference_set = set_1.difference(set_2, set_3)
print(difference_set) # elements in difference_set => {16, 38}

set_1 = {16, 24, 38, 34, 35}
set_2 = {24, 35}
set_3 = {34, 35}
difference_set = set_1 - set_2 - set_3
print(difference_set) # elements in difference_set => {16, 34, 38}

print("\n---------------------------------------------------\n")
frozenset_1 = frozenset([16, 24, 38, 34, 35])
frozenset_2 = frozenset([24, 35])
difference_frozenset = frozenset_1.difference(frozenset_2)
print(difference_frozenset) # output difference_frozenset => frozenset({16, 34, 38})

