#class collections.Counter([iterable-or-mapping])
#dict subclass for counting hashable objects

#counter common patterns
print("counter common patterns")

from collections import Counter
char_counter = Counter("shbytes")
print(char_counter)

print(sum(char_counter.values()))
print(list(char_counter))
print(set(char_counter))
print(dict(char_counter))
print(char_counter.items())
print(Counter(dict(char_counter.items())))

print("\n---------------------------------------------------\n")

#sum(counter.values()) - total of all counts
print("sum(counter.values()) - total of all counts")
print(sum(char_counter.values()))

print("\n---------------------------------------------------\n")

#list(counter) - list unique elements
print("list(counter) - list unique elements")
char_list = list(char_counter)
print(char_list)

print("\n---------------------------------------------------\n")

#set(counter) - convert counter to a set
print("set(counter) - convert counter to a set")
char_set = set(char_counter)
print(char_set)

print("\n---------------------------------------------------\n")

#dict(counter) - convert counter to a regular dictionary
print("dict(counter) - convert counter to a regular dictionary")
char_dict = dict(char_counter)
print(char_dict)

print("\n---------------------------------------------------\n")

#counter.items() - convert counter to a list of (elem, cnt) pairs
print("counter.items() - convert counter to a list of (elem, cnt) pairs")
char_items_list = char_counter.items()
print(char_items_list)

print("\n---------------------------------------------------\n")

#Counter(dict(list)) - convert counter from a list of (elem, cnt) pairs
print("Counter(dict(list)) - convert counter from a list of (elem, cnt) pairs")
dict_counter = Counter(dict(char_items_list))
print(dict_counter)

print("\n---------------------------------------------------\n")

# +counter - remove zero and negative counts
print("+counter - remove zero and negative counts")
char1_counter = Counter(a=2,b=2,c=2)
char2_counter = Counter(c=2,d=1,e=1)
char1_counter.subtract(char2_counter)
print(char1_counter)
print(+char1_counter)

char1_counter.clear()
print(char1_counter)

print("\n---------------------------------------------------\n")

#clear() - reset all counts
print("clear() - reset all counts")
char1_counter = Counter(a=2,b=2,c=2)
print(char1_counter)
char1_counter.clear()
print(char1_counter)
