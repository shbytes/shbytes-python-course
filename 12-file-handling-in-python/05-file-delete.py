# File handling in Python
# open(filename, mode)
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "r+"- Open file for both reading and writing
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode

import os

file_write_text = open('course_details.txt', 'w')
file_write_text.close()

# remove/delete file
print("remove/delete file")
os.remove("course_details.txt")
print("course_details.txt file is removed")

try:
	file_read_text = open('course_details.txt', 'r')
except FileNotFoundError as err:
	print("error", err)

print("\n---------------------------------------------------\n")

# remove file if exists
print("remove file if exists")
if os.path.exists("course_details.txt"):
	os.remove("course_details.txt")
else:
	print("file 'course_details.txt' does not exist")

print("\n---------------------------------------------------\n")

# rename file if exists
file_write_text = open('course_details.txt', 'w')
file_write_text.close()
print("rename file if exists")
if os.path.exists("course_details.txt"):
	os.rename("course_details.txt", "new_course_details.txt")
else:
	print("file 'course_details.txt' does not exist")

print("\n---------------------------------------------------\n")

# create a directory
print("create a directory")
try:
	os.mkdir("file_handling_dir")
except FileExistsError as err:
	print("error", err)
print("folder file_handling_dir created!!")

print("\n---------------------------------------------------\n")

# delete a directory
print("delete a directory")
try:
	os.rmdir("file_handling_dir")
except FileNotFoundError as err:
	print("error", err)
print("folder file_handling_dir deleted!!")

print("\n---------------------------------------------------\n")

# get current working directory directory
print("get current working directory directory")
print(os.getcwd())

print("\n---------------------------------------------------\n")

try:
	os.chdir("new_dir")
except FileNotFoundError as err:
	print("error", err)
