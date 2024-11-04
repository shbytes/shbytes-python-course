#identity-operators
#used to compare the objects for the same memory location
#not for equality of their value, but if they are same object, with the same memory location

#identity operator - is - Returns True if both variables are the same object
print("identity operator - is - Returns True if both variables are the same object")
m = 10
n = 20
k = m
print(k is n)
print(k is m)

print("\n---------------------------------------------------\n")

#identity operator - is not - Returns True if both variables are not the same object
print("identity operator - is not - Returns True if both variables are not the same object")
m = 10
n = 20
k = m
print(k is not n)
print(k is not m)


list_1 = [34, 56, 78]
list_2 = list_1
list_3 = [34, 56, 78]

print(list_1 is list_2)  # True, because list_2 refers to the same object as list_1
print(list_1 is list_3)  # False, because list_3 is a different object, even though it has the same content as list_1

print(list_1 is not list_2)  # False, because list_2 refers to the same object as list_1
print(list_1 is not list_3)  # True, because list_3 is a different object, even though it has the same content as list_1

