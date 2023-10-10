import re

# Metacharacters

txt = "The rain in Spain"

# Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 59 dollars"

# Find all digit characters:

x = re.findall("\d", txt)
print(x)

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

txt = "hello planet"

# Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

txt = "hello planet"

# Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")


# Sets
txt = "The rain in Spain"

# Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


txt = "The rain in Spain"

# Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


txt = "The rain in Spain"

# Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
