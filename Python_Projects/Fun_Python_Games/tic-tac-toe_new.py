from typing import Final
from random import choice

# Set up the game settings
COUNT_OF_MARKERS_NEEDED_TO_WIN: Final[int] = 3
gamemode: str = ""

# Set up the board
BOARD_SIZE: Final[int] = 3
board: Final[list[list[str | None]]] = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Set up score and markers
Scores: Final[dict[str, int]] = {
    "Player": 0,
    "Opponent": 0
}

Markers: Final[dict[str, str]] = {
    "Player Marker": "X",
    "Opponent Marker": "O"
}

# Get gamemode (Another player or against a computer)
def get_gamemode() -> None:

    while True:
        global gamemode
        gamemode = input("Game mode selection [Player / Computer]: ").strip().lower()

        if gamemode in {"player", "computer"}:
            break
        else:
            print("Please enter player or computer as your input to choose the game mode.")

# Place human or player one or two marker on a row or column
def place_player_marker(marker: str) -> None:
    empty_spaces = get_empty_spaces()

    if not empty_spaces:
        return
    
    while True:
        row: str | int = input("Row: ")
        column: str | int = input("Column: ")

        if validate_player_input(row) and validate_player_input(column):
            row = int(row)
            column = int(column)

            if (row, column) in empty_spaces:
                board[row][column] = marker
                print_board()
                break
            else:
                print(f"There is already a marker on row {row}, column {column}.")

# Validate human or player one or two input for row and column for placing marker
def validate_player_input(player_input: str) -> bool:
    try:
        # Check if the user inputted a number and that it's between 0 and 2
        converted_player_input = int(player_input)

        if converted_player_input not in range(BOARD_SIZE):
            print(f"Out of range! The row / column must be between 0 and {BOARD_SIZE - 1}.")
            return False
        else:
            return True

    except ValueError:
        print(f"Invalid input: {player_input}")
        return False

# Place computer marker
def place_computer_marker() -> None:
    empty_spaces = get_empty_spaces()

    if not empty_spaces:
        return

    row, column = choice(tuple(empty_spaces))
    board[row][column] = Markers["Opponent Marker"]
    print_board()

# Get empty spaces to further validate player input
def get_empty_spaces() -> set[tuple[int, int]]:
    return {
        (row, column)
        for row in range(BOARD_SIZE)
        for column in range(BOARD_SIZE)
        if board[row][column] is None
    }

# Check for winner and tie (True for winner, False for tie and None for game is still going)
def check_for_winner_and_tie(marker: str) -> bool | None:

    # Check for rows
    print("rows")
    check_rows = all(marker == spot for row in board for spot in row)
    check_columns = all(marker == spot for column in zip(*board) for spot in column)
    check_diagonal = all(marker == board[i][i] for i in range(BOARD_SIZE))
    check_other_diagonal = all(marker == board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE))

    if any((check_rows, check_columns, check_diagonal, check_diagonal, check_other_diagonal)):
        print("Player One wins!" if marker == Markers["Player Marker"] else "Opponent wins!")
        update_scores(marker)
        return True

    # If no win combinations were True then check if the game is still on-going (None value)
    if any(spot == None for row in board for spot in row):
        print("Game is still on-going!")
        return None

    # No win combinations are hit and all spots are filled, it is a tie game!
    print("Tie game!")
    return False

# Update the scores
def update_scores(marker: str) -> None:
    if marker == Markers["Player Marker"]:
        Scores["Player"] += 1
    else:
        Scores["Opponent"] += 1

# Print the board
def print_board() -> None:
    print("  ", end="")

    for i in range(BOARD_SIZE):
        print(i, end=" ")
    print()

    for i, row in enumerate(board):
        print(i, end=" ")

        for element in row:
            print(element if element is not None else "-", end=" ")
            
        print()

    print()

# Clean up the game by swapping markers (not the scores) and setting everything to None on the board
def clean_up_game() -> None:
    Markers["Player Marker"], Markers["Opponent Marker"] = Markers["Opponent Marker"], Markers["Player Marker"]

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            board[i][j] = None

# Ask the player to play again
def prompt_play_again() -> bool:
    while True:
        play_again: str = input("Want to play again? [Y / N]: ").strip().lower()

        if play_again in {"yes", "y"}:
            return True
        elif play_again in {"no", "n"}:
            return False
        else:
            print(f"Couldn't recognize: \'{play_again}\' as a valid input.")

# main function to play the game
def main() -> None:
    get_gamemode()
    print_board()

    while True:
        print("Player One's turn!")
        place_player_marker(Markers["Player Marker"])

        if check_for_winner_and_tie(Markers["Player Marker"]) is not None:
            break

        if gamemode == "player":
            print("Player Two's turn!")
            place_player_marker(Markers["Opponent Marker"])
        else:
            print("Computer's turn!")
            place_computer_marker()

        if check_for_winner_and_tie(Markers["Opponent Marker"]) is not None:
            break

    if prompt_play_again():
        clean_up_game()
        main()
    else:
        if Scores["Player"] > Scores["Opponent"]:
            print(f"Player One wins: {Scores["Player"]} - {Scores["Opponent"]}")

        elif Scores["Player"] < Scores["Opponent"]:
                print(f"Opponent wins: {Scores["Opponent"]} - {Scores["Player"]}")
        else:
            print("Tie game! No one won.")

print("Welcome to Tic-Tac-Toe!")
print("Your goal of the game is to get three of your markers in a row in any direction to win.")
print("It could be in a row, horizontally, in a column, vertically, or in a diagonal like a criss-cross, diagonally.")

main()