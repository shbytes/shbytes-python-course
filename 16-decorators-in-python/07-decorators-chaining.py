print("\n---------------------------------------------------\n")

# decorator chaining
print("decorator chaining")

def parent_func_1(func):
    def child_func_1(number):
        print("inside child_func_1 function")
        return 2 + func(number)
    return child_func_1

def parent_func_2(func):
    def child_func_2(number):
        print("inside child_func_2 function")
        return 2 * func(number)
    return child_func_2

# remainder_func = parent_func_1(remainder_func)
# remainder_func = parent_func_2(remainder_func)

@parent_func_1
@parent_func_2
def remainder_func(number):
    return number % 3


print("\n---------------------------------------------------\n")

print(remainder_func(8))

print("\n---------------------------------------------------\n")

print(remainder_func(7))