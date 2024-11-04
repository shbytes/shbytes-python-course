#class collections.deque([iterable[, maxlen]])

# remove first occurrence of element from the deque
print("remove first occurrence of element from the deque")
from collections import deque
courses_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(courses_deque)      # Original elements in deque
courses_deque.remove('ML')
print(courses_deque)      # Elements in deque after removing 'ML'

# remove an element from the deque, ValueError if not found
print("remove an element from the deque, ValueError if not found")
courses_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(courses_deque)      # Original elements in deque
try:
	courses_deque.remove('DevOps')    # Devops does not exists in deque, throws ValueError
except ValueError as err:
	print("error", err)
	print(courses_deque)

print("\n---------------------------------------------------\n")



#remove first occurrence of element in the deque
#remove(x)
print("remove first occurrence of element in the deque")
from collections import deque
courses_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(courses_deque)
courses_deque.remove('ML')
print(courses_deque)

print("\n---------------------------------------------------\n")

#remove an element in the deque, ValueError if not found
#remove(x)
print("remove an element in the deque, ValueError if not found")
from collections import deque
courses_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(courses_deque)
try:
	courses_deque.remove('DevOps')
except ValueError as err:
	print("ValueError", err)
	print(courses_deque)

print("\n---------------------------------------------------\n")

# remove and return the element from right of the deque
print("remove and return the element from right of the deque")
from collections import deque
courses_pop_right_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(courses_pop_right_deque)
popped_right_element = courses_pop_right_deque.pop()     # pop element from right
print(courses_pop_right_deque)
print(popped_right_element)

# remove and return the element from left of the deque
print("remove and return the element from left of the deque")
courses_pop_left_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(courses_pop_left_deque)
popped_left_element = courses_pop_left_deque.popleft()  # pop element from left
print(courses_pop_left_deque)
print(popped_left_element)

# pop & popleft method throw index error if no elements are present in deque
print("pop & popleft method throw index error if no elements are present in deque")
empty_deque = deque()
print(empty_deque)
try:
	pop_element = empty_deque.pop()                    # pop or popleft, raise IndexError
except IndexError as err:
	print("IndexError", err)

print("\n---------------------------------------------------\n")

#remove and return the element from right of the deque
#pop()
print("remove and return the element from right of the deque")
from collections import deque
courses_pop_right_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(courses_pop_right_deque)
pop_element = courses_pop_right_deque.pop()
print(courses_pop_right_deque)
print(pop_element)

print("\n---------------------------------------------------\n")

#remove and return the element from left of the deque
#popleft()
print("remove and return the element from left of the deque")
from collections import deque
courses_pop_left_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(courses_pop_left_deque)
pop_element = courses_pop_left_deque.popleft()
print(courses_pop_left_deque)
print(pop_element)

print("\n---------------------------------------------------\n")

#pop & popleft method throw index error if no elements are present in deque
#pop()
print("pop & popleft method throw index error if no elements are present in deque")
from collections import deque
empty_deque = deque() 
print(empty_deque)
try:
	pop_element = empty_deque.pop()
except IndexError as err:
	print("error", err)

	print("\n---------------------------------------------------\n")

# remove all elements from the deque leaving it with no length
#clear()
print("remove all elements from the deque leaving it with no length")
from collections import deque
courses_deque = deque(['Power BI', 'ML', 'Python', "AI", "LLM", "ML"])
print(courses_deque)
courses_deque.clear()   # Removes all elements from the deque
print(courses_deque)
