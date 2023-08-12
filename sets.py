# Sets in python - Built in data structure used to store distinct values.
# It uses curl brace in declaration.
# It has  got the following features: '''
# 1. Uniqueness of its items
# 2. Does not follow order.
# 3. Mutable
# 4. Defined using Curl brace
# 5. Membership testing
# 6. Accepts varying data type items


# SET DECLARATION
set1 = [11, 22, 33, 44, 55, 'String value', True, False]
set2 = {22, 11, 30, 65, 90}
print(set1)
print(len(set1))

listType = type(set1)

# Converting other collections into set
setType = set(set1)

print(setType)


# Accessing set items

# print(setType[2])

# The error message "TypeError: 'set' object is not subscriptable" in Python indicates
# that you're trying to access elements of a set using subscript notation, which is not supported for sets.

if 33 in setType:
    print('It is true that 33 is in the given set')
else:
    print('Not true')

# But you can loop through the set items using a for loop,
# or ask if a specified value is present in a set, by using the in keyword.

print(11 in setType)


# Adding new items /// set.add(elmnt) //

setType.add(4j + 4)
# Clear method
# setType.clear()
# print(setType)

# Intersection and Union between two sets
inter = set2.intersection(setType)

# Subsets and Supersets
inter = set2.issubset(setType)

print(inter)
# Removing set items in the set
setType.remove(11)

print(setType)

# Difference between two sets

diff = setType.difference(set2)


print(diff)


# Joining two sets

setType.update(set2)

print(setType)


# intersection_update

# print(setType.intersection_update(set2))
