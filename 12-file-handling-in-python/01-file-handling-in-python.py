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
print("open a file with read and text mode. File should exist")
file_read_text = open('course_description.txt', 'r')

print("\n---------------------------------------------------\n")

# read mode - error when file does not exists
print("read mode - error when file does not exists")
try:
	file_read_text = open('course_details.txt', 'r')
except FileNotFoundError as err:
	print("error", err)

# open file in write and text mode
# if it does not exist, create an empty file with the given name
print("open file in write and text mode")
print("if it does not exist, create an empty file with the given name")
file_write_text = open('course_details.txt', 'w')

print("\n---------------------------------------------------\n")

# append and text mode, creates the file if it does not exist
print("append and text mode, creates the file if it does not exist")
file_append_text = open('course_details.txt', 'a')

print("\n---------------------------------------------------\n")

# create an empty file with the given name, returns an error if the file exists
print("create an empty file with the given name, returns an error if the file exists")
try:
	file_create_text = open('course_details.txt', 'x')
except FileExistsError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

# open a file with read and binary mode
print("open a file with read and binary mode. File should exist")
file_read_binary = open('course_description.txt', 'rb')

# open a file from differnt path, with read and binary mode
file_read_binary = open('D://shbytes/course_description.txt', 'rb')

print("\n---------------------------------------------------\n")

# open a file in write and binary mode
# if it does not exist, create an empty file with the given name
print("open a file in write and binary mode")
print("if it does not exist, create an empty file with the given name")
file_write_binary = open('course_description.txt', 'wb')

# append and binary mode, creates the file if it does not exist
print("append and binary mode, creates the file if it does not exist")
file_append_binary = open('course_details.txt', 'ab')

print("\n---------------------------------------------------\n")

# close all the open files
# always close the files; because of security & buffering issues, changes may not show until close of the file
print("close all the open files")
file_read_text.close()     # close file_read_text object
file_read_binary.close()   # close file_read_binary object
file_write_text.close()    # close file_write_text object
file_append_text.close()   # close file_append_text object

try:
	file_create_text.close()  # if object does not exist, give NameError
except NameError as err:
	print("error", err)