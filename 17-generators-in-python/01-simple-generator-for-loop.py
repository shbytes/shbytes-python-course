def simple_generator():
    n = 1
    print("value of n is", n)

    # Generator function contains yield statements
    yield n

    n += 1
    print("value of n is", n)
    yield n

    n += 1
    print("value of n is", n)
    yield n


gen_iter_object = simple_generator()
next(gen_iter_object)
next(gen_iter_object)
next(gen_iter_object)

for item in simple_generator():
    print(item)

print("\n---------------------------------------------------\n")
# Generator Function Example
def simple_function_generator():   # function to define generator
    yield "1- One"
    yield "2 - Two"
    yield "3 - Three"

gen_object = simple_function_generator() # object of generator

# Iterating through the generator
for value in gen_object:   # iterate over the generator values
    print(value)

# Output
# 1- One
# 2 - Two
# 3 - Three

print("\n---------------------------------------------------\n")
# Example of yield
def count_down_generator(n):  # function to define generator
    while n > 0:
        yield n
        n -= 1

for value in count_down_generator(5): # iterate over the generator values
    print(value)

print("\n---------------------------------------------------\n")
# Using for loop to create and iterate through  Generators
def generate_even_numbers(limit):     # function to define generator
    for num in range(2, limit+1, 2):  # iterate to get next even number
        yield num                     # yield number

for even in generate_even_numbers(20): # iterate over the generator values
    print(even, end=" ")
# Output => 2 4 6 8 10 12 14 16 18 20

print("\n---------------------------------------------------\n")
# Using Generators with next()
def generate_even_numbers(limit):     # function to define generator
    for num in range(2, limit+1, 2):  # iterate to get next even number
        yield num                     # yield number

gen_object = generate_even_numbers(20) # object - reference to the generator function

print(next(gen_object)) # Output => 2  # using next() - get next value from generator
print(next(gen_object)) # Output => 4  # using next() - get next value from generator
print(next(gen_object)) # Output => 6  # using next() - get next value from generator
# similarly we can get other value and can control the flow of values from generator

print("\n---------------------------------------------------\n")
# Example of an Infinite Generator

def generate_infinite_count(start=0):   # function to define generator
    while True:                         # loop always True
        yield start                     # yield number
        start += 1

gen_object = generate_infinite_count()  # object - reference to the generator function

# Printing the first 10 values of an infinite generator
for _ in range(10):
    print(next(gen_object), end=" ")  # Output => 0 1 2 3 4 5 6 7 8 9

print("\n---------------------------------------------------\n")
# Reading Large Files Line by Line
def read_large_file(file_name):   # function to read large file
    with open(file_name) as f:    # open file in read and text mode
        for line in f:
            yield line.strip()    # yield line from the file

for line in read_large_file("large_file.txt"):
    print(line)                   # print yielded line from the file
