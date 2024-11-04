from collections import deque

# deque indexing
print("deque indexing")
shbytes_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])

print(shbytes_deque[0])   # Output => 'Power BI'
print(shbytes_deque[-1])  # Output => 'ML' (from the right)
print(shbytes_deque[2])   # Output => 'Python'

# deque slicing
print("deque slicing")
deque_list = list(shbytes_deque)[1:3]
print(deque_list)  # Output => ['ML', 'Python']

print("\n---------------------------------------------------\n")

from collections import deque

# returns first match index for element from left
print("returns first match index for element from left")
shbytes_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(shbytes_deque)
element_index = shbytes_deque.index('ML')
print("index of ML - ", element_index)

# return first match index from left at or after start
print("return first match index from left at or after start")
shbytes_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(shbytes_deque)
element_index = shbytes_deque.index('ML', 2)
print("index of ML start from index 2 - ", element_index)

# return first match index from left at or after start and before stop
print("return first match index from left at or after start and before stop")
shbytes_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(shbytes_deque)
element_index = shbytes_deque.index('ML', 1, 3)
print("index of ML start from 2 and stop at 3 - ", element_index)

# ValueError when element not found in deque between start and stop index
print("ValueError when element not found in deque between start and stop index")
shbytes_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(shbytes_deque)
try:
	element_index = shbytes_deque.index('AWS', 1, 3)
except ValueError as err:
	print("ValueError", err)       # ValueError 'AWS' is not in deque


print("\n---------------------------------------------------\n")

#class collections.deque([iterable[, maxlen]])
#index(x[, start[, stop]])

#return index of element in deque with no start index given
#index(x)
#returns the first match element index from left
print("return index of element in deque with no start index given")
from collections import deque
shbytes_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(shbytes_deque)
element_index = shbytes_deque.index('ML')
print("index of ML - ", element_index)

print("\n---------------------------------------------------\n")

#return index of element in deque at or after index start
#index(x, start)
#returns the first match element index from left
print("return index of element in deque at or after index start")
from collections import deque
shbytes_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(shbytes_deque)
element_index = shbytes_deque.index('ML', 1)
print("index of ML - ", element_index)

print("\n---------------------------------------------------\n")

#return index of element in deque at or after index start and before index stop
#index(x, start, stop)
#returns the first match element index from left
print("return index of element in deque at or after index start and before index stop")
from collections import deque
shbytes_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(shbytes_deque)
element_index = shbytes_deque.index('ML', 1, 3)
print("index of ML - ", element_index)

print("\n---------------------------------------------------\n")

#return ValueError when element not found in deque between start and stop index
#index(x, start, stop)
print("return ValueError when element not found in deque between start and stop index")
from collections import deque
shbytes_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(shbytes_deque)
try:
	element_index = shbytes_deque.index('AWS', 1, 3)
except ValueError as err:
	print("error", err)
