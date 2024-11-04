#class collections.deque([iterable[, maxlen]])

# reverse the elements of the deque in-place and then return None
print("reverse the elements of the deque in-place and then return None")
from collections import deque
courses_deque = deque(['AWS','Python','ML','DevOps','Azure']) 
print(courses_deque)                     # original order of elements
return_value = courses_deque.reverse()
print(courses_deque)                     # elements order is reversed in-place
print("returned value - ", return_value) # return None

print("\n---------------------------------------------------\n")

# for positive n, rotate the deque n steps to the right
# for positive n, rotate(n) one step equivalent to d.appendleft(d.pop())
print("for positive n, rotate the deque n steps to the right")
print("for positive n, rotate(n) one step equivalent to d.appendleft(d.pop())")
from collections import deque
courses_deque = deque(['AWS','Python','ML','DevOps','Azure'])
print(courses_deque)    # original order of elements
courses_deque.rotate(2) # 2 (positive) => elements from right moved left
print(courses_deque)    # Order of elements after 2 elements rotation

# for negative n, rotate the deque n steps to the left
# for negative n, rotate(n) one step equivalent to d.append(d.popleft())
print("for negative n, rotate the deque n steps to the left")
print("for negative n, rotate(n) one step equivalent to d.append(d.popleft())")
from collections import deque
courses_deque = deque(['AWS','Python','ML','DevOps','Azure'])
print(courses_deque)     # original order of elements
courses_deque.rotate(-2) # -2 (negative) => elements from left moved right
print(courses_deque)     # Order of elements after 2 elements rotation


print("\n---------------------------------------------------\n")

#for positive n, rotate the deque n steps to the right
#rotate(n)
#for positive n, rotate(n) one step equivalent to d.appendleft(d.pop())
print("for positive n, rotate the deque n steps to the right")
print("for positive n, rotate(n) one step equivalent to d.appendleft(d.pop())")
from collections import deque
courses_deque = deque(['AWS','Python','ML','DevOps','Azure'])
print(courses_deque)
courses_deque.rotate(2)
print(courses_deque)

print("\n---------------------------------------------------\n")

#for negative n, rotate the deque n steps to the left
#rotate(n)
#for negative n, rotate(n) one step equivalent to d.append(d.popleft())
print("for negative n, rotate the deque n steps to the left")
print("for negative n, rotate(n) one step equivalent to d.append(d.popleft())")
from collections import deque
courses_deque = deque(['AWS','Python','ML','DevOps','Azure'])
print(courses_deque)
courses_deque.rotate(-2)
print(courses_deque)

