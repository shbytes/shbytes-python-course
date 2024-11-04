status = 400

match status:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")


value = tuple("shbytes")
match value:
    case int():
        print("value is of integer datatype.")
    case str():
        print("value is of string datatype.")
    case list():
        print("value is of list datatype.")
    case tuple():
        print("value is of tuple datatype.")
    case _:
        print("some other datatype.")


# match Statement with Patterns and Structure Evaluation
point = (12, 15)
print(type(point))
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"Point on x-axis at x={x}")
    case (0, y):
        print(f"Point on Y-axis at y={y}")
    case (x, y):
        print(f"Point at x={x}, y={y}")


# match Statement with Classes
from dataclasses import dataclass

@dataclass
class Coordinates:
    latitude: float
    longitude: float

coord = Coordinates(15.65, 45.56)
match coord:
    case Coordinates(0, 0):
        print("Origin")
    case Coordinates(latitude, 0):
        print(f"Coordinates at latitude={latitude} and longitude 0")
    case Coordinates(0, longitude):
        print(f"Coordinates at latitude 0 and longitude={longitude}")
    case Coordinates(latitude, longitude):
        print(f"Coordinates at latitude={latitude}, and longitude={longitude}")
    case _:
        print("Unknown coordinates")
