# Exercise 1:

# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

print ("Hello world\n"*4)

# Exercise 2:

# Write code that calculates the result of:

# (99^3)*8 (meaning 99 to the power of 3, times 8).

result = (99**3)*8
print (result)

# Exercise 3:

# Predict the output of the following code snippets:

# >>> 5 < 3
# >>> 3 == 3
# >>> 3 == "3"
# >>> "3" > 3
# >>> "Hello" == "hello"

#Answer:

# False
# True
# False
# False (TYPE ERROR)
# False

# Exercise 4:

# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

computer_brand = "MSI"
print ("I have a "+computer_brand+" computer.")

# Exercise 5:

# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.
    
name = "Sagi"
age = "44"
shoe_size = "42"
info = "My name is "+name+" and my age is "+age+".\nI wear a "+shoe_size+" size shoes and I love Avocado!"
print (info)

# Exercise 6:

# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".

a = 33
b = 9
if a>b :
    print ("Hello World")

# Exercise 7:

# Write code that asks the user for a number and determines whether this number is odd or even.

number = input('Please type a number: \n')
if int(number)%2:
    print ("your number is odd")
else:
    print ("your number is even")

# Exercise 8:

# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

my_name="Sagi"
user_name=input("Please enter your name:\n").rstrip().lstrip()

if my_name.lower()==user_name.lower():
    print("same name")
else:
    print ("your name is different so we are not the same person :)")

# Exercise 9:

# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

user_height = int(input("Please enter your Height (rounded) in centimeters:\n"))
if user_height>145:
    print("You are tall enough")
else:
    print("Sorry. you are not tall enough.\nyou should wait a little longer to grow :)")

