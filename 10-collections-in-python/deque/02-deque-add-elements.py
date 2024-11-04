#class collections.deque([iterable[, maxlen]])

from collections import deque

# add element to the right of deque using append method
print("add element to the right of deque using append method")
shbytes_right_deque = deque(['Power BI','Python'])
print(shbytes_right_deque)
shbytes_right_deque.append('ML')         # Add element to the right of deque using append method
print(shbytes_right_deque)

#add element to the left of deque using appendleft method
print("add element to the left of deque using appendleft method")
shbytes_left_deque = deque(['Power BI','Python'])
print(shbytes_left_deque)
shbytes_left_deque.appendleft('ML')      # Add element to the left of deque using appendleft method
print(shbytes_left_deque)

print("\n---------------------------------------------------\n")

#add element to the right of deque using append method
#append(x)
print("add element to the right of deque using append method")
from collections import deque
shbytes_right_deque = deque(['Power BI','Python'])
print(shbytes_right_deque)
shbytes_right_deque.append('ML')
print(shbytes_right_deque)
print(type(shbytes_right_deque))

print("\n---------------------------------------------------\n")

#add element to the left of deque using appendleft method
#appendleft(x)
print("add element to the left of deque using appendleft method")
from collections import deque
shbytes_left_deque = deque(['Power BI','Python'])
print(shbytes_left_deque)
shbytes_left_deque.appendleft('ML')
print(shbytes_left_deque)
print(type(shbytes_left_deque))

print("\n---------------------------------------------------\n")

# add element at an index position in deque using insert method
#insert(i, x)
print("add element at an index position in deque using insert method")
from collections import deque
shbytes_index_deque = deque(['Power BI','Python','ML'])
print(shbytes_index_deque)
shbytes_index_deque.insert(1, 'DevOps')  # Add element at index position
print(shbytes_index_deque)
print(type(shbytes_index_deque))

print("\n---------------------------------------------------\n")

from collections import deque

# add multiple elements to the right of deque using extend method
print("add multiple elements to the right of deque using extend method")
shbytes_extend_right_deque = deque(['Power BI','Python'])
print(shbytes_extend_right_deque)
shbytes_extend_right_deque.extend(['ML', 'DevOps'])    # Add multiple elements to the right of deque
print(shbytes_extend_right_deque)

# add multiple elements to the left of deque using extendleft method
print("add multiple elements to the left of deque using extendleft method")
shbytes_extend_left_deque = deque(['Power BI','Python'])
print(shbytes_extend_left_deque)
shbytes_extend_left_deque.extendleft(['ML', 'DevOps'])  # Add multiple elements to the left of deque
print(shbytes_extend_left_deque)

print("\n---------------------------------------------------\n")

#add multiple elements to the right of deque using extend method
#extend(iterable)
print("add multiple elements to the right of deque using extend method")
from collections import deque
shbytes_extend_right_deque = deque(['Power BI','Python'])
print(shbytes_extend_right_deque)
shbytes_extend_right_deque.extend(['ML', 'DevOps'])
print(shbytes_extend_right_deque)
print(type(shbytes_extend_right_deque))

print("\n---------------------------------------------------\n")

#add multiple elements to the left of deque using extendleft method
#extendleft(iterable)
#left appends results in reversing the order of elements in iterable argument
print("add multiple elements to the left of deque using extendleft method")
from collections import deque
shbytes_extend_left_deque = deque(['Power BI','Python'])
print(shbytes_extend_left_deque)
shbytes_extend_left_deque.extendleft(['ML', 'DevOps'])
print(shbytes_extend_left_deque)
print(type(shbytes_extend_left_deque))