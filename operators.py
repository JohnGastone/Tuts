# This file is for the operator computations
# Python operators are used to perfom operations on variables or values

# Types of Python Operators
# 1. Arithmetic Operators
# 2. Logical Operators
# 3. Assignment Operators
# 4. Comparison Operators
# 5. Identity Operators
# 6. Membership Operators
# 7. Bitwise Operators


# Arithmetic Operators
# Addition (+)
x = 4
y = 6

z = x + y
print(z)
# Subtraction (-)

a = y - x
print(a)
# Multiplication (*)

j = x * y
print(j)
# Division (/)

k = x / y
print(k)

# Exponentiation (**)

r = x**2
f = x**3

# Modulus (%)
i = y % x
print(i)


# Comparison Operators
# Greater than (>)
print(x > y)

# Less than (<)
print(x < y)

# Equal (==)
print(x == y)

# Not equal (!=)
print(x != y)


# Greater than or equal (>=)
print(x >= y)

# Less than or equal ( <=)
print(x <= y)


# Logical Operators
# Three logical operators exists in Python
# 1. and  (&)
# 2. or (|)
# 3. not (!)


t = 20

if t > 10 & t > 12:
    print("Logical and is real")
elif t > 30 | t < 2:
    print("Logical or is real")
elif t == 30:
    print("Logical not is real")
else:
    print("Logical and is unreal")

# Identity Operators
# 1. is
# 2. is not

p = 20
sweetFruits = ['Apple', 'Orange', 'Mango']
sweetestFruits = ['Pineaple', 'Banana', 'Fenesi']
print(sweetFruits is not sweetestFruits)


# Membership Operators
# in - shows belongingness of objects/items in a particular family of things
# not in - Negation of in operator

if 'Chungwa' not in sweetFruits:
    print("Chungwa is a sweet fruit")
elif 'Fenesi' not in sweetestFruits:
    print("Chungwa is a sweetest fruit")
else:
    print('Chungwa is not sweet at all')
