# 🌟 Exercise 1: Cats
# Use the Cat class to create three cat objects with different names and ages.
# Create a function that takes the three cat objects as input,
# and return the oldest cat object.
# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1 = Cat("Mitzy",2)
cat2 = Cat("Pitzy",5)
cat3 = Cat("Roxy",10)

def find_oldest_cat(*args):
    oldest_cat=args[0]
    for cat in args[1:]:
        if cat.age > oldest_cat.age:
            oldest_cat=cat
    return oldest_cat
oldest=find_oldest_cat(cat1,cat2,cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

# 🌟 Exercise 2 : Dogs
# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.
# Step 1: Create the Dog Class
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “ goes woof!”.
# Create a jump() method that prints “ jumps cm high!”, where x is height * 2.
# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.
# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.
# Step 4: Compare Dog Sizes

class Dog():
    def __init__(self, name, height):
        self.name=name
        self.height=height
        print("A new dog has been created")
        print("His name is", name)
    def bark(self):
        print(self.name, "goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height*2}cm high!")
davids_dog = Dog("T-Rex", 80)
sarahs_dog = Dog("Roxy", 18)
print(f"David's dog name is {davids_dog.name} and his height is {davids_dog.height}cm")
print(f"Sarah's dog name is {sarahs_dog.name} and his height is {sarahs_dog.height}cm")
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name, "is the bigger dog!")
else:
    print(sarahs_dog.name, "is the bigger dog :)")

# 🌟 Exercise 3 : Who’s the song producer?
# Create a Song class with a method to print song lyrics line by line.
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.
# Example:
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"]
class Song():
    def __init__(self, lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for i in range(len(self.lyrics)):
            print(self.lyrics[i])

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# 🌟 Exercise 4 : Afternoon at the Zoo
# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.
# 1. Create a class called Zoo.
# 2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.
# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.
# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.
# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.
# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.
# Example output:
# {
#    'B': ['Baboon', 'Bear'],
#    'C': ['Cat', 'Cougar'],
#    'G': ['Giraffe'],
#    'L': ['Lion'],
#    'Z': ['Zebra']
# }
# 7. Add a method get_groups():
# This method prints the grouped animals as created by sort_animals().
# Example output:
# B: ['Baboon', 'Bear']
# C: ['Cat', 'Cougar']
# G: ['Giraffe']
# ...

# Step 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.

# Step 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name  # Store the zoo name
        self.animals = []         # Initialize an empty list to store animal names

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to the zoo!")
        else:
            print(f"{new_animal} is already in the zoo!")

    def get_animals(self):
        if self.animals:
            print("Animals in the zoo:")
            for animal in self.animals:
                print(animal)
        else:
            print("There are no animals in the zoo.")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold!")
        else:
            print(f"{animal_sold} is not in the zoo!")

    def sort_animals(self):
        self.animals.sort()  # Sort the animals alphabetically
        
        # Group animals by their first letter
        grouped_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()  # Get the first letter and capitalize it
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        
        return grouped_animals

    def get_groups(self):
        groups = self.sort_animals()  # Get the grouped animals
        if groups:
            for letter, group in groups.items():
                print(f"{letter}: {group}")
        else:
            print("No animals to group.")

# Create an instance of the Zoo class
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Add animals
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")

# Display all animals
ramat_gan_safari.get_animals()

# Sell an animal
ramat_gan_safari.sell_animal("Bear")

# Display all animals after selling one
ramat_gan_safari.get_animals()

# Sort and group animals
ramat_gan_safari.sort_animals()

# Display grouped animals
ramat_gan_safari.get_groups()
