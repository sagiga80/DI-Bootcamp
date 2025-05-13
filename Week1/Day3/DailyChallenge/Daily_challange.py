# Challenge 1: Letter Index Dictionary
# Goal: Create a dictionary of indices of each letter in a user input.

# Iterate through characters and check if each character is already a key in the dictionary.
# If it is, append the current index to the list associated with that key.
# If it is not, create a new key-value pair in the dictionary.
# Ensure that the characters (keys) are strings.
# Ensure that the indices (values) are stored in lists.

user_word = input("Please enter a word: \n")
letter_indices = {}

# Iterate over the word with index
for index, letter in enumerate(user_word):
    if letter in letter_indices:
        letter_indices[letter].append(index)
    else:
        letter_indices[letter] = [index]

print("Letter Index Dictionary:\n", letter_indices)
print("\n")


# Challenge 2: Affordable Items
# Goal: Create a program that prints a list of items that can be purchased with a given amount of money.

# 1. Store Data:
# You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign).
# You will also be given a string (wallet) representing the amount of money you have.
# 2. Data Cleaning:
# 3. Determining Affordable Items:
# 4. Sorting and Output:
# Sort the list of affordable items in alphabetical order.
# If the list is empty (no items can be afforded), return the string “Nothing”.
# Otherwise, return the sorted list.
# 5. Examples:
# Given:
# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"
# The output should be: ["Bread", "Fertilizer", "Water"].

