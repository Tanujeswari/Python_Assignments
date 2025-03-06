# car.py
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        print(f"This is a {self.brand} {self.model}.")


# person.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")


# __init__.py (Simulating it inside the same file for this example)
# This normally exists in the package directory to mark it as a Python package
# For this single file example, we will just import the classes below.

# Importing the respective classes from other files
from car import Car
from person import Person # type: ignore


# main.py (Main program to create objects and call methods)
def main():
    # Creating an object of the Car class
    my_car = Car("Toyota", "Corolla")
    my_car.car_info()  # Calling the method of the Car class

    # Creating an object of the Person class
    person = Person("Alice", 30)
    person.person_info()  # Calling the method of the Person class


if __name__ == "__main__":
    main()
