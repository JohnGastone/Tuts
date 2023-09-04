'''
In Python, `self` is a special keyword that is typically the first parameter in the definition of a method within a class. It is used to refer to the instance of the class itself. While `self` is not a reserved keyword, it is a convention widely followed in Python.

Here's what `self` means and how it's used:

1. **Referring to the Instance**: Within a class, `self` is used to refer to the specific instance (object) of that class. When you call a method on an object, Python automatically passes that object as the first argument to the method, and by convention, this parameter is named `self`.

2. **Accessing Attributes**: `self` allows you to access and modify instance-specific attributes (variables) and call other methods defined within the class. For example, `self.attribute_name` refers to an instance variable, and `self.method_name()` calls a method of the instance.

3. **Creating and Managing State**: It's crucial for maintaining the state of an object. Instance variables defined with `self` store data that is unique to each instance of the class, allowing different objects to have their own independent states.

Here's a simple example to illustrate the use of `self`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # self.name is an instance variable
        self.age = age    # self.age is an instance variable
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
```

In this example, `self` is used within the `__init__` method to assign values to instance variables `self.name` and `self.age`. It is also used in the `introduce` method to access these instance variables.

When you create an instance of the `Person` class, `self` automatically refers to that instance:

```python
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

person1.introduce()  # Output: My name is Alice and I am 30 years old.
person2.introduce()  # Output: My name is Bob and I am 25 years old.
```

In this way, `self` helps differentiate and manage the state and behavior of individual objects created from the same class.

'''

# Defining a Class


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

# Creating objects


car1 = Car("Toyota", "Camry")
car2 = Car("Tesla", "Model S")


# Accessing attributes and calling methods
print(car1.brand)  # Output: Toyota
car2.drive()       # Output: Tesla Model S is driving.
