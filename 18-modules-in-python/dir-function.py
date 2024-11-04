
import arithmetics.addition as aa
from arithmetics import multiplication as mul

print(aa.func_add(4, 7))
print(mul.func_multiply(4, 7))

print("\n---------------------------------------------------\n")

print(dir(aa))

print("\n---------------------------------------------------\n")

print(aa.__cached__)
print(aa.__doc__)
print(aa.__file__)
print(aa.__loader__)
print(aa.__name__)
print(aa.__package__)
print(aa.__spec__)

print("\n---------------------------------------------------\n")

import builtins
print(dir(builtins))
