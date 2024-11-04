def func_outer():
    outer_counter = 1
    print("outer counter in func_outer : ", outer_counter)

    def func_inner():
        inner_counter = 2
        nonlocal outer_counter
        outer_counter = 3
        print("outer counter : ", outer_counter)
        print("inner counter : ", inner_counter)
    func_inner()
    print("outer counter in func_outer : ", outer_counter)


func_outer()