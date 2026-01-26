import random

# Create and display the board
def create_board():
    return [" " for _ in range(9)]

def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Game status checks
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],    # rows
        [0,3,6], [1,4,7], [2,5,8],    # columns
        [0,4,8], [2,4,6]              # diagonals
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_tie(board):
    return " " not in board

# Simple AI agent logic
def ai_move(board):
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
     
    # Win if possible
    for move in available_moves:
        temp_board = board.copy()
        temp_board[move] = "O"
        if check_winner(temp_board, "O"):
            return move

    # block the player
    for move in available_moves:
        temp_board = board.copy()
        temp_board[move] = "X"
        if check_winner(temp_board, "X"):
            return move

    # choose random move
    return random.choice(available_moves)

# Main game loop
def play_game():
    board = create_board()
    display_board(board)

    while True:
        # Player turn
        try:
            player_move = int(input("Choose a position (0-8): "))
            if player_move < 0 or player_move > 8:
                print("Please choose a number between 0 and 8.")
                continue
            if board[player_move] != " ":
                print("That position is already taken.")
                continue
            board[player_move] = "X"
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")
            continue

        display_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break

        if check_tie(board):
            print("It's a tie!")
            break

        # AI turn
        ai_choice = ai_move(board)
        board[ai_choice] = "O"
        print(f"AI chose position {ai_choice}")

        display_board(board)

        if check_winner(board, "O"):
            print("AI wins!")
            break

        if check_tie(board):
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_game()
