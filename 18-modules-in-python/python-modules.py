
# built-in modules example
import math      # math - Python's built-in module

# Using sqrt() function from math module
print(math.sqrt(36))  # Output => 6.0

# built-in modules example
import datetime  # datetime - Python's built-in module

# get the current date and time
now = datetime.datetime.now()
print(now)   # Output => 2022-10-08 18:17:27.748415

print("\n---------------------------------------------------\n")
# First, install the package using pip:
# pip install requests

import requests

response = requests.get('https://shbytes.com')
print(response.status_code)  # Output => 200

print("\n---------------------------------------------------\n")
# Python file name - website_info.py

def info(name):
    return f"courses@{name}"

# import module and use its function
# import website_info
#
# print(website_info.info('shbytes.com'))  # Output => courses@shbytes.com

print("\n---------------------------------------------------\n")
# Import the Entire Module
import datetime  # datetime - Python's built-in module

now = datetime.datetime.now()
print(now)   # Output => 2022-10-08 18:17:27.748415
current_date = datetime.date.today()

# Import Specific Functions or Classes
from math import sqrt, pi

print(sqrt(25))  # Output => 5.0
print(pi)        # Output => 3.141592653589793

# Import everything from module
from math import *

print(cos(0))   # Output => 1.0
print(sin(90))  # in radians. Output => 0.8939966636005579

print("\n---------------------------------------------------\n")

import math
print(dir(math))
# Output => ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

print("\n---------------------------------------------------\n")
import numpy as np

arr = np.array([12, 22, 35])
print(arr) # Output => [12 22 35]

print("\n---------------------------------------------------\n")
# Package folder structure
# package_1/
#     __init__.py
#     module_1.py
#     module_2.py

print("\n---------------------------------------------------\n")
# website_info.py
def info(name):
    return f"courses@{name}"

# when imported as module, this code will not execute
# when run directly, this code will execute
if __name__ == "__main__":
    info("shbytes.com")
