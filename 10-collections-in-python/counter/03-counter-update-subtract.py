#class collections.Counter([iterable-or-mapping])
#dict subclass for counting hashable objects

# elements are counted from an iterable or added-in from another mapping (or counter)
# update([iterable-or-mapping])
print("elements are counted from an iterable")
from collections import Counter
courses_counter = Counter(["Python","Python","PowerBI"])
print(courses_counter)
courses_counter.update(["Python","PowerBI"])
print(courses_counter)
courses_counter.update({"Python":2,"PowerBI":3})
print(courses_counter)
courses_counter.update(Counter({"Python":2,"PowerBI":3}))
print(courses_counter)

print("\n---------------------------------------------------\n")

#elements are counted from an iterable or added-in from another mapping (or counter)
#update([iterable-or-mapping])
print("elements are counted added-in from another mapping (or counter)")
from collections import Counter
courses_counter = Counter({"c1":"AWS","c2":"Python"})
print(courses_counter)
courses_counter.update({"c1":"AWS","c2":"Python"})
print(courses_counter)

print("\n---------------------------------------------------\n")

# elements are subtracted from an iterable or from another mapping (or counter)
# subtract([iterable-or-mapping])
print("elements are subtracted from an iterable or from another mapping (or counter)")
from collections import Counter

# Create Counter Object
courses_counter = Counter(["Python","Python","PowerBI"])
print(courses_counter)

# Use subtract() method with list iterator
courses_counter.subtract(["Python","PowerBI"])
print(courses_counter)

# Use subtract() method with dictionary
courses_counter.subtract({"Python":2,"PowerBI":3})
print(courses_counter)

# Use subtract() method with another Counter object
courses_counter.subtract(Counter({"Python":2,"PowerBI":3}))
print(courses_counter)

print("\n---------------------------------------------------\n")
#elements are subtracted from an iterable or from another mapping (or counter)
#subtract([iterable-or-mapping])
print("elements are subtracted from an iterable")
from collections import Counter
char_counter = Counter("aabbccdd") 
print(char_counter)
char_counter.subtract("cdef")
print(char_counter)

print("\n---------------------------------------------------\n")

#elements are subtracted from an iterable or from another mapping (or counter)
#subtract([iterable-or-mapping])
print("elements are subtracted from another mapping (or counter)")
from collections import Counter
char1_counter = Counter(a=2,b=2,c=2)
char2_counter = Counter(c=1,d=1,e=1)
print(char1_counter)
print(char2_counter)
char1_counter.subtract(char2_counter)
print(char1_counter)