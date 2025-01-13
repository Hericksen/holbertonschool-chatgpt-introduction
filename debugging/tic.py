def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonal (top-left to bottom-right) for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Check diagonal (top-right to bottom-left) for a winner
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def check_draw(board):
    # If there are no empty spots left, it's a draw
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while not check_winner(board) and not check_draw(board):
        print_board(board)

        # Input validation for row and column
        while True:
            try:
                row = int(
                    input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(
                    input(f"Enter column (0, 1, or 2) for player {player}: "))

                if row not in range(3) or col not in range(3):
                    print(
                        "Invalid input. Row and column must be between 0 and 2. Try again.")
                    continue

                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter numeric values for row and column.")

        # Update the board with the player's move
        board[row][col] = player

        # Switch player
        player = "O" if player == "X" else "X"

    print_board(board)

    if check_winner(board):
        print(f"Player {player} wins!")
    else:
        print("It's a draw!")


tic_tac_toe()
