
# value = dictionary.pop(key, default_value)
# remove element using pop() method
print("remove element using pop() method")
cars_dict = {"c1": "Maruti", "c2": "Hyundai", "c3": "Honda", "c4": "Toyota"}
print(cars_dict)
car_name = cars_dict.pop("c3")
print(car_name)
print(cars_dict)

# remove element using pop() method with default value
print("remove element using pop() method with default value")
cars_dict = {"c1": "Maruti", "c2": "Hyundai", "c3": "Honda", "c4": "Toyota"}
print(cars_dict)
car_name = cars_dict.pop("c5", "Audi")
# car_name = cars_dict.pop("c6")
print(car_name)
print(cars_dict)

print("\n---------------------------------------------------\n")

# key, value = dictionary.popitem()
# remove last element using popitem() method
print("remove last element using popitem() method")
cars_dict = {"c1": "Maruti", "c2": "Hyundai", "c3": "Honda", "c4": "Toyota"}
print(cars_dict)
car_key, car_value = cars_dict.popitem()
car_item = cars_dict.popitem()
print(f"{car_key}, {car_value}")
print(car_item)
print(cars_dict)

# Error - popitem() error with empty dictionary
print("popitem() error with empty dictionary")
cars_dict = {}
print(cars_dict)
# car_item = cars_dict.popitem()

print("\n---------------------------------------------------\n")

# remove element using del keyword
print("remove element using del keyword")
cars_dict = {"c1": "Maruti", "c2": "Hyundai", "c3": "Honda", "c4": "Toyota"}
print(cars_dict)
del cars_dict["c2"]
print(cars_dict)

print("\n---------------------------------------------------\n")

# remove all element using clear() method
print("remove all element using clear() method")
cars_dict = {"c1": "Maruti", "c2": "Hyundai", "c3": "Honda", "c4": "Toyota"}
print(cars_dict)
cars_dict.clear()
print(cars_dict)

print("\n---------------------------------------------------\n")

# delete dictionary using del keyword
print("delete dictionary using del keyword")
cars_dict = {"c1": "Maruti", "c2": "Hyundai", "c3": "Honda", "c4": "Toyota"}
print(cars_dict)
del cars_dict
print(cars_dict["c1"])
