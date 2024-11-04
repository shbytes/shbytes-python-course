def local_function_scope_variable():
    shbytes_local = 0

    while(shbytes_local < 10):
        shbytes_local += 1
        if(shbytes_local %2 == 0) :
            print(f'{shbytes_local} is Even')
        else:
            print(f'{shbytes_local} is Odd')

local_function_scope_variable()