import os
import string

# 1st problem

path = input("Enter the path: ")

all_items = os.listdir(path)

only_dirs = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
only_files = [item for item in all_items if os.path.isfile(os.path.join(path,item))]
print("All items are: " , all_items)
print("Directories are: " , only_dirs)
print("Files are: " , only_files)

# 2nd problem

path = input("Enter the path: ")

if os.path.exists(path): # checks for existance
  if os.access(path, os.R_OK): # checks for readability
    print("This path is readable.")
  if os.access(path, os.W_OK): # checks for writability
    print("This path is writable.")
  if os.access(path, os.X_OK): # checks for executability
    print("This path is executable.")
else:
  print("This path does not exist.")

# 3rd problem

path = input("Enter the path: ")

if os.path.exists(path):
  filename = os.path.basename(path)
  directory = os.path.dirname(path)
  print("This is the filename: ", filename)
  print("This is the path: ", directory)
else:
  print("This path does not exist.")

# 4th problem

file = open("../names.txt", "r")

line_count = 0

for line in file:
  line_count += 1

file.close()

print("Number of lines: ", line_count)

# 5th problem

my_list = [2, 5, 3 , 6]

with open("myfile.txt", "w") as file:
  file.write(str(my_list))

with open("myfile.txt") as file:
  print(file.read())

# 6th problem

for letter in string.ascii_uppercase:
  with open(f"{letter}.txt", "w") as file:
    file.write(f"{letter}.txt\n")

# 7th problem

with open("../names.txt", "r") as file:
  content = file.read()

with open("../myfile.txt", "w") as myfile:
  myfile.write(content)

# 8th problem

path = input("Enter the path: ")
if os.path.exists(path):
  if os.access(path, os.W_OK):
    os.remove("../ab.txt")
    print("File deleted successfully.")
  else: 
    print("File is not writable - cannot be deleted.")
else: 
  print("This path does not exist.")