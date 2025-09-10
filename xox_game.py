def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

boarded = []   # create an empty board
for i in range(3):          # loop for rows
    x = []                  # create an empty row
    for j in range(3):      # loop for columns
        x.append("_")       # add "_" to the row
    boarded.append(x)       # add row to the board

# Show the internal board list
print(boarded)

# Print the board nicely
for row in boarded:
    print(" | ".join(row))
    print("-" * 5)


"""

# Tic-Tac-Toe (XOX) Game

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Ask for move
        row = int(input("Enter row (0,1,2): "))
        col = int(input("Enter col (0,1,2): "))

        # Check valid move
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = current_player

        # Check win
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        # Check draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()

"""