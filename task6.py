# Python File Open
# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# Open a File on the Server

# To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt", "r")

print(f.read())

# If the file is located in a different location, you will have to specify the file path, like this:
# f = open("D:\\myfiles\welcome.txt", "r")

print(f.read())

# Using the with statement

with open("demofile.txt", "r") as file:
  print(file.read())

# Close Files
# If you do not use the with statement, you must wrtie a close statement at the end of your codes.

file = open("demofile.txt")
print(file.readline())
f.close()

# Read Only Parts of the File

with open("demofile.txt") as f:
  print(f.read(5))

# Also you can read one line by using the readline() method:

with open("demofile.txt") as f:
  print(f.readline())

# If you call readline() two times, then there will be read two first lines.

with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

# You can also loop through the lines of the file:

with open("demofile.txt") as f:
  for line in f:
    print(line)

# Python File Write

# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

with open("demofile.txt") as f:
  print(f.read())

#Overwrite Existing Content
print('')
with open("demofile.txt", "w") as f:
  f.write("woops! I have deleted the content!")

with open("demofile.txt") as f:
  print(f.read())

# Create a New File

# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists

# #This will create a new file:
# f = open("myfile.txt", "x")

# #If the file already exist, an error will be raised.

# Python Delete File

# To delete a file, you must import the OS module, and run its os.remove() function:

import os
# os.remove("demofile.txt")

if os.path.exists("mytamana.txt"):
  os.remove("mytamana.txt")
else: 
  print("The file does not exist")

# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

os.rmdir("myfolder")

# Note: You can only remove empty folders.