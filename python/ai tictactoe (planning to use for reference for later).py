# Tic Tac Toe Game in Python

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there's a winner or a tie."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    # Check for a tie
    for row in board:
        if " " in row:
            return None
    return "Tie"

def tic_tac_toe():
    """Main function to play the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Get player input
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] != " ":
                print("Invalid move! Cell already taken.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 1 and 9.")
            continue

        # Make the move
        board[row][col] = current_player
        print_board(board)

        # Check for a winner
        result = check_winner(board)
        if result:
            if result == "Tie":
                print("It's a tie!")
            else:
                print(f"Player {result} wins!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()