# Polymorphism allows objects of the class to have many forms or
# to exhibit numerous behaviors

# Polymorphism in Action

# Defining Super class
class Vehicle:   # Super class
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def Move(self):
        print("A moving vehicle")

# Defining sub classes


class Car(Vehicle):  # Sub class / Inheriting class
    print("This is car")


class Boat(Vehicle):  # Sub class / Inheriting class
    def move(self):
        print("A sailing boat")


class Plane(Vehicle):  # Sub class / Inheriting class
    def move(self):
        print("A flying plane")


# Creating Objects
fuso = Car("XYZ 22", "Toyota")
mvDodoma = Boat("Tata 23", "Azam Ferry")
airTanzania = Plane("Boeing 22", "Fly Emirates")


# Method calling
for x in (fuso, mvDodoma, airTanzania):
    print(x.brand)
    print(x.model)
    if x is mvDodoma:
        x.move()
    elif x is airTanzania:
        x.move()
    else:
        x.Move()
