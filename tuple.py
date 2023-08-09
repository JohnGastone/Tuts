# This file describe the properties of python tuples

# Python tuples are collection-type data structure which stores data/items immutably

# Creating a tuple

myOnlyTuple = ('item 1', 'item 2', 'item 2', 'item 4')
myLastBornTuple = (('item 1', 'item 2', 'item 2', 'item 4'),
                   23, 54.78, 'item last born')

# myOnlyList = list(myOnlyTuple)

# myOnlyList.remove('item 2')

# myOnlyTuple = tuple(myOnlyList)
# print(myOnlyTuple)
print(myLastBornTuple)
print(myOnlyTuple)


# Unpacking a tuple
(first, second, third, fouth) = myOnlyTuple
print(myOnlyTuple)
print(second)
