# 🌟 Exercise 1: Currencies
# Goal: Implement dunder methods for a Currency class to 
# handle string representation, integer conversion, addition, and in-place addition.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        return f"{self.amount} {self.currency}s"
    def __repr__(self):
        return f"{self.amount} {self.currency}s"
    def __int__(self):
        return self.amount
    def __add__(self,other):
        if type(other) == type(self):
            if self.currency==other.currency:
                return self.amount+other.amount
            else:  # TypeError: Cannot add between Currency type <dollar> and <shekel>
                raise TypeError (f"Cannot add between Currency type {self.currency} and {other.currency}")
        else:
            return self.amount+other
    def __iadd__(self,other):
        if type(other) == type(self):
            if self.currency==other.currency:
                self.amount+=other.amount
                return self
            else:  # TypeError: Cannot add between Currency type <dollar> and <shekel>
                raise TypeError (f"Cannot add between Currency type {self.currency} and {other.currency}")
        else:
            self.amount+=other
            return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output:
print(int(c1))    # 5
print(repr(c1))   # '5 dollars'
print(c1 + 5)     # 10
print(c1 + c2)    # 15
print(c1)         # '5 dollars'
c1 += 5
print(c1)         # 10 dollars
print(c2)         # 10 dollars
c1 += c2
print(c1)         # 20 dollars
try:
    print(c1 + c3)    # TypeError: Cannot add between Currency type <dollar> and <shekel>
except:
    print(TypeError)

# 🌟 Exercise 2: Import
# Create a file named func.py.
# Define a function inside that file that takes two numbers as arguments, sums them, and prints the result.
# Create a file named exercise_one.py.
# Import the function from func.py using one of the import syntaxes provided in the instructions.
# Call the imported function with two numbers.


# 🌟 Exercise 3: String module
# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.

# Import the string and random modules.
# Step 2: Create a string of all letters
# Step 3: Generate a random string
# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.

import string
import random
letters = string.ascii_letters
random_string = ''
for _ in range(5):
    random_char = random.choice(letters)
    random_string += random_char
print(random_string)

# 🌟 Exercise 4: Current Date
# Use the datetime module to create a function that displays the current date.
# Step 1: Import the datetime module
# Step 2: Get the current date
# Step 3: Display the date

import datetime
today=datetime.datetime.today()
print(today.strftime("%d/%m/%y"))

# 🌟 Exercise 5: Amount of time left until January 1st
# Use the datetime module to calculate and display the time left until January 1st.
# Step 1: Import the datetime module
# Step 2: Get the current date and time
# Step 3: Create a datetime object for January 1st of the next year
# Step 4: Calculate the time difference
# Step 5: Display the time difference

import datetime
now = datetime.datetime.now()
next_jan_1st = datetime.datetime(year=now.year + 1, month=1, day=1)
time_left = next_jan_1st - now
print("Time left until January 1st:", time_left)

# 🌟 Exercise 6: Birthday and minutes
# Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then displays a message stating how many minutes the user lived in his life.

import datetime
def minutes_lived(birthdate_str):
    birthdate = datetime.datetime.strptime(birthdate_str, "%d-%m-%Y")
    now = datetime.datetime.now()
    time_lived = now - birthdate
    # Convert to minutes
    minutes = int(time_lived.total_seconds() // 60)
    print(f"You have lived approximately {minutes:,} minutes.")

# Example usage:
minutes_lived("01-06-1980")

# 🌟 Exercise 7: Faker Module
# Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.
# Install the faker module and use it to create a list of dictionaries, where each dictionary represents a user with fake data.
# Step 1: Install the faker module
# Step 2: Import the faker module
# Step 3: Create an empty list of users
# Step 4: Create a function to add users
# Create a function that takes the number of users to generate as an argument.
# Inside the function, use a loop to generate the specified number of users.
# For each user, create a dictionary with the keys name, address, and language_code.
# Use the faker instance to generate fake data for each key:
# name: faker.name()
# address: faker.address()
# language_code: faker.language_code()
# Append the user dictionary to the users list.
# Step 5: Call the function and print the users list

from faker import Faker
faker=Faker()
users=[]

def add_users(num):
    for _ in range(num):
        user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code()
        }
        users.append(user)

add_users(10)
print(users)
