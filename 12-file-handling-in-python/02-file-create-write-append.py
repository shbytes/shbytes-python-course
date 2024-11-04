# File handling in Python
# open(filename, mode)
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "r+"- Open file for both reading and writing
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode

# create an empty file with the given name, returns an error if the file exists
print("create an empty file with the given name, returns an error if the file exists")
try:
	file_create_text = open('course_details.txt', 'x')
except FileExistsError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

# open file in write and text mode
# if it does not exist, create an empty file with the given name
print("open file in write and text mode")
print("if it does not exist, create an empty file with the given name")
file_write_text = open('course_details.txt', 'w')
file_write_text.write("Writing text to the file in write mode") # writing first line to the file
file_write_text.write("\nPython Learning @shbytes!!") # writing second line to the file
file_write_text.close() # close the file write object

file_read_text = open('course_details.txt', "r")
print(file_read_text.read()) # read the entire content of the file
file_read_text.close()  # close the file read object

print("\n---------------------------------------------------\n")

# open file in write and binary mode
# if it does not exist, create an empty file with the given name
print("open file in write and binary mode")
print("if it does not exist, create an empty file with the given name")
file_write_binary = open('course_details.txt', 'wb')
file_write_binary.write(bytearray("\nWriting text to the file in write mode".encode()))
file_write_binary.write(bytearray("\nPython Learning @shbytes!!".encode()))
file_write_binary.close()

file_read_text = open('course_details.txt', "r")
print(file_read_text.read())
file_read_text.close()

print("\n---------------------------------------------------\n")

# open file in append and text mode
# if it does not exist, create an empty file with the given name
print("open file in append and text mode")
print("if it does not exist, create an empty file with the given name")
file_append_text = open('course_details.txt', 'a') # open the file in append mode
file_append_text.write("Writing text to the file in append mode") # add a line to the file
file_append_text.write("\nPython is easy to learn!!") # add another line to the file
file_append_text.close() # close the file append object

file_read_text = open('course_details.txt', "r") # open the file read mode
print(file_read_text.read()) # read entire content of the file
file_read_text.close()  # close the file read object

print("\n---------------------------------------------------\n")

# close all the open files
# always close the files; because of security & buffering issues, changes may not show until close of the file
print("close all the open files")
file_read_text.close()
try:
	file_create_text.close()
except NameError as err:
	print("error", err)