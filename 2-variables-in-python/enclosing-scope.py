def outer():
    outer_counter = 1

    def inner():
        inner_counter = 2
        outer_counter = 3
        print("outer counter : ", outer_counter)
        print("inner counter : ", inner_counter)
    inner()
    print("outer counter in func_outer : ", outer_counter)
    # print("inner counter in func_outer : ", inner_counter)

outer()
