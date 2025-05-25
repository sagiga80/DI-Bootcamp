# Exercise 1: Quizz
# What is a class?
# A class is a blueprint for creating objects (instances).

# What is an instance?
# An instance is an individual object created from a class.

# What is encapsulation?
# Encapsulation is the concept of restricting access to an object

# What is abstraction?
# Abstraction is the concept of hiding the details and showing only the features of an object.

# What is inheritance?
# Inheritance is a mechanism in OOP where one class (child class) can inherit the attributes and methods of another class (parent class).

# What is multiple inheritance?
# Multiple inheritance is a feature in Python where a class can inherit from more than one parent class.

# What is polymorphism?
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.

# What is method resolution order (MRO)?
# MRO is the order in which classes are searched when calling a method or looking for an attribute.


# Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

# Deck class
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        # Create all 52 cards
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        # Shuffle the deck randomly
        random.shuffle(self.cards)

    def deal(self):
        # Deal one card from the deck
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None  # No cards left

# Examples:
deck = Deck()
deck.shuffle()
card = deck.deal()
print(f"Dealt card: {card}")
card = deck.deal()
print(f"Dealt card: {card}")
