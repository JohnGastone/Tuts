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

ages = [12, 17, 24, 11, 24, 43, 24, 19, 24, 89]
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

'''
In Python, the `count()` method counts occurrences of a specific element in a list. If the elements are in order and repeated consecutively, the `count()` method will still work as expected and count those occurrences correctly. However, it's possible that some misunderstanding or mistake might be causing unexpected results. Let's take a look at an example:

```python
numbers = [1, 2, 2, 2, 3, 3, 4, 5]
count_of_twos = numbers.count(2)
count_of_threes = numbers.count(3)
print(count_of_twos)   # Output: 3
print(count_of_threes) # Output: 2
```

In this example, the `count()` method correctly counts the occurrences of the elements `2` and `3` in the list. If you're experiencing issues with the `count()` method not working as expected, it could be due to factors such as typos, incorrect data types, or misunderstanding the actual content of the list.

Make sure to double-check your code and ensure that the input data is as expected. If you're still facing difficulties, providing more details about your specific code and the issue you're encountering could help in diagnosing the problem more accurately.
'''

numbers = [1, 2, 3, 2, 4, 2, 5, 2]
index_of_twos = numbers.index(2)
