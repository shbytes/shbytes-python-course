def docstring_function(x):
    """This a python program from Omprosoft
    to explain the Docstring in python.
    Here,it takes in a number x,
    returns the square of x"""
    return x**2


# access docstring using __doc__ method
print(docstring_function.__doc__)

print("\n---------------------------------------------------\n")

# access docstring using help() function
help(docstring_function)

