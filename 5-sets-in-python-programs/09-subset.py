# using issubset() method
print("using issubset() method")
set_1 = {10, 20, 30}
set_2 = {10, 20, 30, 70, 80, 90}
subset_set12 = set_1.issubset(set_2)
subset_set21 = set_2.issubset(set_1)
print(set_1)
print(set_2)
print(subset_set12)
print(subset_set21)

print("\n---------------------------------------------------\n")

# using issubset() method - with empty set
print("using issubset() method - with empty set")
set_1 = set()
set_2 = set()
subset_set12 = set_1.issubset(set_2)
subset_set21 = set_2.issubset(set_1)
print(set_1)
print(set_2)
print(subset_set12)
print(subset_set21)

print("\n---------------------------------------------------\n")
# using subset (<=) operator
print("using subset (<=) operator")
set_1 = {10, 20, 30}
set_2 = {10, 20, 30, 70, 80, 90}
subset_set12 = set_1 <= set_2
subset_set21 = set_2 <= set_1
print(set_1)
print(set_2)
print(subset_set12)
print(subset_set21)

print("\n---------------------------------------------------\n")

# using strict subset (<) operator
print("using strict subset (<=) operator")
set_1 = {10, 20, 30}
set_2 = {10, 20, 30, 70, 80, 90}
subset_set12 = set_1 < set_2
subset_set21 = set_2 < set_1
print(set_1)
print(set_2)
print(subset_set12)
print(subset_set21)

print("\n---------------------------------------------------\n")


def custom_issubset(set_1, set_2):
    # Iterate through elements of set_1
    for element in set_1:
        # Check if any element of set_1 not in set_2
        if element not in set_2:
            return False
    return True

set_1 = {10, 20, 30}
set_2 = {10, 20, 30, 40, 50, 60}
set_3 = set()
set_4 = set()
print(custom_issubset(set_1, set_2))  # Output: True
print(custom_issubset(set_2, set_1))  # Output: False
print(custom_issubset(set_3, set_4))  # Output: True

print("\n---------------------------------------------------\n")
set_1 = {10, 20, 30}
list_1 = [10, 20, 30, 40]

print(set_1.issubset(list_1))  # True

dict_1 = {10: 'Python', 20: 'Power BI', 30: 'LLM'}
print(set_1.issubset(dict_1))  # True