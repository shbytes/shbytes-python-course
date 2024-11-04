"""docstring for file or module - This is the docstring module"""


class Shbytes:
    """docstring for class - this is the class Shbytes"""


def __init__(self, a):
    """docstring for __init__ - This is the initialize method"""
    self.a = a


def display_values(self):
    """docstring for display_values - this method is used to display the values"""
    print(self.a)


print("\n---------------------------------------------------\n")

# access docstring at module level
print(__doc__)

print("\n---------------------------------------------------\n")

# access docstring at class level
print(Shbytes.__doc__)


print("\n---------------------------------------------------\n")

# access docstring at method level
print(display_values.__doc__)


print("\n---------------------------------------------------\n")

# access docstring using class object
shbytes_class_object = Shbytes()
print(shbytes_class_object.__doc__)
