number = 3676743
number_list = []
index = 0
while number > 0:
    number_list.append(number % 10)
    number //= 10
    index += 1
number_list = list(reversed(number_list))
print(number_list)


number = 3676743
number_str = str(number)
number_list = [int(char) for char in number_str]
print(number_list)
