# Variable is declared and initialized
s = "This is an object referenced by variable s"

print(s)        # Print the value of the variable

del s           # Delete the defined variable (Breaks the reference to the memory)

print(s)        # Gives error, since variable s is already deleted
