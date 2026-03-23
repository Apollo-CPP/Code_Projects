import random
import typing

Max_Ship_Chance: typing.Final[int] = 100
Random_Ship_Chance: typing.Final[int] = 50

Game_Configuration: dict[str, int] = {
    "Minimum Rows": 4,
    "Maximum Rows": 9,
    "Max Ships": 8,
}

class Board:
    __Ship_Locations: set[tuple[int, int]] = set() # I set this to a private variable because it's literally the answers

    def __init__(self, Amount_of_Rows: int, Amount_of_Columns: int):
        self.Ship_Board: list[list[bool | None]] = [[None for _ in range(Amount_of_Columns)] for _ in range(Amount_of_Rows)] # Sets up new board with x elements (columns) and y rows
        self.User_Guessed_Locations: list[list[bool | None]] = [[None for _ in range(Amount_of_Columns)] for _ in range(Amount_of_Rows)] # Same thing but just used to check what coordinates the user already guessed
        # Implemented to prevent double guessing and wasting a turn

    @classmethod
    def Generate_Ships(cls, Ship_Board: list[list[bool | None]]) -> None:
        for i, Ship_Row in enumerate(cls.__Ship_Locations):
            for j in range(len(Ship_Row)):

                Random_Chance: int = random.randint(0, Max_Ship_Chance) # Random Number from 0 to 100

                if Random_Chance <= Random_Ship_Chance: # If it is basically less than or equal to 50 (1/2 chance of a ship spawning but a high range of numbers for better probability)
                    cls.__Ship_Locations.add((i, j))
                    print(f"Row: {i}, Column: {j}") # Debugging Purposes

    @classmethod
    def Get_Ship_Locations(cls) -> set[tuple[int, int]]: # Simple Get Method for returning the private variable (Ship Locations)
        return cls.__Ship_Locations
    
    def Update_Ship_Locations(self) -> None: # Returns the indices (coordinates) of where the ships are
        self.__Ship_Locations = {
            (Row_Index, Column_Index)

            for Row_Index, Ship_Row in enumerate(self.Ship_Board)
            for Column_Index, value in enumerate(Ship_Row)
            if value is True
        }

def Display_Introduction_and_Instructions() -> None:
    print("Welcome to BattleShip! (Python Version)")
    print("Your goal here is to destroy all of the enemy ships before they destroy you.")
    print("There will be 8 ships that will be hidden on your side and your opponent's side")

    """
    I don't know how to make it so that the player can know where their ships are and the other player (or computer) knows where their ships also are without them cheating because the game is ran on one device
    So, I had  to put that statement there on line 48
    """

    print("You will be asked to input the Row and Column that you want to fire at")
    print("If you hit a ship, congratulations, that's -1 ship for the enemy and a hit for you. However if you miss, just hope that the opponent doesn't destroy one of your ships.")
    print("There are some rules for inputting as well and I have added safe guards to ensure that you don't somehow crash the entire program")

    print("----- RULES FOR INPUTTING -----")
    print("1. Your input has to be an INTEGER, or a WHOLE NUMBER. No spaces, special characters, or literally just an empty input.")
    print("2. Your input needs to be within the range of 0 - (Ship Row or Ship Column depending on which input you're putting in for) MINUS 1 because tables start at the index of 0 instead of 1")

    print("----- SHIP BOARD KEYS -----")
    print("~ = Unknown (Possible Ship).")
    print("X = Hit, nice you hit a ship!")
    print("O = Miss, better luck next time.")

    print("----- SPECIAL INPUTS -----")
    print("MENU - Opens up the Menu")
    print("QUIT (Needs to be in the Menu) - Stop and Exit the game and confirm your choice")
    print("RESTART (Needs to be in the Menu) - Restarts the game and also requires confirmation")
    print("CONTINUE (Needs to be in the Menu) - Simply continues the game")
    print()

    print("Objective: Destroy your enemy ships before they destroy you. Good luck.")
    print("----------------------------------------")

def Get_Player_Input():

    while True:

        while True:

            Input_Row = input("Row: ")

def Validate_Player_Input(Player_Input: str) -> bool:
    try:
        Converted_Player_Input = int(Player_Input)