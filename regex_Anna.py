# Regular expression is a way of string matching and manipulation

# In python we work with regular expressions under the hood of "re" module

# Importing re module

import re

# Basic searching
text = "Hello Regular Expressions"  # String
pattern = "Regular"  # Pattern for searching / matching

match_text = re.search(pattern, text)  # re object

if match_text:
    print("Pattern found: ")

# Metacharacters (*, /, -)
# Metacharacters are characters with special meaning

# Backslash \

neno = "Hiki kitakua kilo 5034"
# Find all digit characters

digits = re.findall("\d", neno)

if digits:
    print(digits)
    print("Yes there exists some digits in the neno string")
else:
    print("No there exists no digit in the neno string")


# ^ - Start with

anza = re.findall("^Hii", neno)

if anza:
    print("Yes, the neno string starts with 'Hii'")
else:
    print("No, the neno string starts with some other word")

# $ - Ends with

maliza = re.findall("5034$", neno)

if maliza:
    print("Neno string ends with 5034")
else:
    print("Neno string ends with some other word")


'''
. + ? {} | () - Check how these characters are used in Regular expression

'''
