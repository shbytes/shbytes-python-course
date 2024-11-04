import arithmetic_module        # module not added multiple times
import arithmetic_module as am  # import module with alias
import arithmetic_module

print(arithmetic_module.func_add(3, 4))  # call module function using module name

print(am.func_multiply(3, 4))  # call module function using alias

print(am.func_divide(6, 3))    # call module function using alias
