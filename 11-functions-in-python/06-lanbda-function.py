# lambda function - have only single statement

# lambda function - with multiple parameters
print("lambda function - with multiple parameters")

product = lambda num1, num2, num3: num1 * num2 * num3 # product is the lambda function

print("\n---------------------------------------------------\n")

# calling of lambda function
print("calling of lambda function")
print("Product of values 3, 4, 5 is - : ", product(3, 4, 5))

print("\n---------------------------------------------------\n")

print("Product of values 10, 20, 30 is - : ", product(10, 20, 30))

print("\n---------------------------------------------------\n")

numbers_list = [14, 19, 31, 44]

# Use lambda function with map()
squared = list(map(lambda x: x ** 2, numbers_list))
print(squared)  # Output => [196, 361, 961, 1936]

# Use lambda function with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
print(even_numbers)  # Output => [14, 44]

print("\n---------------------------------------------------\n")

# Function Annotations
def add(a: int, b: int) -> int:
    return a + b

print(add("shbytes", "courses"))

print("\n---------------------------------------------------\n")

# Higher Order Functions
def apply_function(func, value):
    return func(value) # call the parameter function with argument

# call function with lambda function and value as arguments
print(apply_function(lambda x: x * 2, 10))  # Output => 20

print("\n---------------------------------------------------\n")

# This is a function
def shbytes():
    print("Python")

class Learning:
    # This is a method inside a class
    def shbytes(self):
        print("Python")

