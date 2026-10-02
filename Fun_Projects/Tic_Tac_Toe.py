from random import choice
from typing import Final
from enum import Enum

BOARD_SIZE: Final[int] = 3
board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
game_mode = ""

markers: dict[str, str] = {
    "player": "X",
    "opponent": "O"
}

scores: dict[str, int] = {
    "player": 0,
    "opponent": 0
}

# I completely forgot about Enums until ChatGPT suggested Enums to give my win conditions better namings and meanings
class Game_Status(Enum):
    WIN = 1
    ON_GOING = 0
    TIE = -1

def get_player_input() -> tuple[int, int]:

    """
    Retrieve player's choice for row and column and return those values
    If the player's input validation failed then it would loop back to inputting Row and Column until the player entered a number input
    If their input is valid then convert the row and column variables to integers and return both of them (tuples of values)
    """

    while True:
        row = input("Row: ")
        column = input("Column: ")

        if validate_player_input(row) and validate_player_input(column):
            return int(row), int(column)
        else:
            print(f"Please enter a valid range from 0 to {BOARD_SIZE - 1}.")

def validate_player_input(player_input: str) -> bool:

    """
    Validate player's input to make sure that nothing can break the code
    Return True if the player's input was able to be converted to an int and is in the range of 0 - 2 (for indexing the board)
    Return False if there is an error or that the player's input is not in the range
    """

    try:
        return int(player_input) in range(BOARD_SIZE)
    except ValueError:
        return False

def place_marker(marker: str) -> None:

    """
    After retrieving and validating player's input for row and column
    Check if the row and column located on the board is occupied
    If it is occupied already then print a message, keep looping back until the player enters in a valid input
    However if it is not occupied then keep getting place the marker and break out of the loop
    """

    while True:
        row, column = get_player_input()

        if board[row][column] is not None:
            print(f"Row: {row}, Column: {column} has already been occupied by: {board[row][column]}")
        else:
            board[row][column] = marker
            break

def check_for_win(target_marker: str) -> Game_Status:

    """
    Check if any of the markers won or not
    Make variables for checking win combinations for rows, columns, the main diagonal, and the other diagonal
    If any of the variables evaluate to True then print who won using the marker, update the winner's score, and return Game Status Win
    If there are no win conditions met then check if there are any empty spaces, if there are then the game is on-going so return Game Status On Going
    However, if all fails, then return Game Status Tie because there are no win conditions met but also no more empty spaces left
    """

    check_rows = any(
        all(spot == target_marker for spot in row)
        for row in board
    )

    check_columns = any(
        all(spot == target_marker for spot in row)
        for row in zip(*board)
    )

    check_main_diagonal = all(board[i][i] == target_marker for i in range(BOARD_SIZE))

    check_other_diagonal = all(board[i][BOARD_SIZE - 1 - i] == target_marker for i in range(BOARD_SIZE))

    if any((check_rows, check_columns, check_main_diagonal, check_other_diagonal)):
        if game_mode == "player":
            if target_marker == markers["player"]:
                print("Player 1 has won!")
                scores["player"] += 1
            else:
                print("Player 2 has won!")
                scores["opponent"] += 1
        else:
            if target_marker == markers["player"]:
                print("Human has won!")
                scores["player"] += 1
            else:
                print("Computer has won!")
                scores["opponent"] += 1

        return Game_Status.WIN

    empty_spaces = get_empty_spaces()

    if empty_spaces:
        print("On-going game!")
        return Game_Status.ON_GOING

    print("Tie game!")
    return Game_Status.TIE

def get_empty_spaces() -> tuple[tuple[int, int], ...]:

    """
    Return empty spaces on the board
    """

    return tuple(
        (row, column)
        for row in range(BOARD_SIZE)
        for column in range(BOARD_SIZE)
        if board[row][column] is None
    )

