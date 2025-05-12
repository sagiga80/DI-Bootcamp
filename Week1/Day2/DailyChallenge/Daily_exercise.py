# Challenge 1: Multiples of a Number
# 1. Ask the user for two inputs:
# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

input_number=int(input("Please enter a number:   "))
input_length=int(input("Please enter the length: "))
multiples=[]
for n in range(1, input_length+1):
    multiples.append(input_number*n)
print(multiples)

print("\n")

# Challenge 2: Remove Consecutive Duplicate Letters
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
# 3. The program should print the modified string.

string_input=input("Please enter a String:\n")
list_string=[]
list_string.append(string_input[0])
for char in string_input[1:]:
    if char != list_string[-1]:
        list_string.append(char)
modified_string="".join(list_string)
print(modified_string)
