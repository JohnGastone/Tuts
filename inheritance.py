# Inheritance allows us to define a class that inherits all the methods
# and properties from another class.

# In inheritance we have two kind of classes namely Parent and Child classes.

# A Parent class is the class being inherited from, sometimes it is termed as Base class.
# A Child class is the class that inherits from another class, also termed as Derived class.

# Creating a Parent Class : This is just a normal class creation

class Parent:
    def __init__(self, name, age, religion):
        self.name = name
        self.age = age
        self.religion = religion

    def possessions(self):
        print('''This is the possession of this Parent, 
              all of its children will inherit them''')

    def profile(self):
        print("Her name is " + self.name)
        print("Her age is " + str(self.age))
        print("Her religion is " + self.religion)


Baba = Parent(name="Mshua Masta", age=45, religion="Budha")

# Baba.possessions()
# Creating a Child Class : This is just a normal class creation


class Child(Parent):
    print('This is the first child of the above parent')


mtoto = Child("Festi boni", 20, "Hindu")
mtoto.profile()
