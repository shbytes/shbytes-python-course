print("integer number representation")
number_int = 10
print(number_int)
print(type(number_int))

number_long = 999849389348943899988
print(number_long)
print(type(number_long))

print("\n---------------------------------------------------\n")

print("Octal decimal number representation")
number_octal1 = 0o12
# octal1 decimal equivalent = 1*8^1 + 1*8^0 = 9
print(number_octal1)
print(type(number_octal1))

number_octal2 = 0o7654321
# 7*8^6 + 6*8^5 + 5*8^4 + 4*8^3 + 3*8^2 + 2*8^1 + 1*8^0 = 2054353
print(number_octal2)
print(type(number_octal2))

print("\n---------------------------------------------------\n")

print("Hexadecimal number representation")
number_hexa1 = 0x12
# hexa1 decimal equivalent = 1*16^1 + 1*16^0 = 17
print(number_hexa1)
print(type(number_hexa1))

number_hexa2 = 0xfedcba987654321
# 16*16^15 + 15*16^14 + 14*16^13 + 13*16^12 + 12*16^11 + 11*16^10 +
# 10*16^9 + 9*16^8 + 8*16^7 + 7*16^6 + 6*16^5 + 5*16^4 +
# 4*16^3 + 3*16^2 + 2*16^1 + 1*16^0 = 1147797409030816545
print(number_hexa2)
print(type(number_hexa2))

print("\n---------------------------------------------------\n")

print("Float number representation - float type")
number_float = 10.53
print(number_float)
print(type(number_float))

print("\n---------------------------------------------------\n")

print("Complex number representation - complex type")
number_complex = 10 + 12j
print(number_complex)
print(type(number_complex))
print(number_complex.real)
print(number_complex.imag)
