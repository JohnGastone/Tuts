# List is a python built in data type for storing multiple items in one variable

# Creating a list
myFavCodLanguages = ['C#', 'Python', 'Php', 'Java', 'Dart']
mixedDataTypeList = [23, 'Ugali', 43.9, 9 + 4j, {'Wali', 'Pilau', 'Biriani'}]
print(len(myFavCodLanguages))
print(myFavCodLanguages)
# Features of Lists
# 1. Dynamic in size
# 2. Heterogeneous in nature
# 3. Accept Indexing
# 4. Accept Slicing
# 5. Accept Iteration
# 6. Accept Concatenation


# Accessing list items - List items can be traversed using their respective indices

# Index number 1 is inclusive while index number 4 is exclusive
print(myFavCodLanguages[1:4])
print(mixedDataTypeList[-5:-2])

if 'Pilau' in mixedDataTypeList[4]:
    print("Pilau is in the sub list")


# Changing List Items

myFavCodLanguages[2:3] = ['JavaScript', 'Golang']
print(myFavCodLanguages)


regionsList = []
regionsList.append('Mtwara')
regionsList[0] = 'Simiyu'
regionsList.append(['Mtwara', 'Dodoma', 'Morogoro', 'Dsm'])
regionsList[2:4] = ['Geita', 'Singida', 'Kigoma']
regionsList.insert(1, 'Morogoro')
regionsList.extend(myFavCodLanguages)
print(regionsList)

# Remove List items

# regionsList.remove('Morogoro')
# Using Pop()
# regionsList.clear()
# del regionsList
regionsList.reverse()
print(regionsList)

numberList = [1, 4, 54, 74, 12, 90]
numberList.sort()
print(numberList)


# List methods - These are operations on python lists
# append()	- Adds an element at the end of the list
# clear()	- Removes all the elements from the list
# copy()	- Returns a copy of the list
# count()	- Returns the number of elements with the specified value
# extend()	- Add the elements of a list (or any iterable), to the end of the current list
# index()	- Returns the index of the first element with the specified value
# insert()	- Adds an element at the specified position
# pop()	- Removes the element at the specified position
# remove()	- Removes the item with the specified value
# reverse()	- Reverses the order of the list
# sort()	- Sorts the list
