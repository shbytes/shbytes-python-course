
# Syntax:  A.symmetric_difference_update(B)
# Parameters:
# The symmetric_difference takes a single “iterable” as an argument. Iterable should contain hashable object.
# Returns:
# This method returns None (which indicates absence of a return value). It only updates the set calling symmetric_difference_update() with the symmetric difference of sets.

# using symmetric_difference_update() method
print("symmetric_difference_update() method")
set_1 = {'Python','AWS','ML','Java','Azure'}
set_2 = {'PHP','UI','MongoDB','Java','Azure'}
difference_set12 = set_1.symmetric_difference_update(set_2)
print(set_1)
print(set_2)
print(difference_set12)

print("\n---------------------------------------------------\n")

# using symmetric_difference() method
print("symmetric_difference() method")
set_1 = {'Python','AWS','ML','Java','Azure'}
set_2 = {'PHP','UI','MongoDB','Java','Azure'}
difference_set12 = set_1.symmetric_difference(set_2)
difference_set21 = set_2.symmetric_difference(set_1)
print(set_1)
print(set_2)
print(difference_set12)
print(difference_set21)

print("\n---------------------------------------------------\n")
# using ^ operator
print("using ^ operator")
set_1 = {'Python','AWS','ML','Java','Azure'}
set_2 = {'PHP','UI','MongoDB','Java','Azure'}
difference_set12 = set_1 ^ set_2
difference_set21 = set_2 ^ set_1
print(set_1)
print(set_2)
print(difference_set12)
print(difference_set21)

print("\n---------------------------------------------------\n")
set_1 = {15, 28, 43}
set_2 = {15, 28, 43}
symmetric_difference_set12 = set_1 ^ set_2
print(symmetric_difference_set12)  # Elements after symmetric difference => set() or {}

print("\n---------------------------------------------------\n")
def ordered_symmetric_difference(list_1, list_2):
    list_symmetric_difference = []
    for element in list_1:
        if element not in list_2:
            list_symmetric_difference.append(element)
    for element in list_2:
        if element not in list_1:
            list_symmetric_difference.append(element)
    return list_symmetric_difference

# Example usage:
list_1 = [21, 42, 53]
list_2 = [53, 64, 85]
print(ordered_symmetric_difference(list_1, list_2))  # symmetric difference list => [21, 42, 64, 85]
