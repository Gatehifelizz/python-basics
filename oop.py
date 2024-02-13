class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def describe_car(self):
        print(f"I own a {self.make}  {self.model} manufactured in {self.year} thats painted {self.color} ")


myobj = Car("Volkswagen ", "beetle", 2021, "grey")
myobj.describe_car()
myobj2 = Car("Toyota", "Fj cruiser", 2020, "blue")
myobj2.describe_car()


class Gari:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_gari(self):
        return f"The {self.make} {self.year} {self.model} "

    def read_odometer(self):
        return f"This car has {self.odometer_reading} mileage"

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Gari("porsche", "cayenne", 2006)
print(my_car.describe_gari())
print(my_car.read_odometer())
my_car.update_odometer(100)
print(my_car.read_odometer())
my_car.increment_odometer(50)
print(my_car.read_odometer())

# Polymorphism and INHERITANCE
class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I feed on meat")
class Dog(Animal):
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"
class Cat(Animal):
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says meow!"
bosco=Dog("bosco")
coco=Cat("coco")
print(bosco.speak())
print(coco.speak())

class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplemented("subclass must implement this abstract function")
my_animal=Animal("bosco")
my_animal.speak()
