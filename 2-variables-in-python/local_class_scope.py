class Shbytes:
    shbytes_local = 0
    print(shbytes_local)

    def func_scope_variable(number):
        while (number < 10):
            number += 1
            if (number % 2 == 0):
                print(f'{number} is Even')
            else:
                print(f'{number} is Odd')

Shbytes.func_scope_variable(Shbytes.shbytes_local)

