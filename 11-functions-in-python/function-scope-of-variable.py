g_variable = 100       # global variable

# local variable with same name as global variable
print("local variable with same name as global variable")
def l_scope_function():
    l_variable = 10    # local variable
    print(l_variable)
    g_variable = 90    # without global keyword will create local variable
    print(g_variable)  # print value of local variable

l_scope_function()

# access global variable with global keyword
print("access global variable with global keyword")
def g_scope_function():
    l_variable = 10    # local variable
    print(l_variable)
    global g_variable  # access global variable with global keyword
    print(g_variable)  # print value of global variable

g_scope_function()

