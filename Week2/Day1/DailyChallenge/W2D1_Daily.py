#Old MacDonald’s Farm
# Create a class called Farm (to represent a farm and its animals).

# Inside __init__, create two attributes: name to store the farm’s name and animals to store the animals (initialize as an empty dictionary).
# It should take one parameter: farm_name.

# Create a method called add_animal.
# It should take two parameters: animal_type and count (with a default value of 1). Count is the quantity of the animal that will be added to the animal dictionary.
# The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
# If the animal_type already exists in the animals dictionary, increment its count by count.
# If it doesn’t exist, add it to the dictionary as the key and with the given count as value.

# Create a method called get_info.
# It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
# Format the output to match the provided example.
# Use string formatting to align the animal names and counts into columns.

# Step 5: Test Your Code
# Create a Farm object and call the add_animal and get_info methods.
# Verify that the output matches the provided Example:
# class Farm:
#     def __init__(self, farm_name):
#         # ... code to initialize name and animals attributes ...
#     def add_animal(self, animal_type, count):
#         # ... code to add or update animal count in animals dictionary ...
#     def get_info(self):
#         # ... code to format animal info from animals dictionary ...

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow', 5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# #output:
# # McDonald's farm
# # cow : 5
# # sheep : 2
# # goat : 12
# #     E-I-E-I-0!


# Bonus: Expand The Farm
# Add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all animal types (keys from the animals dictionary).
# Use the sorted() function to sort the list.

# Add a method called get_short_info to the Farm class.
# This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.

# Call the get_animal_types method to get the list of animals.
# Construct the string, adding an “s” to the animal name if its count is greater than 1.
# Use string formatting to create the output.

class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name  # Store the farm name
        self.animals = {}  # Initialize an empty dictionary for animals

    def add_animal(self, animal_type, count=1):
        # If the animal type already exists, increase its count
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            # If the animal type does not exist, add it with the specified count
            self.animals[animal_type] = count

    def get_info(self):
        # Build the information string
        info = f"{self.farm_name}'s farm\n"
        # Format animal types and counts into a neat table
        for animal, count in self.animals.items():
            info += f"{animal: <10}: {count}\n"  # Align animal names to the left
        # Append the "E-I-E-I-O!" phrase
        info += "     E-I-E-I-O!"
        return info

    def get_animal_types(self):
        # Return a sorted list of animal types (keys from the animals dictionary)
        return sorted(self.animals.keys())

    def get_short_info(self):
        # Construct a string with pluralized animal names based on their count
        animals = [f"{animal}s" if count > 1 else animal for animal, count in self.animals.items()]
        return f"{self.farm_name}'s farm has " + ", ".join(animals) + "."

# Step 5: Testing the Code

# Create a Farm object
macdonald = Farm("McDonald")

# Add animals to the farm
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')  # Defaults to 1
macdonald.add_animal('sheep')  # Increments to 2
macdonald.add_animal('goat', 12)

# Get the farm info
print(macdonald.get_info())

# Output:
# McDonald's farm
# cow       : 5
# sheep     : 2
# goat      : 12
#      E-I-E-I-O!

# Get the sorted list of animal types
print(macdonald.get_animal_types())  # ['cow', 'goat', 'sheep']

# Get short information about the farm
print(macdonald.get_short_info())  # McDonald's farm has cows, goats and sheeps.
