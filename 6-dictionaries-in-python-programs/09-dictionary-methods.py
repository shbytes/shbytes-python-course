# create dictionary with default values
# dict.fromkeys(keys, value)

# create dictionary with default values using fromkeys method
print("create dictionary with default values using fromkeys method")
keys = (1, 2, 3, 4)
default_value = "Python"
courses = dict.fromkeys(keys, default_value)
print(courses)
print(type(courses))

print("\n---------------------------------------------------\n")

# create dictionary with default values as None using fromkeys method
print("create dictionary with default values using fromkeys method")
keys = (1, 2, 3, 4)
courses = dict.fromkeys(keys)
print(courses)
print(type(courses))

# Creating a dictionary with characters from a string
char_dict = dict.fromkeys('shbytes', True)

print(char_dict)

print("\n---------------------------------------------------\n")

# dict.setdefault(keyname, value)
# set default values to a key in dictionary
print("set default values to a key in dictionary")
language_dict = {"name": "Python", "popular": "Yes"}
print(language_dict)
return_value = language_dict.setdefault("learn", "Yes")
print(language_dict)
print(return_value)

print("\n---------------------------------------------------\n")

# no impact of setdefault method if key is already present
print("no impact of setdefault method if key is already present")
language_dict = {"name": "Python", "popular": "Yes", "learn": "Yes"}
print(language_dict)
return_value = language_dict.setdefault("learn", "No")
print(language_dict)
print(return_value)

print("\n---------------------------------------------------\n")

# setdefault default value is None
print("setdefault default value is None")
car_dict = {"brand": "Honda", "popular": "Yes"}
print(car_dict)
return_value = car_dict.setdefault("color")
print(car_dict)
print(return_value)

# Safely retrieving or setting a default value using setdefault()
user_settings = {}
returned_theme = user_settings.setdefault('theme', 'light')
print(returned_theme)
print(user_settings)