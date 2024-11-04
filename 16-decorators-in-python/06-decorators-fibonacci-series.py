print("\n---------------------------------------------------\n")

# decorator calculation for fibonacci series
print("decorator calculation for fibonacci series")

def fibonacci_series(func):
    def child_func(number):
        print("inside child_func function")
        for m in range(number):
            fibonacci_list.append(func(m))
        print(fibonacci_list)

    return child_func


# fibonacci_number = fibonacci_series(fibonacci_number)
@fibonacci_series
def fibonacci_number(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fibonacci_list[number - 1] + fibonacci_list[number - 2]


print("\n---------------------------------------------------\n")

fibonacci_list = []
fibonacci_number(5)

print("\n---------------------------------------------------\n")

fibonacci_list = []
fibonacci_number(10)
