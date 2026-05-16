# Single Inheritance
# Single inheritance is a type of inheritance where a class inherits
# properties and behaviors from a single parent class.


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):  # method overriding
        print("Bark!")
