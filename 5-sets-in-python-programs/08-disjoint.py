
# check set has common elements - using isdisjoint() method
print("check set has common elements - using isdisjoint() method")
set_1 = {10, 20, 30}
set_2 = {70, 80, 90}
set_3 = {10, 20, 30, 70, 80, 90}
isdisjoint_set12 = set_1.isdisjoint(set_2)
isdisjoint_set21 = set_2.isdisjoint(set_1)
print(set_1)
print(set_2)
print(isdisjoint_set12)
print(isdisjoint_set21)
print(set_3)
isdisjoint_set13 = set_1.isdisjoint(set_3)
print(isdisjoint_set13)

print("\n---------------------------------------------------\n")

# using isdisjoint() method - with empty sets
print("using isdisjoint() method - with empty sets")
set_1 = set()
set_2 = set()
empty_isdisjoint = set_1.isdisjoint(set_2)
print(set_1)
print(set_2)
print(empty_isdisjoint)

print("\n---------------------------------------------------\n")

# using isdisjoint() method - with set and dictionary
print("using isdisjoint() method - with set and dictionary")
set_1 = {"a", "b", "c"}
dict_1 = {"a": "Python", "b": "NumPy", "c": "PowerBI"}
dict_2 = {"Python": "a", "NumPy": "b", "PowerBI": "c"}
isdisjoint_set1_dict1 = set_1.isdisjoint(dict_1)
isdisjoint_set1_dict2 = set_1.isdisjoint(dict_2)
print(set_1)
print(dict_1)
print(dict_2)
print(isdisjoint_set1_dict1)
print(isdisjoint_set1_dict2)

print("\n---------------------------------------------------\n")

def custom_isdisjoint(set1, set2):
    # Iterate through elements of set1
    for element in set1:
        # Check if any element of set1 is in set2
        if element in set2:
            return False
    return True

# Example Usage
set1 = {10, 20, 30}
set2 = {40, 50, 60}
set3 = {30, 40, 50}

print(custom_isdisjoint(set1, set2))  # Output: True
print(custom_isdisjoint(set1, set3))  # Output: False

print("\n---------------------------------------------------\n")
set_1 = {10, 20, 30}
list_1 = [40, 50, 60]
print(set_1.isdisjoint(list_1))  # True

print("\n---------------------------------------------------\n")
set_1 = {10, 20, 30}
frozen_set = frozenset([40, 50, 60])
print(set_1.isdisjoint(frozen_set))  # True
print(frozen_set.isdisjoint(set_1))  # True

print("\n---------------------------------------------------\n")
list_of_sets = [{13, 23}, {35, 46}, {57, 68}]
all_disjoint = True

for index in range(len(list_of_sets)):
    for j in range(index + 1, len(list_of_sets)):
        if not list_of_sets[index].isdisjoint(list_of_sets[j]):
            all_disjoint = False
            break

print(all_disjoint)  # True
