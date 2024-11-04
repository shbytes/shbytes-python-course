# File handling in Python
# open(filename, mode)
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "r+"- Open file for both reading and writing
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode

# open a file with read and text mode
print("open a file with read and text mode")
file_read_text = open('course_description.txt', 'r')

# Read first 9 characters from the file text
print(file_read_text.read(9))   # Output => Python is
# Read next 20 characters starting from seek position
print(file_read_text.read(20))  # Output => a powerful language

# Read next line of the file starting from seek position
print(file_read_text.readline()) # Output => for data manipulation and file handling
# Read next line of the file starting from seek position
print(file_read_text.readline()) # Output => It pairs seamlessly with Power BI, Microsoft's leading data visualization tool.

# Read complete content of the file starting from seek position
print(file_read_text.read())
# Output
# In this tutorial, we will learn how to read data from files using Python
# Clean or process it, and then connect the resulting data to Power BI for visualization.
# Useful when dealing with large datasets, log files that need processing before analysis.

for line in file_read_text:  # Read file content line by line in loop
	print(line)

# open a file with read and text mode
print("open a file with read and text mode")
file_read_text = open('course_description.txt', 'r')

print("\n---------------------------------------------------\n")

# Read open file by each line
print("Read open file by each line")
for line in file_read_text:  # Read file content line by line in loop
	print(line)
# read pointer shifts line by line

print("\n---------------------------------------------------\n")

# Read complete file in one go
print("Read complete file in one go")
file_read_text = open('course_description.txt', 'r')
print(file_read_text.read())   # Read complete content of the file

print("\n---------------------------------------------------\n")

# Read limited number of characters from start of file
print("Read limited number of characters from start of file")
file_read_text = open('course_description.txt', 'r')
print(file_read_text.read(9))   # Read first 9 characters from the file text
print(file_read_text.read(20))  # Read next 20 characters from the file text

print("\n---------------------------------------------------\n")

# Read file - first & second line with readline
print("Read file - first & second line with readline")
file_read_text = open('course_description.txt', 'r')
print(file_read_text.readline()) # Read first line of the file
print(file_read_text.readline()) # Read second line of the file

print("\n---------------------------------------------------\n")

# open a file with read and binary mode
# print("open a file with read and binary mode")
# file_read_binary = open('course_description.txt', 'rb')
#
# print("\n---------------------------------------------------\n")
#
# # Read binary open file by each line
# print("Read binary open file by each line")
# for each in file_read_binary:
# 	print (each)


# open a file with read and binary mode
print("open a file with read and binary mode")
file_read_binary = open('course_description.txt', 'rb')

# Read first 9 characters from the file text
print(file_read_binary.read(9))   # Output => b'Python is'
# Read next 20 characters starting from seek position
print(file_read_binary.read(20))  # Output => b' a powerful language'

# Read next line of the file starting from seek position
print(file_read_binary.readline()) # Output => b' for data manipulation and file handling\r\n'
# Read next line of the file starting from seek position
print(file_read_binary.readline()) # Output => b'It pairs seamlessly with Power BI, Microsoft\xe2\x80\x99s leading data visualization tool.\r\n'
# Read complete content of the file starting from seek position
print(file_read_binary.read())
# Output
# In this tutorial, we will learn how to read data from files using Python
# Clean or process it, and then connect the resulting data to Power BI for visualization.
# Useful when dealing with large datasets, log files that need processing before analysis.

for line in file_read_binary:  # Read file content line by line in loop
	print(line)

print("\n---------------------------------------------------\n")

# open file at different location - error when file does not exists
print("open file at different location - error when file does not exists")
try:
	file_read_text = open('D:\\course_details.txt', 'r')
except FileNotFoundError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

# close all the open files
# always close the files; because of security & buffering issues, changes may not show until close of the file
print("close all the open files")
file_read_text.close()
file_read_binary.close()
try:
	file_create_text.close()
except NameError as err:
	print("error", err)