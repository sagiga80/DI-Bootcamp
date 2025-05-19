# Exercise 1: Pets
# Create a class called Siamese that inherits from the Cat class.
# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Give each cat a name and age.
# Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.
# Call the walk() method on the sara_pets instance.

class Pets():
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())
class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# solution to excersize above, commented out:
# bengal_obj = Bengal("Bengi",4)
# chartreux_obj = Chartreux("Charti",6)
# siamese_obj = Siamese("Simi",8)
# all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# sara_pets = Pets(all_cats)
# sara_pets.walk()


# 🌟 Exercise 2: Dogs
# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “ is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.
# Create three instances of the Dog class with different names, ages, and weights.
# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.

class Dog():
    def __init__(self, name, age, weight):
        self.name=name
        self.age=age
        self.weight=weight
    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return (self.weight/self.age*10)
    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if self_power > other_power:
            return f"{self.name} won the fight"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight"
        else:
            return "It's a tie!"

# solution to excersize above, commented out:
# dog1=Dog("Roxy",10,5)
# dog2=Dog("T-Rex",5,100)
# dog3=Dog("Midi",4,12)
# print(dog1.bark())
# print(dog2.bark())
# print(dog3.bark())
# print(dog1.run_speed())
# print(dog2.run_speed())
# print(dog3.run_speed())
# print(dog1.fight(dog2))
# print(dog2.fight(dog1))
# print(dog3.fight(dog2))
# print(dog3.fight(dog1))
