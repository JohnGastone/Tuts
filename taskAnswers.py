# Question 1
for num in range(1, 11):
    print(num)

# Question 2
sum_even = 0
for num in range(2, 51, 2):
    sum_even += num
print(sum_even)


# Question 3
fibonacci = [0, 1]
for i in range(2, 10):
    next_num = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_num)
print(fibonacci)


# Question 4
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)


# Question 5
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)


# Question 6
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


# Question 7
word = input("Enter a word: ")
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
print(reversed_word)


# Question 8
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# Question 9
numbers = [int(x) for x in input("Enter a list of numbers: ").split()]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(average)


# Question 10
num = int(input("Enter a number for the multiplication table: "))
range_limit = int(input("Enter the range limit: "))
for i in range(1, range_limit + 1):
    print(f"{num} x {i} = {num * i}")
