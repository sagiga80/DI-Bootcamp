# Goal: Decrypt a hidden message from a matrix string by processing it column-wise and filtering characters.

# You are given a “Matrix” string:

# MATRIX_STR = '''
# 7ii
# Tsx
# h%?
# i #
# sM 
# $a 
# #t%'''       

# Imagine this string arranged in rows and columns, forming a grid.
# transform this string into a 2D list (a list of lists), where each inner list represents a row.
# read the matrix column by column, from top to bottom, starting from the leftmost column.
# write code that iterates through the columns of your 2D list.
# Think about how you can access the elements of a 2D list by column.
# Filter Alpha Characters (letters).
# For each character in a column, check if it’s an alpha character.
# If it is, add it to a temporary string.
# Think about how you can check if a character is an alphabet letter.

# Step 4: Replacing Symbols with Spaces
# Replace every group of symbols (non-alpha characters) between two alpha characters with a space.
# After you have gathered the alpha characters, you will need to iterate through them, and where there are non alpha characters between them, you will insert a space.
# Think about how you can keep track of when you encounter an alphabet character, and when you encounter a non alphabet character.

# Step 5: Constructing the Secret Message
# Combine the filtered and processed characters to form the decoded message.
# Print the decoded message.

MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''

rows = MATRIX_STR.strip().split('\n')
# creating a list of lists:
matrix = [list(row) for row in rows]

decoded_chars = []
num_cols = len(matrix[0])
num_rows = len(matrix)
for col in range(num_cols):
    for row in range(num_rows):
        decoded_chars.append(matrix[row][col])
# Replacing non-alpha (between letters only) with a space
final_message = ''
i = 0
while i < len(decoded_chars):
    char = decoded_chars[i]
    if char.isalpha(): #built in method to check if a character is alpha (letter)
        final_message += char
        i += 1
    else:
        j = i
        symbol_chunk = ''
        while j < len(decoded_chars) and not decoded_chars[j].isalpha():
            symbol_chunk += decoded_chars[j]
            j += 1
        # If surrounded by letters, replace with a space
        if i > 0 and j < len(decoded_chars) and decoded_chars[i-1].isalpha() and decoded_chars[j].isalpha():
            final_message += ' '
        i = j
print(final_message)
