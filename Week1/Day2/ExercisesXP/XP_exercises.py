# 🌟 Exercise 1: Favorite Numbers
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.

my_fav_numbers=set()
my_fav_numbers.add(3)
my_fav_numbers.add(69)
my_fav_numbers.add(96)
my_fav_numbers.add(333)
print(my_fav_numbers)
my_fav_numbers.add(999)
my_fav_numbers.add(90)
print(my_fav_numbers)
my_fav_numbers.remove(90)
print(my_fav_numbers)
friend_fav_numbers=set()
friend_fav_numbers.add(4)
friend_fav_numbers.add(444)
friend_fav_numbers.add(44)
print(friend_fav_numbers)
our_fav_numbers=set()
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

print("\n")

# 🌟 Exercise 2: Tuple
# Given a tuple of integers, try to add more integers to the tuple.

integers_tuple=(3,333,9)
print(integers_tuple)
integers_list=list(integers_tuple)
integers_list.extend([444,8])
print(integers_list)
integers_tuple=tuple(integers_list)
print(integers_tuple)

print("\n")

# 🌟 Exercise 3: List Manipulation
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
apples_count=basket.count("Apples")
print(apples_count)
basket.clear()
print(basket)

print("\n")

# 🌟 Exercise 4: Floats
# Create a list containing the following sequence of mixed floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.

mixed_numbers = [int(x) if x.is_integer() else x for x in [x / 2 for x in range(3, 11)]]
print(mixed_numbers)

print("\n")

# 🌟 Exercise 5: For Loop
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1,21):
    print(i)
print("\n")
for i in range(1,21):
    if i%2:
        print(i)

print("\n")

# 🌟 Exercise 6: While Loop
# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.

my_name="sagi"
user_input=""
while user_input!=my_name:
    user_input=input("Please enter your name:\t")
    user_input=user_input.lower()
print("We have the same name!")

print("\n")

# 🌟 Exercise 7: Favorite Fruits
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

favorite_fruits_input = input("Enter your favorite fruits (separated by spaces): \n")
favorite_fruits = [fruit.lower() for fruit in favorite_fruits_input.split()]
chosen_fruit = input("Enter the name of any fruit: ").lower()
if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

print("\n")

# 🌟 Exercise 8: Pizza Toppings
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): \t")
    if topping.lower() == 'quit':
        break    
    print("Adding "+ topping + " to your pizza.")
    toppings.append(topping)
cost = 10 + 2.5 * len(toppings)
print("\nYour pizza will have the following toppings:")
for t in toppings:
    print(f"- {t}")
print(f"Total cost: ${cost:.2f}")

print("\n")

# 🌟 Exercise 9: Cinemax Tickets
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

# Bonus:
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

total_tickets_cost = 0
while True:
    age_input = input("Enter the person's age (or type 'done' to finish): ")
    if age_input.lower() == 'done':
        break
    age = int(age_input)
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    total_tickets_cost += cost
print(f"The Total ticket cost is: ${total_tickets_cost}")

print("\n")

# 🌟 Exercise 10: Sandwich Orders
# Using the list:
# sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
# The deli has run out of “Pastrami”, so use a loop to remove all instances of “Pastrami” from the list.
# Prepare each sandwich, one by one, and move them to a list called finished_sandwiches.
# Print a message for each sandwich made, such as: "I made your Tuna sandwich."
# Print the final list of all finished sandwiches.

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
print(sandwich_orders)
finished_sandwiches=[]
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print("I made your "+sandwich+" sandwich.")
print("\nFinal list of all finished_sandwiches:")
print(finished_sandwiches)
