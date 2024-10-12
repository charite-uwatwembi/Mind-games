import random

# 1. Generate random pairs of letters
def generate_letter_pairs():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:12]  # 12 unique letters
    pairs = list(letters) * 2
    pairs += [" "]  # Fill the last spot
    random.shuffle(pairs)
    return pairs

# 2. Create the 5x5 grid with random pairs
def create_board():
    pairs = generate_letter_pairs()
    return [pairs[i*5:(i+1)*5] for i in range(5)]

# 3. Initialize a board to track revealed positions
def create_revealed_board():
    return [["X"] * 5 for _ in range(5)]

# 4. Display the current board to the player
def display_board(revealed_board, board):
    print("\nCurrent Board:")
    for row_revealed, row_board in zip(revealed_board, board):
        for revealed, letter in zip(row_revealed, row_board):
            if revealed == "X":
                print("X", end=" ")
            else:
                print(letter, end=" ")
        print()
    print()

# 5. Get valid user input
def get_user_input():
    while True:
        try:
            x, y = map(int, input("Enter row and column (0-4) separated by a space: ").split())
            if 0 <= x < 5 and 0 <= y < 5:
                return x, y
            else:
                print("Invalid input! Coordinates must be between 0 and 4.")
        except ValueError:
            print("Invalid input! Please enter two numbers.")

# 6. Reveal tiles and check for matches
def reveal_tiles(board, revealed_board, first_choice, second_choice):
    x1, y1 = first_choice
    x2, y2 = second_choice

    revealed_board[x1][y1] = board[x1][y1]
    revealed_board[x2][y2] = board[x2][y2]
    
    display_board(revealed_board, board)
    
    if board[x1][y1] == board[x2][y2]:
        print("It's a match!")
        return True
    else:
        print("Not a match!")
        revealed_board[x1][y1] = "X"
        revealed_board[x2][y2] = "X"
        return False

# 7. Check if all tiles are revealed
def check_win(revealed_board):
    for row in revealed_board:
        if "X" in row:
            return False
    return True

# 8. Main game loop
def play_game():
    board = create_board()
    revealed_board = create_revealed_board()
    
    while not check_win(revealed_board):
        display_board(revealed_board, board)
        
        print("Pick the first tile:")
        first_choice = get_user_input()
        
        print("Pick the second tile:")
        second_choice = get_user_input()
        
        reveal_tiles(board, revealed_board, first_choice, second_choice)
    
    print("Congratulations! You have revealed all the tiles.")

# Start the game
play_game()
