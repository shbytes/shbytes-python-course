x = 5
def fun_scope():
    x = 10
    print(x, end = " ")

fun_scope()
print(x)