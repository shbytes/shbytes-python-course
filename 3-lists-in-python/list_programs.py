prefix = "prefix"
suffix = "suffix"
number_of_variables = 5
list_of_variables = []
for x in range(number_of_variables):
    list_of_variables.append(prefix+str(x)+suffix)
print(list_of_variables)

print("\n---------------------------------------------------\n")

import math
number = 16
sqrt_value = math.sqrt(number)
print(sqrt_value)

import cmath
sqrt_value = cmath.sqrt(number)
print(sqrt_value)

import numpy as np
sqrt_value = np.sqrt(number)
print(sqrt_value)

print("\n---------------------------------------------------\n")

def find_prime_number(number):
    if number <= 1 or number == 2:
        return True
    number_sqrt = int(number ** 0.5) + 1
    for i in range(number_sqrt):
        if i > 1 and number % i == 0:
            return False
    return True

number_1 = int(input('Enter start number: '))
number_2 = int(input('Enter end number: '))
prime_number_list = []
if number_2 < number_1:
    print("End number is less than start number")
else:
    for number_diff in range(number_2 - number_1):
        number = number_1 + number_diff
        if find_prime_number(number):
            prime_number_list.append(number)
print(prime_number_list)


number_list = [12,41,10,12,11,31,87,67,77,91]
prime_number_list = []
for number in number_list:
    if find_prime_number(number):
        prime_number_list.append(number)
print(prime_number_list)

print("\n---------------------------------------------------\n")

number_list = [12,41,10,12,11,31,87,67,77,91]
print(" ".join(map(str, number_list)))

number_list = [12,41,10,12,11,31,87,67,77,91]
for element in number_list:
    print(element, end=" ")


number_tuple = (12,41,10,12,11,31,87,67,77,91)
print(" ".join(map(str, number_tuple)))

number_tuple = (12,41,10,12,11,31,87,67,77,91)
for element in number_tuple:
    print(element, end=" ")

shbytes_string = "shbytes"
print(shbytes_string)
print("\n---------------------------------------------------\n")

