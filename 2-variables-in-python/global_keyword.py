def func_local_variable():
    global shbytes_local          # declared locally but made global
    shbytes_local = "This is local variable with global scope!!"
    print(shbytes_local)

func_local_variable()

print(shbytes_local)
