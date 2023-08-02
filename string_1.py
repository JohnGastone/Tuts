# This is the file for implementing String properties and its operations

# Declaring String Variables
session = 'Zoom session'
print('This day is wonderful')


# Declaring multiline String

multiLineString = '''
This is the way of declaring a multiline string
'''

# Treating a string as an Array

stringAsArray = 'Bromochlorodifluoromethane'

# Foward indexing
print(stringAsArray[21])

# Reverse indexing
print(stringAsArray[-26])


# String Slicing
print(stringAsArray[:6])

# String Modification (lower(), upper(), strip(), replace())
print(stringAsArray.strip())
# stringAsArray[]
print(stringAsArray.replace('o', 'J', 3))

# String concatenation

fName = 'John '
lName = 'Mshua \n Masta'

fullName = fName + lName


print(fullName)
