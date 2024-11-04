variable = "shbytes"
try:
    variable  # access the variable
    print("Variable is defined and has a value:", variable)
except NameError:
    print("Variable is not defined.")

def variable_func():
    print(locals())
    if 'variable' in locals():
        print("Variable is defined and has a value:", variable)
    else:
        print("Variable is not defined.")
variable_func()


print(globals())
if 'variable' in globals():
    print("Variable is defined and has a value:", variable)
else:
    print("Variable is not defined.")

if variable is None:
    print("Variable value is:", variable)
else:
    print("Variable is not None.")