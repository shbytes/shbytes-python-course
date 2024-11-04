
# Fibonacci series upto given position using function
print("Fibonacci series upto given position using function")
def fibonacci_series(count):
	series = []
	if count <= 0:
		print("Please provide a positive value number of counts")
	
	position = 0
	while(position < count):
		if position == 0 or position == 1:
			series.append(1)
		else:
			series.append(series[position-1] + series[position-2])
		position += 1
	return series

print("Fibonacci series till 5th position - ", fibonacci_series(5))
print("Fibonacci series till 10th position - ", fibonacci_series(10))

print("\n---------------------------------------------------\n")

# Fibonacci number at given position using function recursion
print("Fibonacci number at given position using function recursion")
def fibonacci_number(count):
	if count < 0:
		print("Incorrect input for count")
	elif count == 0:
		return 0
	elif count == 1 or count == 2:
		return 1
	else:
		return fibonacci_number(count-1) + fibonacci_number(count-2)

print("Fibonacci number at 5th position - ", fibonacci_number(5))
print("Fibonacci number at 10th position - ", fibonacci_number(10))

print("\n---------------------------------------------------\n")

# Factorial series upto given number using function
print("Factorial series upto given number using function")
def factorial_series(number):
	series = []
	if number <= 0:
		print("Please provide a positive value number of counts")
	
	position = 0
	while(position <= number):
		if position == 0 or position == 1:
			series.append(1)
		else:
			series.append(series[position-1] * position)
		position += 1
	return series

print("Factorial series till 5th position - ", factorial_series(5))
print("Factorial series till 10th position - ", factorial_series(10))

print("\n---------------------------------------------------\n")

# Factorial value for the given number using function recursion
print("Factorial value for the given number using function recursion")
def factorial_number(number, value = 1):
	if number < 0:
		print("Incorrect input for count")
	elif number == 0 or number == 1:
		return value
	else:
		value *= number
		return factorial_number(number-1, value)

print("Factorial number at 5th position - ", factorial_number(5))
print("Factorial number at 10th position - ", factorial_number(10))

print("\n---------------------------------------------------\n")

# validate number is Palindrome or not
print("validate number is Palindrome or not")
def palindrome_num_validation(number):
	num = number
	new_num = 0
	while(num > 0):
		remainder = num % 10
		new_num = new_num * 10 + remainder
		num = num // 10
	if new_num == number:
		return "Number is palindrome"
	else:
		return "Number is not palindrome"

print("5463773645 - ", palindrome_num_validation(5463773645))
print("123242321 - ", palindrome_num_validation(123242321))
print("923832892 - ", palindrome_num_validation(923832892))

print("\n---------------------------------------------------\n")

# validate string is Palindrome or not
print("validate string is Palindrome or not")
def palindrome_string_validation(value_str):
	isPalindrome = True
	length_str = len(value_str)
	for x in range(length_str):
		if value_str[x] == value_str[length_str - x - 1]:
			isPalindrome = True
		else:
			isPalindrome = False
	if isPalindrome:
		return "String is palindrome"
	else:
		return "String is not palindrome"

print("omproorpmo - ", palindrome_string_validation("omproorpmo"))
print("softfos - ", palindrome_string_validation("softfos"))
print("courses - ", palindrome_string_validation("courses"))

print("\n---------------------------------------------------\n")

# sorting of number list
print("sorting of number list")
def sort_num_list(num_list):
	num_list.sort()

num_list = [1, 19, 5, 16, 12, 15, 8, 4]
sort_num_list(num_list)
print("sorted list - ", num_list)

print("\n---------------------------------------------------\n")

# binary search in number sorted list with recursion function
print("binary search in number sorted list  with recursion function")
def binary_num_search(num_array, left, right, number):
	if right >= left:
		center = (left + right) // 2
		if num_array[center] == number:
			return center
		elif num_array[center] > number:
			return binary_num_search(num_array, left, center - 1, number)
		else:
			return binary_num_search(num_array, center + 1, right, number)
	else:
		return -1

num_array = [1, 2, 5, 8, 10, 14, 16, 17]
number = 5
num_index = binary_num_search(num_array, 0, len(num_array)-1, number)
if num_index == -1:
	print("Number is not present in array")
else:
	print("Number is present at index - ", str(num_index))
