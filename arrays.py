# An array is a data structure that holds a collection of elements, each identified
# by its index or key.

# Here are the uses of arrays
'''
1. Storing data.
2. List of items.
3. Iteration and processing.
4. Sorting.
5. Searching.
6. Buffering.
7. Caching

'''
# Creating Arrays

ages = [12, 17, 24, 24, 43, 19, 89]
mixed_data_types = [4, "String", True, 12 + 12j]
print(ages)
print(mixed_data_types)


# Accessing Elements of an array

print(ages[0])
print(ages[1])
print(ages[2])
print(ages[3])
print(ages[4])


# Modifying Elements of an array

ages[3] = [1, 2, 3, 4, 5, 6, 7]  # Array nesting

print(ages[3])
print(ages)

# Adding Elements to an array

ages.append(100)
print(ages)

# Removing Elements from an array

ages.remove(100)
print(ages)

# Sorting an array

# ages.sort()
# print(ages)

# Searching an array
hesabu = ages.count(24)
print(ages.index(24))
print(hesabu)

'''

In Python, the count() method is used to count 
the number of occurrences of a specified element in
 a list (which can be considered as an array). Here's how the count() method works:
'''

numbers = [1, 2, 3, 2, 4, 2, 5, 2]
count_of_twos = numbers.count(2)
print(count_of_twos)  # Output: 4
