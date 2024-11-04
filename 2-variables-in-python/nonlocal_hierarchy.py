# def nonlocalscope():
#     nonlocal a
#     a = "changing to non-local!"
#     print(a)
#
# a = "global variable!"
# nonlocalscope()

def localscope():
    a = "local variable!"

    def nonlocalscope():
        nonlocal a
        a = "changing to non-local!"
        print(a)
    nonlocalscope()
    print(a)

localscope()