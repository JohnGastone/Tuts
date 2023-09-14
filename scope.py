import iterator

# Scope determines the extent of usage of some entities in a file.

# Two kinds of Scope do exist
# 1. Global Scope - This enables entity usage across the whole file.
time = 1230  # Global Variable


def kazi():
    print(n1)


def kazikazi():
    print(n1)
# 2. Local Scope - This enables entity usage only within defined locale.


def nyumbani():
    global n1        # global keyword
    n1 = "Kijichi kwetu"  # Global Variable
    print(n1)
    print(time)


print(iterator.myCollection)
