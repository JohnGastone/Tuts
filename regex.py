#

import re

# Pattern matching

text = "Hello, World!"
pattern = "John"
match = re.search(pattern, text)
if match:
    print("Pattern found: ", match.group())
else:
    print("Pattern not found: ")


# Metacharacters

text = "apple, appple, apPle, apPPle"
pattern = "ap*le"  # Matches "ale", "apple", "appple", etc.
matches = re.findall(pattern, text)
if matches:
    print("Metacharacter(s) found:" + str(matches))
else:
    print("Metacharacter(s) not found: ")


# Character Classes

text = "I have 3 apples and 2 bananas."
pattern = "[0-9]+"  # Matches one or more digits
match_ = re.findall(pattern, text)

if match_:
    print("Character(s) found:" + str(match_))
else:
    print("Character(s) not found: ")


# Anchors

text = "The cat is on the mat."
pattern = "^The"  # Matches "The" only at the start
matchy = re.search(pattern, text)

if matchy:
    print("Anchor(s) found:" + str(matchy))
else:
    print("Anchor(s) not found")


# Groups

text = "John Smith (Age: 30)"
pattern = r"(\w+) (\w+) \(Age: (\d+)\)"
matchyy = re.search(pattern, text)
name = matchyy.group(1, 2)  # Captures first and last name
age = matchyy.group(3)  # Captures age

if matchyy:
    print("Groups: " + str(matchyy.group))
else:
    print("Groups not found:")


# Quantifiers

# text = "aaaabbbbcccc"
# pattern = "a{2,3}"  # Matches "aaa" or "aa"
# matchey = re.findall(pattern, text)

# if matchey:
#     print("There are : " + str(matchey.group) + " matches")
# else:
#     print("There are no matches ")


# ALternation
text = "apple banana cherry"
pattern = "apple|banana"  # Matches "apple" or "banana"
matches = re.search(pattern, text)

if matches:
    print("There are : " + str(matches.group) + " matches")
else:
    print("There are no matches ")
