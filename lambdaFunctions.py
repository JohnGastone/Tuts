# Lambda functions are small anonymous functions which are declared usually in a single line

# Declaring Lambda function
# lambda arguments : expression

'''
Normal functions and lambda functions (also known as anonymous functions) are both used to define and encapsulate blocks of code in programming, but they have some differences in terms of syntax, usage, and capabilities. Here's a comparison of normal functions and lambda functions:

**1. Syntax:**
- **Normal Function**: Defined using the `def` keyword, followed by a function name, parameters in parentheses, a colon, and a code block.
- **Lambda Function**: Defined using the `lambda` keyword, followed by parameters, a colon, and an expression.

**2. Name:**
- **Normal Function**: Has a name that can be used to call the function.
- **Lambda Function**: Is often anonymous (no formal name), but it can be assigned to a variable to use it.

**3. Size and Complexity:**
- **Normal Function**: Can be more complex and include multiple statements and control structures.
- **Lambda Function**: Is typically used for simple operations and consists of a single expression.

**4. Return Value:**
- **Normal Function**: Uses the `return` statement to return a value to the caller.
- **Lambda Function**: The result of the expression is automatically returned as the output of the function.

**5. Scope and Namespace:**
- **Normal Function**: Can have a larger scope and can access variables from the enclosing scope.
- **Lambda Function**: Usually operates within a more limited scope and has access to its parameters.

**6. Function Name and Documentation:**
- **Normal Function**: Can have a descriptive name and can include docstrings for documentation.
- **Lambda Function**: Lacks a formal name and is less suited for extensive documentation.

**7. Use Cases:**
- **Normal Function**: Well-suited for more complex tasks and reusable code.
- **Lambda Function**: Often used for simple transformations, filtering, and as arguments to higher-order functions like `map()`, `filter()`, and `sorted()`.

**8. Readability:**
- **Normal Function**: Can have meaningful names and be more descriptive, aiding code readability.
- **Lambda Function**: May sacrifice some readability due to its brevity and lack of a meaningful name.

**9. Multiple Expressions:**
- **Normal Function**: Can contain multiple expressions and statements, providing more flexibility.
- **Lambda Function**: Limited to a single expression, but you can use the expression to achieve complex results.

**10. Function Definition:**
- **Normal Function**: Can be defined anywhere in the code.
- **Lambda Function**: Is often used when a simple function is needed directly within an expression.

**Example:**
```python
# Normal function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))          # Output: 25
print(square_lambda(5))   # Output: 25
```

In summary, normal functions are more versatile and suitable for complex tasks, whereas lambda functions are concise and well-suited for simple operations and scenarios where a function is needed directly within an expression or as an argument to other functions. The choice between using a normal function or a lambda function depends on the specific context and requirements of your code.

'''

# Example 1


def x(a, z): return a * z + 5  # Lambda function


print(x(4, 3))


# Example 2
def mama(mtoto): return mtoto + " ni mtoto wa kwanza wa Anna"


print(mama("Ivy"))


# Example 3

def myfunc(n):
    return lambda a: a * n


myfunc(2)
print(myfunc(33))
