# File handling in Python
# open(filename, mode)
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "r+"- Open file for both reading and writing
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode

file_read_text = open("course_details.txt", "r")

# file.fileno() - method to return the file descriptor of the stream, as a number
print("fileno of the file - ", file_read_text.fileno()) # Output => 3

# file.isatty() - method returns True if file stream is interactive
print("file stream is interactive - ", file_read_text.isatty()) # Output => False

# file.readable() - method returns True if the file is readable, else False
print("file is readable - ", file_read_text.readable()) # Output => True

# file.seekable() - method returns True if file is seekable, else False
print("file is seekable - ", file_read_text.seekable()) # Output => True

# file.seek(offset) - method sets current file position in a file stream and returns the new position
print("file seek offset - ", file_read_text.seek(4)) # # Output => 4

# file.tell() - method returns the current file position in file stream
print("file tell current position - ", file_read_text.tell()) # Output => 4

# file.writable() - method returns True if the file is writable, else False
print("file is writable - ", file_read_text.writable()) # Output => False

#  file.closed - True if file is closed, else False
print(file_read_text.closed) # Output => False

#  file.mode - access mode with which file was opened
print(file_read_text.mode) # Output => r

#  file.name - name of the file
print(file_read_text.name) # Output => course_details.txt

file_read_text.close()  # close file object




file_write_text = open('course_details.txt', 'w')

# file.flush() - method to clean the internal buffer
file_write_text.write("some random text")
file_write_text.flush()

# file.truncate(size) - method resizes the file to given number of bytes
print(file_write_text.truncate(5)) # Output => 5

# file.writable() - method returns True if the file is writable, else False
print("file is writable - ", file_write_text.writable()) # Output => True

# file.writelines(list) - method writes list of items to the file
file_write_text.writelines(["Python Learning @shbytes!!","\nNew line"])
file_write_text.close() # close file object


print("\n---------------------------------------------------\n")

file_write_text = open('course_details.txt', 'w')
file_write_text.close()

# file.fileno() - method to return the file descriptor of the stream, as a number
print("file.fileno() - method to return the file descriptor of the stream, as a number")

file_read_text = open("course_details.txt", "r")
print("fileno of the file - ", file_read_text.fileno())

print("\n---------------------------------------------------\n")

# file.flush() - method to clean the internal buffer
print("file.flush() - method to clean the internal buffer")
file_write_text = open('course_details.txt', 'w')
file_write_text.write("\nPython Learning @shbytes!!")
file_write_text.flush()
file_write_text.write("\nWriting text to the file in write mode")

file_read_text = open('course_details.txt', "r")
print(file_read_text.read())
file_read_text.close()

print("\n---------------------------------------------------\n")

# file.isatty() - method returns True if file stream is interactive
print("file.isatty() - method returns True if file stream is interactive")
file_read_text = open('course_details.txt', "r")
print("file stream is interactive - ", file_read_text.isatty())

print("\n---------------------------------------------------\n")

# file.readable() - method returns True if the file is readable, else False
print("file.readable() - method returns True if the file is readable, else False")

file_read_text = open('course_details.txt', "r")
print("file is readable - ", file_read_text.readable())

print("\n---------------------------------------------------\n")

# file.seek(offset) - method sets current file position in a file stream
print("file.seek(offset) - method sets current file position in a file stream")
print("file.seek(offset) - method also returns new postion")

file_read_text = open('course_details.txt', "r")
print(file_read_text.seek(4))

print("\n---------------------------------------------------\n")

# file.seekable() - method returns True if file is seekable, else False
print("file.seekable() - method returns True if file is seekable, else False")
print("file is seekable - ", file_read_text.seekable())

print("\n---------------------------------------------------\n")

# file.tell() - method returns the current file position in file stream
print("file.tell() - method returns the current file position in file stream")
print(file_read_text.readline())
print(file_read_text.tell())

print("\n---------------------------------------------------\n")

# file.truncate(size) - method resizes the file to given number of bytes
print("file.truncate(size) - method resizes the file to given number of bytes")
file_write_text = open('course_details.txt', 'w')
print(file_write_text.truncate(5))
file_read_text = open('course_details.txt', 'r')
print(file_read_text.readline())

print("\n---------------------------------------------------\n")

# file.writable() - method returns True if the file is writable, else False
print("file.writable() - method returns True if the file is writable, else False")
print("file is writable - ", file_read_text.writable())

print("\n---------------------------------------------------\n")

# file.writelines(list) - method writes list of items to the file
print("file.writelines(list) - method writes list of items to the file")
file_write_text = open('course_details.txt', 'w')
file_write_text.writelines(["Python Learning @shbytes!!","\nNew line"])
file_write_text.close()

file_read_text = open('course_details.txt', "r")
print(file_read_text.read())
file_read_text.close()

print("\n---------------------------------------------------\n")

# file object attributes
print("file object attributes")
file_read_text = open('course_details.txt', "r")

#  file.closed - True if file is closed, else False
print("file.closed - True if file is closed, else False")
print(file_read_text.closed)

#  file.mode - access mode with which file was opened
print("file.mode - access mode with which file was opened")
print(file_read_text.mode)

#  file.name - name of the file
print("file.name - name of the file")
print(file_read_text.name)
