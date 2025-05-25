from game import Game

def get_user_menu_choice():
    """Display the menu and get the user's choice."""
    while True:
        print("\nMenu:")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        user_choice = input("Enter your choice (1, 2, or 3): ")
        if user_choice in ['1', '2', '3']:
            return user_choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def print_results(results):
    """Display the results in a friendly format."""
    print("\nGame Summary:")
    print(f"Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}")
    print("Thank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        user_choice = get_user_menu_choice()
        
        if user_choice == '1':  # Play a new game
            game = Game()
            result = game.play()
            results[result] += 1
        
        elif user_choice == '2':  # Show scores
            print_results(results)
        
        elif user_choice == '3':  # Quit
            print_results(results)
            break

if __name__ == "__main__":
    main()
