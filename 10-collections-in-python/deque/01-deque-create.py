#Declaring deque()
#class collections.deque([iterable[, maxlen]])

from collections import deque                     # Import collections module

#create empty deque
print("create empty deque with no max length")
empty_deque = deque()                             # deque() constructor without iterable
print(empty_deque)                                # empty deque object
print(type(empty_deque))                          # type of deque object

#create deque with list and no max length
print("create deque with list and no max length")
list_deque = deque(['Power BI','Python','ML'])    # deque() constructor list iterable
print(list_deque)

#create deque with tuple and no max length
print("create deque with tuple and no max length")
tuple_deque = deque(('Power BI','Python','ML'))    # deque() constructor tuple iterable
print(tuple_deque)

#create deque with max length
print("create deque with max length")
maxlen_deque = deque(['Power BI','Python','ML'], 3)  # deque() constructor list and maxlen parameter
print(maxlen_deque)

print("\n---------------------------------------------------\n")

#create deque with list and no fixed length
print("create deque with list and no fixed length")
from collections import deque
courses_deque = deque(['AWS','Python','ML']) 
print(courses_deque)
print(type(courses_deque))

print("\n---------------------------------------------------\n")

#create deque with tuple and no fixed length
print("create deque with tuple and no fixed length")
from collections import deque
courses_deque = deque(('AWS','Python','ML')) 
print(courses_deque)
print(type(courses_deque))

print("\n---------------------------------------------------\n")

#create deque with fixed length
print("create deque with fixed length")
from collections import deque
courses_fixed_deque = deque(['AWS','Python','ML'], 2) 
print(courses_fixed_deque)
print(type(courses_fixed_deque))
