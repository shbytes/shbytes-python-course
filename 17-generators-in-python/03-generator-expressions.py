
number_list = [1, 5, 7, 9, 12]

# list comprehension - each term multiply by 2
square_number_list = [item*2 for item in range(5)]   # list comprehension using square brackets []
print(square_number_list)    # print list elements

# generator expression - surrounded by parenthesis ()
generator_object = (item*2 for item in range(5))     # generator expression using paranthesis ()

print(generator_object)         # print generator object
print(next(generator_object))   # next value from generator
print(next(generator_object))   # next value from generator
print(next(generator_object))   # next value from generator

print("\n---------------------------------------------------\n")
print("while loop - iterating over the generator iterator object")

list_generator_object = (item*2 for item in number_list)

while True:
    try:
        print(next(list_generator_object))
    except StopIteration:
        break

print("\n---------------------------------------------------\n")
print("for loop - iterating over the generator iterator object")

list_generator_object = (item*2 for item in number_list)

for item in list_generator_object:
    print(item)


print("\n---------------------------------------------------\n")
# List comprehension
squares = [x**2 for x in range(10)]

# Generator expression
gen_squares = (x**2 for x in range(10))

# Iterating through the generator expression
for square in gen_squares:
    print(square)


print("\n---------------------------------------------------\n")
# Generator Pipelines
def generate_integers():    # generator function for integers
    for i in range(1, 11):
        yield i             # yield integer values

def generate_squared_numbers(numbers):  # generator function for square numbers
    for number in numbers:
        yield number ** 2   # yield square values

def generate_even_numbers(numbers):     # generator function for even numbers
    for number in numbers:
        if number % 2 == 0:
            yield number    # yield even numbers

# Chaining 3 generators together
pipeline = generate_even_numbers(generate_squared_numbers(generate_integers()))

for value in pipeline:
    print(value, end=" ")  # Output => 4 16 36 64 100
