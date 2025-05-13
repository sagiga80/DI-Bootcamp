# 🌟 Exercise 1: Converting Lists into Dictionaries
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))

# 🌟 Exercise 2: Cinemax #2
# Write a program that calculates the total cost of movie tickets for a family based on their ages.
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

family = {"Rick": 43, "Beth": 23, "Morty": 5, "Summer": 8}
total_cost = 0
print("\n")

for member, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"Ticket price for {member.title()} (age {age}) is ${price}")
    total_cost += price

print(f"\nTotal tickets cost: ${total_cost}\n")

# 🌟 Exercise 3: Zara

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

# Create a dictionary called brand with the provided data.
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.

# Bonus:
# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print(f"Zara's clothes are great for {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print("The last international competitor is:", brand["international_competitors"][-1])
print("Major colors in the US:", brand["major_color"]["US"])
print("Number of keys:", len(brand))
print("All keys:", list(brand.keys()))

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7500
}
brand.update(more_on_zara)
print("\nThe updated dictionary:")
print(brand)
print("\n")
# 🌟 Exercise 4: Disney Characters
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
# 1. Create a dictionary that maps characters to their indices:
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# 2. Create a dictionary that maps indices to characters:
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

dict1 = {name: index for index, name in enumerate(users)}
print("1. Characters to indices:", dict1)
dict2 = {index: name for index, name in enumerate(users)}
print("2. Indices to characters:", dict2)
sorted_users = sorted(users)
dict3 = {name: index for index, name in enumerate(sorted_users)}
print("3. Alphabetical characters to indices:", dict3)
print("\n")
