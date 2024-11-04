# collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

from collections import namedtuple

# _fields - strings listing the field names
print("_fields - strings listing the field names")
Coordinates = namedtuple('Coordinates',['lat','long']) 
c = Coordinates(-34.0667,46.8231)
print(c)          # namedtuple object
print(c._fields)  # Returns the field names as tuple

#_field_defaults - Dictionary mapping field names to default values
print("_field_defaults - Dictionary mapping field names to default values")
shbytes = namedtuple('shbytes', ['c1','c2','c3'], defaults=['Power BI','Python'])
print(shbytes._field_defaults) # Returns fields mapped to default values

print("\n---------------------------------------------------\n")

from collections import namedtuple

# convert dictionary to a namedtuple using double-star-operator
print("convert dictionary to a namedtuple using double-star-operator")
Courses = namedtuple('Courses', ['c1', 'c2'])
course_dict = {'c1':'Python', 'c2':'AWS'}
print(course_dict)
print(Courses(**course_dict))

print("\n---------------------------------------------------\n")

Point = namedtuple('Point', 'x y')
Rectangle = namedtuple('Rectangle', 'top_left bottom_right')

# Create instances of Point
p1 = Point(0, 0)
p2 = Point(10, 10)

# Create an instance of Rectangle using Point
rectangle = Rectangle(top_left=p1, bottom_right=p2)
print(rectangle)  # Output => Rectangle(top_left=Point(x=0, y=0), bottom_right=Point(x=10, y=10))
