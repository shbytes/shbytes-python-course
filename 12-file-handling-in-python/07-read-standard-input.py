# read standard input
# two built-in functions to read a line of text from standard input
# input([prompt])
# eval(expression)

# input([prompt]) - reads one line from standard input, returns as a string, removing trailing newline
print("input([prompt]) - reads one line from standard input, returns as a string, removing trailing newline")
std_input = input("Provide input value: ") # Read standard input from console
print("Received input value: ", std_input)

print("\n---------------------------------------------------\n")

# eval(expression) - allows to evaluate arbitrary expressions from a string-based or compiled-code-based input
print("eval() - allows to evaluate arbitrary expressions from a string-based or compiled-code-based input")
std_input = input("Provide input value: ")		# [m*3 for m in range(5)]
print("Received input: ", eval(std_input))