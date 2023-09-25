# Exceptions are errors which arise due to semantic and syntax errors

# Exception handling involves all actions that are taken to detect and expose exceptions in programs


# We use try---catch to detect and capture errors

# try block is responsible to test a program  and enable detection of errors

# catch | except in pyhon - handles the exception raised by catch block
'''
try:
    # Code that may raise exception
except Exception as e:
    # Code to handle exceptions

'''

# Ex 1
# x = 3
# y = 5
# try:
#     x > 3 & y < 7
# except Exception as e:
#     print("Exception raised")


# # Ex 2
# def divide(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         result = "Error: Division by zero"
#         print("This runs whenever an exception is raised ")
#     return result


# try:
#     numerator = 10
#     denominator = 0
#     result = divide(numerator, denominator)
#     print(f"Result: {result}")
# except Exception as e:
#     print(f"An exception occurred: {e}")
# finally:
#     print("Execution complete.")


# Ex 3

try:
    file = open("non_existent.txt", "r")
    content = file.read()
    file.close
except FileNotFoundError as e:
    print(f"File not found error: {e}")
except Exception as e:
    print(f"An exception occured: {e}")
finally:
    print("File handling complete")
