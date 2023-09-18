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

    def method(self):
        print("Just a method")

# Defining sub classes


class Car(Vehicle):  # Sub class / Inheriting class
    def move(self):
        print("Gari inayoendeshwa")


class Boat(Vehicle):  # Sub class / Inheriting class
    def move(self):
        print("A sailing boat")


class Plane(Boat):  # Sub class / Inheriting class
    pass


# Creating Objects
fuso = Car("XYZ 22", "Toyota")
mvDodoma = Boat("Tata 23", "Azam Ferry")
airTanzania = Plane("Boeing 22", "Fly Emirates")


# Method calling
# for x in (fuso, mvDodoma, airTanzania):
#     print(x.brand)
#     print(x.model)
#     if x is mvDodoma:
#         x.move()
#     elif x is airTanzania:
#         x.move()
#     else:
#         x.move()

if __name__ == "__main__":
    for x in (fuso, mvDodoma, airTanzania):
        print(x.brand)
        print(x.model)
        x.move()
