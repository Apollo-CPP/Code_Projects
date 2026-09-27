from random import choice
from typing import Final

BOARD_SIZE: Final[int] = 3
board: list[list[str | None]] = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

class Game:
    def __init__(self):
        self.scores: dict[str, int] = {
            "player": 0,
            "opponent": 0
        }

        self.markers: dict[str, str] = {
            "player": "X",
            "opponent": "O"
        }

        self.gamemode: str | None = None

    def swap_markers(self) -> None:
        self.markers["player"], self.markers["opponent"] = self.markers["opponent"], self.markers["player"]

    def get_player_input(self) -> tuple[int, int]:

        while True:
            row = input("Row: ")
            column = input("Column: ")

            if self.validate_player_input(row) and self.validate_player_input(column):
                return int(row), int(column)
            
    def validate_player_input(self, player_input: str) -> bool:

        try:
            return int(player_input) in range(BOARD_SIZE)
        
        except ValueError:
            print("It's either that you put an invalid input or your numbers are just out of range.")
            return False
        
    def place_marker(self, marker: str) -> None:
        while True:
            row, column = self.get_player_input()

            if board[row][column] is None:
                board[row][column] = marker
                break
            else:
                print(f"The spot is already occupied by {board[row][column]}!")
            

    def check_for_win(self, target_marker: str) -> bool | None:

        check_rows: bool = any(
            all(spot == target_marker for spot in row)
            for row in board
        )

        
        check_columns: bool = any(
            all(spot == target_marker for spot in column)
            for column in zip(*board))
        
        check_main_diagonal: bool = all(
            board[i][i] == target_marker
            for i in range(BOARD_SIZE))
        
        check_other_diagonal: bool = all(
            board[i][BOARD_SIZE - 1 - i] == target_marker
            for i in range(BOARD_SIZE)
        )

        if any((check_rows, check_columns, check_main_diagonal, check_other_diagonal)):

            if target_marker == self.markers["player"]:
                print("Player has won!")
                self.scores["player"] += 1
            else:
                if self.gamemode == "player":
                    print("Player Two has won!")
                else:
                    print("Computer has won!")

                self.scores["opponent"] += 1 

            return True

        check_for_ongoing: bool = any(spot is None for row in board for spot in row)
        
        if check_for_ongoing:
            print("Ongoing game!")
            return None

        print("Tie game!")
        return False

    def prompt_play_again(self) -> bool:

        while True:
            play_again_choice = input("Do you want to play again? [Y / N]: ").strip().lower()

            if play_again_choice in {"y", "ye", "yes"}:
                return True

            elif play_again_choice in {"n", "no"}:
                return False
            print("Please enter yes or no")
            
    def get_gamemode(self) -> None:

        while True:
            self.gamemode = input("Who would you like to play against? A computer or another person? [Player / Computer]: ").strip().lower()

            if self.gamemode in {"player", "computer"}:
                break

    def clear_board(self) -> None:
        for row_index in range(BOARD_SIZE):
            for column_index in range(BOARD_SIZE):
                board[row_index][column_index] = None

    def announce_final_winner(self) -> None:
        print(f"Final Scores: {self.scores["player"]} - {self.scores["opponent"]}")

        if self.scores["player"] > self.scores["opponent"]:

            if self.gamemode == "player":
                print("You win the entire game!")
            else:
                print("Player 1 won the entire game!")

        elif self.scores["player"] < self.scores["opponent"]:
            if self.gamemode == "player":
                print("Player 2 won the entire game!")
            else:
                print("Computer has won the entire game!")
        else:
            print("Both scores are tied. No one won.")


class Computer:

    @staticmethod
    def get_empty_spaces() -> set[tuple[int, int]]:

        return {
            (row_index, column_index)
            for row_index in range(BOARD_SIZE)
            for column_index in range(BOARD_SIZE)
            if board[row_index][column_index] is None
        }

    def place_marker_at_random_spot(self, marker: str) -> None:

        empty_spaces = self.get_empty_spaces()

        if not empty_spaces:
            return

        row, column = choice(tuple(empty_spaces))
        board[row][column] = marker

def play_game() -> None:        
    Server.get_gamemode()
    print_board()

    if Server.gamemode == "player":

        while True:
            print("Player's turn!")
            Server.place_marker(Server.markers["player"])
            print_board()

            if Server.check_for_win(Server.markers["player"]) is not None:
                break

            print("Player Two's turn!")
            Server.place_marker(Server.markers["opponent"])
            print_board()

            if Server.check_for_win(Server.markers["opponent"]) is not None:
                break

    else:
        while True:
            print("Your turn!")
            Server.place_marker(Server.markers["player"])
            print_board()

            if Server.check_for_win(Server.markers["player"]) is not None:
                break

            print("Computer's turn!")
            Bot.place_marker_at_random_spot(Server.markers["opponent"])
            print_board()

            if Server.check_for_win(Server.markers["opponent"]) is not None:
                break

def main() -> None:

    print("Welcome to Tic-Tac-Toe!")
    print("Your goal is to get 3 in a row, column, or diagonal to win!")

    while True:
        play_game()

        if Server.prompt_play_again():
            Server.swap_markers()
            Server.clear_board()
        else:
            Server.announce_final_winner()
            break

def print_board() -> None:
    print()

    for row_index, row in enumerate(board):
        for column_index, spot in enumerate(row):
            print(spot if spot is not None else "-", end="")

            if column_index < (BOARD_SIZE - 1):
                print(" | ", end="")
        print()

        if row_index < (BOARD_SIZE - 1):
            print("--+---+---")

Server = Game()
Bot = Computer()
main()