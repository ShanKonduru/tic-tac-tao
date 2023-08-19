import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_cells.append((row, col))
    return empty_cells

def computer_move(board, level, computer_player, human_player):
    if level == "basic":
        return random.choice(get_empty_cells(board))
    elif level == "medium":
        # Add your medium level AI logic here (e.g., check for winning moves, block human winning moves)
        pass
    elif level == "advanced":
        # Add your advanced level AI logic here (e.g., implement Minimax algorithm)
        pass

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    modes = {
        "1": ("Person vs Person", [0, 1]),
        "2": ("Person vs Computer", [0, 2]),
    }

    print("Welcome to Tic-Tac-Toe!")
    print("Select mode:")
    for key, value in modes.items():
        print(f"{key}: {value[0]}")
    mode_choice = input()

    if mode_choice in modes:
        mode = modes[mode_choice]
        print(f"Selected mode: {mode[0]}")

        if mode[1][1] == 2:
            levels = ["basic", "medium", "advanced"]
            print("Select computer level:")
            for i, level in enumerate(levels):
                print(f"{i+1}: {level}")
            level_choice = int(input())
            computer_level = levels[level_choice - 1]
            print(f"Selected computer level: {computer_level}")

        current_player = players[0]
        while True:
            print_board(board)
            print(f"Player {current_player}'s turn")

            if mode[1][current_player == 'O']:
                row, col = map(int, input("Enter row and column (space-separated): ").split())
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    board[row][col] = current_player
                else:
                    print("Invalid move. Try again.")
                    continue
            else:
                row, col = computer_move(board, computer_level, 'O', 'X')
                board[row][col] = 'X'

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = players[1] if current_player == players[0] else players[0]

    else:
        print("Invalid mode choice. Exiting.")

if __name__ == "__main__":
    main()
