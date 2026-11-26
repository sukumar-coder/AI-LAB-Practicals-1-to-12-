
import math

# Initialize Board
board = [" "] * 9

HUMAN = "X"
AI = "O"


# Display Board
def display_board():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print()


# Check Winner
def check_winner():
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


# Check Draw
def is_draw():
    return " " not in board and check_winner() is None


# Minimax with Alpha-Beta Pruning
def minimax(is_maximizing, alpha, beta):
    winner = check_winner()

    if winner == AI:
        return 10

    if winner == HUMAN:
        return -10

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = AI

                score = minimax(False, alpha, beta)

                board[i] = " "
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                if beta <= alpha:
                    break

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN

                score = minimax(True, alpha, beta)

                board[i] = " "
                best_score = min(best_score, score)
                beta = min(beta, best_score)

                if beta <= alpha:
                    break

        return best_score


# Find Best Move for AI
def best_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = AI

            score = minimax(False, -math.inf, math.inf)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# Main Game
def play_game():
    print("TIC TAC TOE - AI GAME")
    print("You are X | AI is O")
    print("Enter position from 1 to 9")

    display_board()

    while True:
        # Human Turn
        try:
            position = int(input("Enter your move (1-9): ")) - 1

            if position < 0 or position >= 9 or board[position] != " ":
                print("Invalid move! Try again.")
                continue

            board[position] = HUMAN

        except ValueError:
            print("Please enter a number.")
            continue

        display_board()

        if check_winner() == HUMAN:
            print("You Win!")
            break

        if is_draw():
            print("Game Draw!")
            break

        # AI Turn
        print("AI is thinking...")

        move = best_move()
        board[move] = AI

        display_board()

        if check_winner() == AI:
            print("AI Wins!")
            break

        if is_draw():
            print("Game Draw!")
            break


# Start Game
play_game()
