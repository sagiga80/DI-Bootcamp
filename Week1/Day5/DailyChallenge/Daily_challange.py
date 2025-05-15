# Challenge 1: Sorting
# Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’).
# The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.
# Use the input() function to get a string of words from the user.
# The words will be separated by commas.
# Step 2: Split the String
# Step 3: Sort the List and Join the Sorted List
# Print the resulting comma-separated string.

user_input=input("Please type a single string containing a few words separated by commas:\n")
new_string_list=user_input.split(',')
sorted_list=sorted(new_string_list)
result=",".join(sorted_list)
print(result)

# Challenge 2: Longest Word
# Write a function that takes a sentence as input and returns the longest word in the sentence.
# If there are multiple longest words, return the first one encountered.
# Characters like apostrophes, commas, and periods should be considered part of the word.
# 
# Define a function that takes a string (the sentence) as a parameter.
# Step 2: Split the Sentence into Words
# Step 3: Initialize Variables and Iterate Through the Words
# Step 5: Compare Word Lengths and Return the Longest Word

# Expected Output:
# longest_word("Margaret's toy is a pretty doll.") should return "Margaret's".
# longest_word("A thing of beauty is a joy forever.") should return "forever.".
# longest_word("Forgetfulness is by all means powerless!") should return "Forgetfulness".

def longest_word(sentence):
    words = sentence.split()
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word   
    return longest_word

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
