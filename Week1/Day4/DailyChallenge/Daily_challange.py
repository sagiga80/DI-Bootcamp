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

# --- Decoding  Functions ---
def collect_non_alpha_chunk(chars, start_index):
    """Collect consecutive non-alpha characters starting from a given index."""
    j = start_index
    while j < len(chars) and not chars[j].isalpha():
        j += 1
    return j

def should_insert_space(chars, i, j):
    """Check if a space should be inserted between two alphabet characters."""
    return (
        i > 0
        and j < len(chars)
        and chars[i - 1].isalpha()
        and chars[j].isalpha()
    )

def decode_message(chars):
    """Decode the character list into a message, inserting spaces where needed."""
    message = ''
    i = 0
    while i < len(chars):
        if chars[i].isalpha():
            message += chars[i]
            i += 1
        else:
            j = collect_non_alpha_chunk(chars, i)
            if should_insert_space(chars, i, j):
                message += ' '
            i = j
    return message

final_message = decode_message(decoded_chars)
print(final_message)
