# An iterator is an object that contains a countable number of values.

# This object uses __iter__() and __next__() method s to iterate through the values.

# Iterator versus Iterable.

# Example 1:
myCollection = ("Yaya", "Kolo", "Toure")  # Colection

# myIterator = iter(myCollection)  # Iterator object

for myIterator in myCollection:
    print(myIterator)
