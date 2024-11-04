#bitwise-operators
#used to compare (binary) numbers

#bitwise operator - & - AND	Sets each bit to 1 if both bits are 1
print("bitwise operator - & - AND Sets each bit to 1 if both bits are 1")
m = 5				#00000101
n = 12				#00001100
print(m & n)		#00000100


print("\n---------------------------------------------------\n")

#bitwise operator - | - OR - Sets each bit to 1 if one of two bits is 1
print("bitwise operator - | - OR - Sets each bit to 1 if one of two bits is 1")
m = 5				#00000101
n = 12				#00001100
print(m | n)		#00001101

print("\n---------------------------------------------------\n")

#bitwise operator - ^ - XOR - Sets each bit to 1 if only one of two bits is 1
print("bitwise operator - ^ - XOR - Sets each bit to 1 if only one of two bits is 1")
m = 5				#00000101
n = 12				#00001100
print(m ^ n)		#00001001

print("\n---------------------------------------------------\n")

#bitwise operator - ~ - NOT - Inverts all the bits
print("bitwise operator - ~ - NOT - Inverts all the bits")
m = 5				#00000101
print(~m)			#11111010 (250 - 256)

print("\n---------------------------------------------------\n")

#bitwise operator - << - Zero fill left shift - Shift left by pushing zeros in from the right and let the leftmost bits fall off
print("bitwise operator - << - Zero fill left shift - Shift left by pushing zeros in from the right and let the leftmost bits fall off")
m = 12				#00001100
n = 5				#00000101
print(m << n)		#110000000 (256 + 128)

print("\n---------------------------------------------------\n")

#bitwise operator - >> - Signed right shift
#Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print("bitwise operator - >> - Signed right shift")
print("Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off")
m = 140				#10001100
n = 5				#00000101
print(m >> n)		#00000100
