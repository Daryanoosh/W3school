# 1st problem
import re

pattern = r"ab*"

test_string = input("Enter a string: ")
if re.search(pattern, test_string):
    print("Match found!")
else:
    print("No match.")

# 2nd problem

txt = input("Enter a string: ")
x = re.findall(r"ab{2,3}", txt)
if x:
    print("Match found!")
else:
    print("No match.")

# 3rd problem

txt = input("Enter a string: ")

x = re.findall(r"[a-z]+_[a-z]+", txt)

if x:
    print("Matches found:", txt)
else:
    print("No match.")

# 4th problem

txt = input("Enter a string: ")

x = re.findall(r"\b[A-Z][a-z]+", txt)

if x:
    print("Match found:", txt)
else:
    print("No match.")

# 5th problem

txt = input("Enter a string: ")
x = re.findall(r"a.*b$", txt)

if x:
    print("Match found: ", txt)
else:
    print("No match.")

# 6th problem

txt = input("Enter a string: ")
x = re.sub(r'[., ]', ':', txt)

print(x)

# 7th problem


def snake_to_camel(snake_str):

    return re.sub(r'_([a-zA-Z])', lambda x: x.group(1).upper(), snake_str)


snake = input("Enter a string: ")
camel = snake_to_camel(snake)
print(camel)

# 8th problem


# Take input from the user
txt = input("Enter a string: ")

# Use RegEx to split at uppercase letters
parts = re.split(r'(?=[A-Z])', txt)

# Remove any empty strings from the result
parts = [word for word in parts if word]

print("Split result:", parts)
