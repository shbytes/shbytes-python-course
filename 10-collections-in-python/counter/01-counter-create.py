#Declaring Counter()
#class collections.Counter([iterable-or-mapping])
#dict subclass for counting hashable objects


print("create Counter object")
from collections import Counter                # import Counter from collection module

# Empty Counter object
empty_counter = Counter()
print(empty_counter)
print(type(empty_counter))

# Counter object from list
courses_counter = Counter(["Python","Python","Python","PowerBI"])
print(courses_counter)

# Counter object from string
shbytes_counter = Counter("shbytes")
print(shbytes_counter)

# Counter object from dictionary
mapping_counter = Counter({"c1":"PowerBI", "c2":"Python"})
print(mapping_counter)

# Counter object from keyword arguments
args_counter = Counter(courses=5, trainings=15)
print(args_counter)

# Counter object from iterable and keyword arguments
iter_keyword_counter = Counter({"c1":"AWS", "c2":"Python"}, courses=5, trainings=15)
print(iter_keyword_counter)

print("\n---------------------------------------------------\n")

#create empty Counter
print("create empty Counter")
from collections import Counter
empty_counter = Counter() 
print(empty_counter)
print(type(empty_counter))

print("\n---------------------------------------------------\n")

#create Counter from iterable
print("create Counter from iterable")
from collections import Counter
courses_counter = Counter(["Python","Python","Python","PowerBI"])
print(courses_counter)
print(type(courses_counter))

print("\n---------------------------------------------------\n")

#create Counter from iterable string
print("create Counter from iterable string")
from collections import Counter
shbytes_counter = Counter("shbytes")
print(shbytes_counter)
print(type(shbytes_counter))

print("\n---------------------------------------------------\n")

#create Counter from mapping
print("create Counter from mapping")
from collections import Counter
mapping_counter = Counter({"c1":"PowerBI", "c2":"Python"})
print(mapping_counter)
print(type(mapping_counter))

print("\n---------------------------------------------------\n")

#create Counter from keyword args
print("create Counter from keyword args")
from collections import Counter
args_counter = Counter(courses=5, trainings=15) 
print(args_counter)
print(type(args_counter))


mapping_counter = Counter({"c1":"AWS", "c2":"Python"}, courses=5, trainings=15)
print(mapping_counter)