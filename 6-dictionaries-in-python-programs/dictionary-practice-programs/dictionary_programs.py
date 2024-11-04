prefix = "prefix"
suffix = "suffix"
number_of_variables = 5
dict_of_variables = {}
for x in range(number_of_variables):
    dict_of_variables[prefix+str(x)+suffix] = x
print(dict_of_variables)
print(dict_of_variables.keys())

prefix = "prefix"
suffix = "suffix"
number_of_variables = 5
dict_of_variables = {}
for x in range(number_of_variables):
    dict_of_variables[x] = prefix+str(x)+suffix
print(dict_of_variables)
print(dict_of_variables.values())