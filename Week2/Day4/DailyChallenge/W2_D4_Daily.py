
# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.

# Part I: Analyzing a Simple String
# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g., self.text).

# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.

# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.

# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.

# Part II: Analyzing Text from a File
# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.

# Bonus: Text Modification
# Create a class called TextModification that inherits from Text.

# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.

# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.

# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.

import string
import re

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else f"The word '{word}' does not appear in the text."

    def most_common_word(self):
        words = self.text.lower().split()
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        most_common = max(frequency, key=frequency.get)
        return most_common

    def unique_words(self):
        words = self.text.lower().split()
        unique = set(words)
        return list(unique)

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return cls(content)
        except FileNotFoundError:
            return f"File not found: {file_path}"

class TextModification(Text):
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = self.text.translate(translator)
        return cleaned_text

    def remove_stop_words(self):
        stop_words = set([
            "a", "an", "the", "is", "are", "was", "were", "in", "on", "at", "of", "and", 
            "or", "but", "if", "to", "with", "as", "by", "for", "this", "that", "these", 
            "those", "it", "be", "has", "have", "had", "not", "do", "does", "did", "so"
        ])
        words = self.text.lower().split()
        filtered_words = [word for word in words if word not in stop_words]
        return ' '.join(filtered_words)

    def remove_special_characters(self):
        cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return cleaned_text

#example:
text = Text("This is a test. This test is only a test.")
print(text.word_frequency("test"))           # Output: 3
print(text.most_common_word())               # Output: 'test'
print(text.unique_words())                   # Output: ['this', 'is', 'a', 'test.', 'test', 'only']

mod_text = TextModification("Hello! This is a test, with punctuation... and special characters #1.")
print(mod_text.remove_punctuation())         # Output: 'Hello This is a test with punctuation and special characters 1'
print(mod_text.remove_stop_words())          # Output: 'hello! test, punctuation... special characters #1.'
print(mod_text.remove_special_characters())  # Output: 'Hello This is a test with punctuation and special characters 1'
