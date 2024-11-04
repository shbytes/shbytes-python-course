#class collections.deque([iterable[, maxlen]])

from collections import deque

# count the number of deque elements equal to given element
print("count the number of deque elements equal to given element")
shbytes_deque = deque(['AWS','Python','ML','DevOps','Python'])
print(shbytes_deque)   # Original elements
element_count = shbytes_deque.count('Python')     # Return count of 'Python'
print("Python element count - ", element_count)   # Output => 2

print("\n---------------------------------------------------\n")

# create a deep copy of the deque
print("create a deep copy of the deque")
from collections import deque
shbytes_deque = deque(['AWS','Python','ML','DevOps','Python']) 
print(shbytes_deque)    # Original object
copy_deque = shbytes_deque.copy() # Create deep copy of elements
print(copy_deque)       # Copied elements
copy_deque.append('Data Science') # Append elements in copied object
print(shbytes_deque)    # No change in original object
print(copy_deque)       # Elements in copied object after append

print("\n---------------------------------------------------\n")

from collections import deque

# maximum size of a deque or None if unbounded
print("maximum size of a deque or None if unbounded")
shbytes_deque = deque(['AWS','Python','ML','DevOps','Python']) # deque without maxlen
print(shbytes_deque)  # Original object
deque_maxlen = shbytes_deque.maxlen # maxlen will return None
print(deque_maxlen)   # Output => None

#maximum size of a deque or None if unbounded
#maxlen
print("maximum size of a deque or None if unbounded")
from collections import deque
shbytes_deque = deque(['AWS','Python','ML'], 5) # deque with maxlen=5
print(shbytes_deque)   # Original object
deque_maxlen = shbytes_deque.maxlen  # maxlen will return 5
print(deque_maxlen)    # Output => 5