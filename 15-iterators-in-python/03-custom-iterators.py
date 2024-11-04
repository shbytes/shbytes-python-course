class PowerElement:
    """Class to implement an iterator to calculate power of all numbers
    from 1 to given number"""

    def __init__(self, number, power):  # class __init__ function
        self.number = number
        self.power = power

    def __iter__(self):                 # __iter__ function to define iterator
        self.counter = 1
        return self

    def __next__(self):                 # __next__ function to get next element from iterator
        if self.counter <= self.number:
            result = self.counter ** self.power
            self.counter += 1
            return result
        else:
            raise StopIteration


# create a class object
power_element_object = PowerElement(4, 3)

# create an iterable from iterator class object
i = iter(power_element_object)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))  # raise StopIteration error