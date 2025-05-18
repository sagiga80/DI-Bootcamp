# Create a (command line) TicTacToe game in Python where two players can compete (marking a 3x3 grid)
# Players take turns marking empty squares with their symbol (‘O’ or ‘X’).
# The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.
# If all squares are filled and no player has three in a row, the game is a tie.

# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).
# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.

# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.

# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.

# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.

# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).

def display_board(matrix):
    print(f"-{matrix[0][0]}-{matrix[0][1]}-{matrix[0][2]}-")
    print(f"-{matrix[1][0]}-{matrix[1][1]}-{matrix[1][2]}-")
    print(f"-{matrix[2][0]}-{matrix[2][1]}-{matrix[2][2]}-")

def get_position(input):
    mapping = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2),
    }
    return mapping.get(input)

def player_input(board, player):
    while True:
        player_input = input(f"\nPlayer {player}, choose a tile (1-9): ").strip()
        if player_input not in "123456789":
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        row, col = get_position(player_input)
        if board[row][col] != " ":
            print("This tile is already marked.")
            continue
        return row, col

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_tie(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False  # Found an empty space, so it's not a tie yet
    return True  # All cells are filled and no winner, it's a tie

def switch_player(current):
    return "O" if current == "X" else "X"

def play():
    board = [[" ", " ", " "] for _ in range(3)]  #building a new board with list comprehension
    current_player = "X"
    
    print("\nWelcome to the Tic Tac Toe game!")
    print("The tiles are numbered as shown:")
    example_matrix = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    display_board(example_matrix)

    while True:  #playing the game in an 'infinite' loop until there is a win or a tie
        row, col = player_input(board, current_player)
        board[row][col] = current_player
        print("\n")
        display_board(board)

        if check_win(board, current_player):
            print(f"\nPlayer {current_player} wins!")
            break
        elif check_tie(board):
            print("\nIt's a tie!")
            break
        else:
            current_player = switch_player(current_player)

play()