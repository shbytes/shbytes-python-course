# Declaring DefaultDict()
# class collections.defaultdict([default_factory[, ...]])
# returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class.

from collections import defaultdict

# Scenario 1 - defaultdict with int as default_factory
int_defaultdict = defaultdict(int)     # defaultdict with int as default_factory
print(int_defaultdict['missing_key'])  # Output => 0
int_defaultdict['existing_key'] += 5   # operation on the dictionary element
print(int_defaultdict)  # Output => defaultdict(<class 'int'>, {'missing_key': 0, 'existing_key': 5})

# Scenario 2 - defaultdict with list as default_factory
list_defaultdict = defaultdict(list)   # defaultdict with list as default_factory
print(list_defaultdict['missing_key']) # Output => []
list_defaultdict['new_key'].append(12) # operation on the dictionary element
list_defaultdict['new_key'].append(22) # operation on the dictionary element
print(list_defaultdict)  # Output => defaultdict(<class 'list'>, {'missing_key': [], 'new_key': [12, 22]})


# create defaultdict with function definition
print("create defaultdict with function definition")
def def_course():
    return "no course"
      
course_default_dict = defaultdict(def_course, {'c1':'AWS','c2':'Python'}) # defaultdict with function and kwargs
print(course_default_dict)       # initial defaultdict object
print(course_default_dict["c1"]) # access key c1 from dictionary
print(course_default_dict["c2"]) # access key c2 from dictionary
print(course_default_dict["c3"]) # access key c3 from dictionary
print(course_default_dict)       # defaultdict after setting default value

print("\n---------------------------------------------------\n")

# create defaultdict with lambda
print("create defaultdict with lambda")
course_default_dict = defaultdict(lambda: "no course", {'c1':'AWS','c2':'Python'})
print(course_default_dict)       # initial defaultdict object
print(course_default_dict["c1"]) # access key c1 from dictionary
print(course_default_dict["c2"]) # access key c2 from dictionary
print(course_default_dict["c3"]) # access key c3 from dictionary
print(course_default_dict)       # defaultdict after setting default value

print("\n---------------------------------------------------\n")

# defaultdict changed with the default value for the key
print("defaultdict changed with the default value for the key")
course_default_dict = defaultdict(lambda: "no course", {'c1':'AWS','c2':'Python'})
print(course_default_dict)                   # initial defaultdict object
print(course_default_dict.__missing__('c1')) # This considers c1 as missing and reassign default value
print(course_default_dict.__missing__('c2')) # This considers c2 as missing and reassign default value
print(course_default_dict.__missing__('c3')) # c3 as missing and assign default value
print(course_default_dict)                   # defaultdict after assigning default value

# course_default_dict = defaultdict(None, {'c1':'AWS','c2':'Python'})
# print(type(course_default_dict))
# print(course_default_dict["c3"])

data = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('b', 5)]
d = defaultdict(list)
for k, v in data:
    d[k].append(v)
print(d)  # Output => defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2, 4, 5]})

course_list = ['Python', 'Power BI', 'Java', 'Python', 'Power BI', 'Power BI']
count_dict = defaultdict(int)
for course in course_list:
    count_dict[course] += 1
print(count_dict)  # Output => defaultdict(<class 'int'>, {'Python': 2, 'Power BI': 3, 'Java': 1})

from collections import defaultdict

d = defaultdict(int, {'a': 14, 'b': 42})
regular_dict = dict(d)
print(regular_dict)  # Output => {'a': 14, 'b': 42}
