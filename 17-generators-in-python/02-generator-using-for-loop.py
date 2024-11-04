def func_string_character(input_string):
    for index in range(len(input_string)):
        yield input_string[index]


for character in func_string_character("omprosoft"):
    print(character)