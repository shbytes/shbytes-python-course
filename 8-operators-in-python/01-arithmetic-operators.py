#arithmetic-operators
#used with numeric values
#perform common mathematical operations

#arithmetic operator - addition (+)
print("arithmetic operator - addition (+)")
m = 10
n = 20
print(m + n)
print(30 + 40)
print('m' + 'n')
print(['AWS'] + ['Python'])

print("\n---------------------------------------------------\n")

#arithmetic operator - Subtraction (-)
print("arithmetic operator - Subtraction (-)")
m = 10
n = 20
print(m - n)
print(30 - 40)
print({"Python", "NumPy"} - {"NumPy"})

print("\n---------------------------------------------------\n")

#arithmetic operator - Multiplication (*)
print("arithmetic operator - Multiplication (*)")
m = 10
n = 20
print(m * n)
print(30 * 40)
print('mn' * 3)
print(('AWS','Python') * 3)
print(['AWS','Python'] * 3)

print("\n---------------------------------------------------\n")

#arithmetic operator - Exponentiation (**)
print("arithmetic operator - Exponentiation (**)")
m = 2
n = 3
print("m ** n - ", m ** n)
print("n ** m - ", n ** m)

print("\n---------------------------------------------------\n")

#arithmetic operator - Division (/)
print("arithmetic operator - Division (/)")
m = 22
n = 8
print(m / n)
print(37 / 5)

print("\n---------------------------------------------------\n")

#arithmetic operator - Modulus (%) - gives remainder after division
print("arithmetic operator - Modulus (%) - gives remainder after division")
m = 22
n = 10
print(m % n)
print(37 % 5)

print("\n---------------------------------------------------\n")

#arithmetic operator - Floor division (//) - rounds the result down to the nearest whole number
print("arithmetic operator - Floor division (//) - rounds the result down to the nearest whole number")
m = 22
n = 8
print("m // n - ", m // n)
print(37 // 5)

print("\n---------------------------------------------------\n")

print(30 + 40)                       # Addition of two number
print('m' + 'n')                        # Addition of two characters
print(['AWS'] + ['Python'])    # Addition of two lists

print(30 - 40)                        # Subtraction of two numbers
print({"Python", "NumPy"} - {"NumPy"})   # Subtraction between two sets

print(30 * 40)                       # Multiplication of two numbers
print('mn' * 3)                       # Multiplication on string
print(('AWS','Python') * 3)   # Multiplication on Tuple
print(['AWS','Python'] * 3)    # Multiplication on List

print(37 / 5)                         # Division of two numbers

print(37 // 5)                        # Floor Division of two numbers

print(37 % 5)                        # Modulus of two numbers

print("2 ** 3 - ", 2 ** 3)        # Exponentiation of two numbers