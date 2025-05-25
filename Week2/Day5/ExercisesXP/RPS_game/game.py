import random

class Game:
    def __init__(self):
        self.items = ['rock', 'paper', 'scissors']
        
    def get_user_item(self):
        """Get the user's choice (rock/paper/scissors)."""
        while True:
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if user_choice in self.items:
                return user_choice
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")
    
    def get_computer_item(self):
        """Randomly select an item for the computer (rock/paper/scissors)."""
        return random.choice(self.items)
    
    def get_game_result(self, user_item, computer_item):
        """Determine the result of the game based on user and computer choices."""
        if user_item == computer_item:
            return 'draw'
        elif (user_item == 'rock' and computer_item == 'scissors') or \
             (user_item == 'scissors' and computer_item == 'paper') or \
             (user_item == 'paper' and computer_item == 'rock'):
            return 'win'
        else:
            return 'loss'
    
    def play(self):
        """Play one round of the game."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        
        result = self.get_game_result(user_item, computer_item)
        
        print(f"You chose: {user_item}")
        print(f"Computer chose: {computer_item}")
        print(f"Result: You {result}!")
        
        return result