def computer_random_choice() -> None:

    """
    The computer places its marker on a random, empty spot on the board
    """

    empty_spaces = get_empty_spaces()

    if not empty_spaces:
        return

    row, column = choice(empty_spaces)
    board[row][column] = markers["opponent"]

def get_game_mode() -> None:

    """
    Get the player's choice for the game mode
    """

    global game_mode
    
    while True:
        game_mode = input("Select Game Mode [Player / Computer]: ").strip().lower()

        if game_mode in {"player", "computer"}:
            break
        else:
            print("Please enter player or computer to select the game mode.")

def clean_up_game() -> None:

    """
    Swap the markers after every game and reset the board by changing all values back to None
    """

    markers["player"], markers["opponent"] = markers["opponent"], markers["player"]

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            board[row][column] = None

def display_final_winner() -> None:

    """
    Use many if statements to just print the appropriate winning message (I'm sorry okay so many I know there is A LOT OF if statements 😭)
    """

    print(f"Final Score: {scores['player']} - {scores['opponent']}")

    if game_mode == "player":
        if scores["player"] > scores["opponent"]:
            print("Player 1 has won the entire game!")
        elif scores["player"] < scores["opponent"]:
            print("Player 2 has won the entire game!")
        else:
            print("Wow, it's a tie game. No one wins!")
    else:
        if scores["player"] > scores["opponent"]:
            print("Player has won the entire game!")
        elif scores["player"] < scores["opponent"]:
            print("Computer has won the entire game!")
        else:
            print("Wow, it's a tie game. No one wins!")

def print_board() -> None:

    """
    Print the board except that it is printed "prettier" with separators in between the markers and rows
    I learned how to format the board with ChatGPT (Using Artificial Intelligence to ACTUALLY learn and not simply copy and pasting down code)
    """

    for row_index, row in enumerate(board):
        for column_index, spot in enumerate(row):
            print(spot if spot is not None else "-", end="")

            if column_index < (BOARD_SIZE - 1):
                print(" | ", end="")
        print()

        if row_index < (BOARD_SIZE - 1):
            print("--+---+--")

def prompt_play_again() -> bool:

    """
    Prompt the player to play again
    If they want to play again then return True
    If not, return False
    If the player did not enter in a valid input then print a message and loop back until the player enters in a valid input
    """

    while True:
        play_again = input("Want to play again [Y / N]: ").strip().lower()

        if play_again in {"y", "ye", "yes"}:
            return True
        elif play_again in {"n", "no"}:
            return False
        else:
            print("Please enter yes or no to play again or not.")

def play_game() -> None:

    """
    Print the board to see what the board looks like at first
    If game mode is player or computer then run the code below it (Inner while loops to keep the player and other player or computer to keep placing markers until a win or tie)
    After every game, prompt the player or players if they want to play again or not
    If yes, then clean up the game and loop back to play the game (Outer while loop)
    If not then display the final winner out of every game the player or players have played and break
    """

    while True:

        print_board()

        if game_mode == "player":

            while True:
                print("Player 1's turn!")
                place_marker(markers["player"])
                print_board()

                if check_for_win(markers["player"]) is not Game_Status.ON_GOING:
                    break

                print("Player 2's turn!")
                place_marker(markers["opponent"])
                print_board()

                if check_for_win(markers["opponent"]) is not Game_Status.ON_GOING:
                    break
        else:
            while True:
                print("Your turn!")
                place_marker(markers["player"])
                print_board()

                if check_for_win(markers["player"]) is not Game_Status.ON_GOING:
                    break

                print("Computer's turn!")
                computer_random_choice()
                print_board()

                if check_for_win(markers["opponent"]) is not Game_Status.ON_GOING:
                    break

        if prompt_play_again():
            clean_up_game()
        else:
            display_final_winner()
            break

def main() -> None:

    """
    Main function with everything in it compressed into one main function
    """

    print("Welcome to Tic-Tac-Toe!")
    print("Your game is to get 3 in a row, column, or diagonal to win!")

    get_game_mode()
    play_game()

main()