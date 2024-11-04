
# remove element from set - using remove() method
print("remove element from set - using remove() method")
numbers_set = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(numbers_set)
number = numbers_set.remove(40)
print(numbers_set)
print(number)

print("\n---------------------------------------------------\n")

# remove element from set - raise error if element does not exists
print("remove element from set - raise error if element does not exists")
numbers_set = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(numbers_set)
# numbers_set.remove(100)
try:
	numbers_set.remove(100)
except KeyError as err:
	print("error", err)
	print(numbers_set)

print("\n---------------------------------------------------\n")

# remove element from set - using discard() method
print("remove element from set - using discard() method")
numbers_set = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(numbers_set)
number = numbers_set.discard(40)
print(numbers_set)
print(number)

print("\n---------------------------------------------------\n")

# discard() method does not raise error if element does not exists
print("discard() method does not raise error if element does not exists")
numbers_set = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(numbers_set)
number = numbers_set.discard(100)
print(numbers_set)
print(number)

print("\n---------------------------------------------------\n")

# pop() method to take out an element - order is not defined
print("pop() method to take out an element - order is not defined")
numbers_set = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(numbers_set)
number = numbers_set.pop()
print(numbers_set)
print(number)

print("\n---------------------------------------------------\n")

# clear() method to remove all elements from set
print("clear() method to remove all elements from set")
numbers_set = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(numbers_set)
number = numbers_set.clear()
print(numbers_set)
print(number)

print("\n---------------------------------------------------\n")

# del will delete the set itself
print("del will delete the set itself")
numbers_set = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(numbers_set)
del numbers_set
# print(numbers_set)

print("\n---------------------------------------------------\n")

numbers_set = {12, 22, 33, 46, 58}
elements_to_remove = {22, 33}
for element in elements_to_remove:
	numbers_set.discard(element)  # or we can use numbers_set.remove(element)
print(numbers_set)   # Elements remain in numbers_set {58, 12, 46}

numbers_set = {12, 22, 33, 46, 58}
elements_to_remove = {22, 33}
numbers_set = numbers_set - elements_to_remove
print(numbers_set)   # Elements remain in numbers_set {58, 12, 46}

numbers_set = {12, 22, 33, 46, 58}
elements_to_remove = {22, 33}
numbers_set.difference_update(elements_to_remove)
print(numbers_set)   # Elements remain in numbers_set {58, 12, 46}

print("\n---------------------------------------------------\n")

empty_set = set()    # an empty set
try:
    empty_set.pop()  # This will raise a KeyError
except KeyError as error:
    print("KeyError raised - ", error)

print("\n---------------------------------------------------\n")
set = {14, 24, 34}
if 4 in set:
    set.remove(4)  # Will only remove if 4 exists
