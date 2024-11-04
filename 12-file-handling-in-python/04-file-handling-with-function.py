# File handling in Python
# open(filename, mode)
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "r+"- Open file for both reading and writing
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode

# with - to open and read file in one command
print("with - to open and read file in one command")
with open("course_description.txt") as file_read_text:   # open file in read mode
	file_data = file_read_text.read()                    # read entire content of the file
	print(file_data)
file_read_text.close()

print("\n---------------------------------------------------\n")

# with - to open and write file in one command
print("with - to open and write file in one command")
with open('course_details.txt', 'w') as file_write_text:  # open file in write mode
	file_write_text.write("\nWriting text to the file in write mode") # write content to the file
	file_write_text.write("\nPython Learning @shbytes!!")
file_write_text.close()

file_read_text = open('course_details.txt', "r")
print(file_read_text.read())
file_read_text.close()

print("\n---------------------------------------------------\n")

# split() function for splitting of line to get list of each word
print("split() function for splitting of line to get list of each word")
with open("course_details.txt", "r") as file_read_text:
	file_data = file_read_text.readlines()
	for line in file_data:
		word = line.split()
		print (word)
file_read_text.close()
