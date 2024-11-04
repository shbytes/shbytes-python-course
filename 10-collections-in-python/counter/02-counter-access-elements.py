#class collections.Counter([iterable-or-mapping])
#dict subclass for counting hashable objects

#access Counter element by key
print("access Counter element by key")
from collections import Counter
courses_counter = Counter(["AWS","Python","AWS","Data Science"])
print(courses_counter)
print(courses_counter["AWS"])
print(courses_counter["ML"])

print("\n---------------------------------------------------\n")

# iterator over Counter object elements repeating each as many times as its count
# elements() methods
print("iterator over Counter object elements repeating each as many times as its count")
from collections import Counter
shbytes_counter = Counter("shbytes")
print(shbytes_counter)
for element in shbytes_counter.elements():
	print(element)

print("\n---------------------------------------------------\n")

# return list of n most common elements and their counts
# most_common([n]
print("return list of n most common elements and their counts")
from collections import Counter
most_common_counter = Counter("shbytes")
print(most_common_counter)
print(most_common_counter.most_common(2))
print(most_common_counter.most_common()[:-4:-1])
print(most_common_counter.most_common())

print("\n---------------------------------------------------\n")

#return list of n least common elements and their counts
#most_common([n]
print("return list of n least common elements and their counts")
from collections import Counter
least_common_counter = Counter("shbytes")
print(least_common_counter)
print(least_common_counter.most_common()[:-4:-1])

print("\n---------------------------------------------------\n")

#most_common([n] - return all elements and their counts
print("return list of n most common elements and their counts from most common to the least")
from collections import Counter
all_elements_counter = Counter("omprosoft") 
print(all_elements_counter)
print(all_elements_counter.most_common())
