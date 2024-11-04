
# array.array(data_type, value_list)
# array of signed char type
print("array of signed char type")
import array as array
signed_char_array = array.array("b", [10, -20, 30, -40])
print(signed_char_array)
print("signed char type", signed_char_array.typecode)

print("\n---------------------------------------------------\n")

# array.array(data_type, value_list)
# array of unsigned char type
print("array of unsigned char type")
import array as array
unsigned_char_array = array.array("B", [10, 20, 30, 60])
print(unsigned_char_array)
print("unsigned char type", unsigned_char_array.typecode)

print("\n---------------------------------------------------\n")

# array of signed short type
print("array of signed short type")
signed_short_array = array.array("h", [2330, -2230, 6730, -8740])
print(signed_short_array)
print("signed char type", signed_short_array.typecode)

print("\n---------------------------------------------------\n")

# array of unsigned short type
print("array of unsigned short type")
unsigned_short_array = array.array("H", [1670, 2980, 9860, 49660])
print(unsigned_short_array)
print("unsigned char type", unsigned_short_array.typecode)

print("\n---------------------------------------------------\n")

# array.array(data_type, value_list)
# array of Unicode type
print("array of Unicode type")
import array as array
unicode_array = array.array("u", ['o', 'm', 'p', 'r'])
print(unicode_array)
print("Unicode type", unicode_array.typecode)

print("\n---------------------------------------------------\n")

# array.array(data_type, value_list)
# array of signed long type
print("array of signed long type")
signed_long_array = array.array("l", [-341000, 452000, -8783000, 8774000])
print(signed_long_array)
print("signed long type", signed_long_array.typecode)

print("\n---------------------------------------------------\n")

# array.array(data_type, value_list)
# array of unsigned long type
print("array of unsigned long type")
unsigned_long_array = array.array("L", [22321000, 76542000, 878543000, 96544000])
print(unsigned_long_array)
print("unsigned long type", unsigned_long_array.typecode)

print("\n---------------------------------------------------\n")

# array of signed long type
print("array of signed long type")
signed_long_array = array.array("l", [-341000, 452000, -8783000, 8774000])
print(signed_long_array)
print("signed long type", signed_long_array.typecode)

print("\n---------------------------------------------------\n")

# array of unsigned long type
print("array of unsigned long type")
unsigned_long_array = array.array("L", [22321000, 76542000, 878543000, 96544000])
print(unsigned_long_array)
print("unsigned long type", unsigned_long_array.typecode)

empty_array = array.array('f')   # empty array, that can store float numbers
print(empty_array)

float_array = array.array('f', (5.1, 42.2, 37.38))   # typecode f, float numbers
print(float_array)