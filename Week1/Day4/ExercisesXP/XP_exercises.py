# 🌟 Exercise 1: What Are You Learning?
# Define a function named display_message().
# Step 2: Print a Message
# For example: “I am learning about functions in Python.”
# Step 3: Call the Function
def display_message():
    print("I am learning about functions in Python.")

display_message()

# 🌟 Exercise 2: What’s Your Favorite Book?
# Goal: Create a function that displays a message about a favorite book.
# Step 1: Define a Function with a Parameter named favorite_book().
# This function should accept one parameter called title.
# Step 2: Print a Message with the Title
# The function needs to output a message like “One of my favorite books is <title>”.
# Step 3: Call the Function with an Argument
# Call the favorite_book() function and provide a book title as an argument.
# For example: favorite_book("Alice in Wonderland").
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")

# 🌟 Exercise 3: Some Geography
# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.
# Inside the function, set up the code to display a sentence like “ is in “.
# Call the describe_city() function with different city and country combinations.
# Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").
def describe_city(city, country="Unknown"):
    print (f"The City {city} is in {country}")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

# 🌟 Exercise 4: Random
# Goal: Create a function that generates random numbers and compares them.
# Step 1: Import the random Module
# Step 2: Define a Function with a Parameter
# Create a function that accepts a number between 1 and 100 as a parameter.
# Step 3: Generate a Random Number
# Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.
# Step 4: Compare the Numbers
# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.
# Step 5: Call the Function
# Call the function with a number between 1 and 100.
# Expected Output:
# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)

import random
def random_guess(number_input):
    random_number=random.randint(1, 100)
    if type(number_input)!=int:
        print("invalid input type")
    elif number_input<1 or number_input>100:
        print("invalid input range")
    else:
        if random_number==number_input:
            print("Success!")
        else:
            print(f"Fail!\nYour number: {number_input}, Random number: {random_number}")

random_guess(55)

# 🌟 Exercise 5: Let’s Create Some Personalized Shirts!
# Goal: Create a function to describe a shirt’s size and message, with default values.
# Define a function called make_shirt().
# This function should accept two parameters: size and text.
# Set up the function to display a sentence summarizing the shirt’s size and message.
# Step 3: Call the Function
# Step 4: Modify the Function with Default Values
# Modify the make_shirt() function so that size has a default value of “large” and text has a default value of “I love Python”.
# Step 5: Call the Function with Default and Custom Values
# Call make_shirt() to make a large shirt with the default message.
# Call make_shirt() to make a medium shirt with the default message.
# Call make_shirt() to make a shirt of any size with a different message.
# Step 6 (Bonus): Keyword Arguments
# Call make_shirt() using keyword arguments (e.g., make_shirt(size="small", text="Hello!")).
# Expected Output:
# The size of the shirt is large and the text is I love Python.
# The size of the shirt is medium and the text is I love Python.
# The size of the shirt is small and the text is Custom message.

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt("L", "Rebellious")
make_shirt()
make_shirt("medium")
make_shirt(size="small", text="Hello!")

# 🌟 Exercise 6: Magicians…
# Create a list called magician_names with the given names:
# [‘Harry Houdini’, ‘David Blaine’, ‘Criss Angel’]
# Create a function called show_magicians() that takes the magician_names list as a parameter.
# Inside the function, iterate through the list and print each magician’s name.
# Create a function called make_great() that takes the magician_names list as a parameter.
# Inside the function, use a for loop to iterate through the list and add “the Great” before each magician’s name.
# Call make_great() to modify the list.
# Call show_magicians() to display the modified list.
# Expected Output:
# Harry Houdini the Great
# David Blaine the Great
# Criss Angel the Great

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(names):
    for name in names:
        print(name)
def make_great(names):
    for i in range(len(names)):
        names[i] = names[i] + ' the Great'

make_great(magician_names)
show_magicians(magician_names)

# 🌟 Exercise 7: Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.
# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.
# Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”
# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”

import random
def get_random_temp():
    return random.randint(-10, 40)
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 17 <= temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    elif 33 <= temp <= 40:
        print("It’s really hot! Stay cool.")

main()

# Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.
def get_random_temp():
    return round(random.uniform(-10, 40) ,2)
main()
