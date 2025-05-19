# 🌟 Exercise 3: Dogs Domesticated
# In a new Python file, import the Dog class from the previous exercise.
# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.
# Implement a play(*args) method that prints “ all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the random tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a random index from it each time the method is called.
# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.
import random
import Dogs
class PetDog(Dogs.Dog):
   def __init__(self, name, age, weight):
       super().__init__(name, age, weight)
       self.trained = False
   def train(self):
       print(self.bark())
       self.trained = True
   def play(self, *args):
#       dog_names = [dog.name for dog in args]
        print (f"{args} all play together")
   def do_a_trick(self):
       if self.trained:
           tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
           print(f"{self.name} {random.choice(tricks)}")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()

# Exercise 4: Family and Person Classes
# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.
# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)
# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.
# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."
# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""  # Initialized as an empty string
    def is_18(self):
        return self.age >= 18
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name  # Assign family's last name
        self.members.append(new_person)
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No family member named {first_name} found.")
    def family_presentation(self):
        print(f"Family: {self.last_name}")
        print("Members:")
        for member in self.members:
            print(f"{member.first_name}, Age: {member.age}")

# instantiate a family and add persons using 'born' method:
codi_family = Family("Codi")
codi_family.born("Alice", 16)
codi_family.born("Bob", 20)
codi_family.born("Charlie", 12)
# test majority method:
codi_family.check_majority("Bob")      # Should allow
codi_family.check_majority("Charlie")  # Should not allow
codi_family.check_majority("John")     # Person not found
# family presentation:
codi_family.family_presentation()
