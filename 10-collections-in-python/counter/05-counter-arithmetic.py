#class collections.Counter([iterable-or-mapping])
#dict subclass for counting hashable objects

from collections import Counter
char1_counter = Counter(a=2,b=2,c=2)
char2_counter = Counter(c=1,d=1,e=1)

# add two counters together: counter1[x] + counter2[x]
print("add two counters together: counter1[x] + counter2[x]")
add_char_counter = char1_counter + char2_counter
print(add_char_counter)

# subtract (keeping only positive counts): counter1[x] - counter2[x]
print("subtract (keeping only positive counts): counter1[x] - counter2[x]")
subtract_char_counter = char1_counter - char2_counter
print(subtract_char_counter)

# intersection: min(c1[x], c2[x]) - counter1 & counter2
print("intersection: min(c1[x], c2[x]) - counter1 & counter2")
intersect_char_counter = char1_counter & char2_counter
print(intersect_char_counter)

# union: max(c1[x], c2[x]) - counter1 | counter2
print("union: max(c1[x], c2[x]) - counter1 | counter2")
union_char_counter = char1_counter | char2_counter
print(union_char_counter)

char1_counter.subtract(char2_counter)
print(char1_counter)
# unary addition for adding an empty counter
print("unary addition for adding an empty counter")
print(+char1_counter)

#unary subtraction for subtracting from an empty counter
print("unary subtraction for subtracting from an empty counter")
print(-char1_counter)

print("\n---------------------------------------------------\n")

#add two counters together: counter1[x] + counter2[x]
print("add two counters together:  counter1[x] + counter2[x]")
print(char1_counter)
print(char2_counter)
add_char_counter = char1_counter + char2_counter
print(add_char_counter)

print("\n---------------------------------------------------\n")

#subtract (keeping only positive counts): counter1[x] - counter2[x]
print("subtract (keeping only positive counts): counter1[x] - counter2[x]")
print(char1_counter)
print(char2_counter)
subtract_char_counter = char1_counter - char2_counter
print(subtract_char_counter)

print("\n---------------------------------------------------\n")

#intersection: min(c1[x], c2[x]) - counter1 & counter2
print("intersection: min(c1[x], c2[x]) - counter1 & counter2")
print(char1_counter)
print(char2_counter)
intersect_char_counter = char1_counter & char2_counter
print(intersect_char_counter)

print("\n---------------------------------------------------\n")

#union: max(c1[x], c2[x]) - counter1 | counter2
print("union: max(c1[x], c2[x]) - counter1 | counter2")
print(char1_counter)
print(char2_counter)
union_char_counter = char1_counter | char2_counter
print(union_char_counter)

print("\n---------------------------------------------------\n")

#unary addition for adding an empty counter
print("unary addition for adding an empty counter")
print(char1_counter)
print(char2_counter)
char1_counter.subtract(char2_counter)
print(char1_counter)
print(+char1_counter)

print("\n---------------------------------------------------\n")

#unary subtraction for subtracting from an empty counter
print("unary subtraction for subtracting from an empty counter")
char1_counter = Counter(a=2,b=2,c=2)
char2_counter = Counter(c=2,d=1,e=1)
print(char1_counter)
print(char2_counter)
char1_counter.subtract(char2_counter)
print(char1_counter)
print(-char1_counter)
