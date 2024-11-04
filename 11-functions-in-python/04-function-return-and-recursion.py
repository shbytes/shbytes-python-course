# function => block of code to run when it is called
# function takes arguments, known as parameters to pass data
# function can return value as a result

print("parameter => variable listed inside the parentheses in function definition")
print("argument  => value sent to the function when it is called")

# Scenario 1 - function return value using return keyword
print("function return value using return keyword")
def multiple_numbers(number1, number2):  # function with 2 parameters
	return number1 * number2             # return multiple of two numbers

multiple = multiple_numbers(3, 5)
print("multiple", multiple)


# Scenario 2 - function return multiple values
print("function return multiple values")
def numbers_operation(number1, number2):          # function with 2 parameters
	return number1 + number2, number1 - number2   # return sum and subtract of two numbers

sum, subtract = numbers_operation(5, 3) # return multiple values and assigned to variables
print("sum", sum, "subtract", subtract)

print("\n---------------------------------------------------\n")

# function pass statement to void execution of any statement after that
print("function pass statement to void execution of any statement after that")
def multiple_numbers(number1, number2):
	pass

print("\n---------------------------------------------------\n")

# function recursion - calling of same function from its own function definition
print("function recursion - calling of same function from its own function definition")
def sum_sequence(number):
	if(number <= 0):
		return number
	else:
		return number + sum_sequence(number - 1)

print("function to calculate sum of sequence like 5 + 4 + 3 + 2 + 1")
print(sum_sequence(5))

print("function to calculate sum of sequence like 6 + 5 + 4 + 3 + 2 + 1")
print(sum_sequence(6))