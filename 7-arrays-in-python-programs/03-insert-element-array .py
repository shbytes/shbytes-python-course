import array as array

# array of integer type - insert method - insert integer
print("array of integer type - insert method - insert integer")
integer_array = array.array("i", [10, 20, 30, 40])
print(integer_array)
integer_array.insert(3, 50)
print(integer_array)

print("\n---------------------------------------------------\n")

# TypeError - insert float with unsigned short type-code
print("TypeError - insert float with unsigned short type-code")
unsigned_short_array = array.array("H", [10, 20, 30, 40])
try:
    unsigned_short_array.insert(3, 50.55)
except TypeError as err:
    print("error", err)
    print(unsigned_short_array)

print("\n---------------------------------------------------\n")

# array of unsigned short type - insert method - insert unsigned short
print("array of unsigned short type - insert method - insert unsigned short")
unsigned_short_array = array.array("H", [1, 2, 3, 4])
print(unsigned_short_array)
unsigned_short_array.insert(3, 5)
print(unsigned_short_array)

print("\n---------------------------------------------------\n")

# array of unsigned short type - insert method - insert signed short
print("array of unsigned short type - insert method - insert signed short")
unsigned_short_array = array.array("H", [1, 2, 3, 4])
print(unsigned_short_array)
try:
    unsigned_short_array.insert(3, -5)
except OverflowError as err:
    print("error", err)
    print(unsigned_short_array)

# similarly we can insert elements in other typecode type array


# custom implementation - insert() method
print("custom implementation - insert() method")

import array as array


def custom_insert(array_object, index, element):
    if index < 0:
        index = len(array_object) + index

    new_array_object = array.array(array_object.typecode, [0] * (len(array_object) + 1))
    for x in range(len(new_array_object)):
        if x < index:
            new_array_object[x] = array_object[x]
        elif x == index:
            new_array_object[x] = element
        else:
            new_array_object[x] = array_object[x - 1]
    return new_array_object


signed_long_array = array.array("l", [135, 28976, 323674, 499834])
signed_long_array = custom_insert(signed_long_array, -3, 5055)
print(signed_long_array)
