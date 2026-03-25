import random

Game_Configuration: dict[str, int] = {
    "Max_Ship_Chance": 100,
    "Random_Ship_Chance": 50,
    
    "Minimum Rows": 4,
    "Maximum Rows": 9,
    "Max Ships": 10
}

Game_State: dict[str, int] = {
    "Current Turn": 1, # Just so you don't get confused, 1 is for Player One and 2 is for Player Two or Computer (I put this to see who opened the menu in case if a player or computer wants to do an action like a nuke)

    "Player One Hits": 0,
    "Player Two Hits": 0,

    "Player One Total Hits": 0,
    "Player Two Total Hits": 0,

    "Player One Score": 0,
    "Player Two Score": 0
}

class Board:
    def __init__(self, Amount_of_Rows: int, Amount_of_Columns: int):
        self.__Ship_Locations: set[tuple[int, int]] = set() # I set this to a private variable because it's literally the answers
        # self.Ship_Board: list[list[bool | None]] = [[None for _ in range(Amount_of_Columns)] for _ in range(Amount_of_Rows)] # Sets up new board with x elements (columns) and y rows
        # Realized I didn't even need the Ship_Board list at all. Rarely even used.
        self.Guessed_Coordinates: dict[tuple[int, int], bool] = dict() # Created an empty dictionary with tuples holding 2 integers (coordinates) as keys and booleans as values
        # Implemented to prevent double guessing and wasting a turn but also for efficiently retrieving the Board symbols (~ for unknown, X for hit, and O for miss)
        self.Number_of_Rows: int = Amount_of_Rows
        self.Number_of_Columns: int = Amount_of_Columns

    def Generate_Ships(self) -> None:
        for i, Ship_Row in enumerate(self.__Ship_Locations):
            for j in range(len(Ship_Row)):

                Random_Chance: int = random.randint(0, Game_Configuration["Max_Ship_Chance"]) # Random Number from 0 to 100

                if Random_Chance <= Game_Configuration["Random_Ship_Chance"]: # If it is basically less than or equal to 50 (1/2 chance of a ship spawning but a high range of numbers for better probability)
                    self.__Ship_Locations.add((i, j))
                    print(f"Row: {i}, Column: {j}") # Debugging Purposes

        if len(self.__Ship_Locations) <= 0:
            print("Wow... You are unlucky yet lucky. The ship generator function has generated ZERO ships.")
            print("The system will now just exit the game and prompt you if you want to play the game.")

    def Get_Ship_Locations(self) -> set[tuple[int, int]]: # Simple Get Method for returning the private variable (Ship Locations)
        return self.__Ship_Locations
    
    # def Update_Ship_Locations(self) -> None: # Returns the indices (coordinates) of where the ships are
    #     self.__Ship_Locations = {
    #         (Row_Index, Column_Index)

    #         for Row_Index, Ship_Row in enumerate(self.Ship_Board)
    #         for Column_Index, value in enumerate(Ship_Row)
    #         if value is True
    #     }
    # Originally created this function to keep track of all ships located in real time but thought it over and just why not just show all ship locations instead?

    def Retrieve_Board_Symbol(self, Row_Index: int, Column_Index: int) -> str:
        Coordinates: tuple[int, int] = (Row_Index, Column_Index)

        if not self.Guessed_Coordinates.get((Row_Index, Column_Index)):
            return "~"
        
        if Coordinates not in self.__Ship_Locations:
            return "O"
        else:
            return "X"
        
    def Print_Ship_Board(self) -> None:
        # print(*(Column_Number for Column_Number in range(len(self.Ship_Board[0]))), sep=" ") # AI Usage No. 2 - I was confused on how to print the elements using a comprehension but while also separating them with a space
        # Apparently all I had to do was just to unpackage it using the * sign
        # Later thought about it and changed it to the version below for readability

        for Column in range(self.Number_of_Columns):
            print(Column, end=" ")
        print()

        for i in range(self.Number_of_Rows):
            for j in range(self.Number_of_Columns):
                print(self.Retrieve_Board_Symbol(i, j))
            print()

    def Generate_Random_Coordinate(self) -> tuple[int, int]: # Hey! This is only used when the Game mode is computer so that the computer can generate a random coordinate
        Empty_Spots = {
            (Row_Index, Column_Index)

            for Row_Index in range(self.Number_of_Rows)
            for Column_Index in range(Row_Index)
            if (Row_Index, Column_Index) not in self.Guessed_Coordinates
        }

        Random_Coordinate = random.choice(tuple(Empty_Spots)) # AI usage No. 3 - I was COMPLETELY stupid. All I had to do was covert the set to a list or a tuple. bruh.
        return Random_Coordinate


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
    print("NUKE (Needs to be in Menu and requires 5 ships destroyed) - Destroy everything in a 3 mile radius of the coordinate (including the coordinate).", end="\n")

    print("Objective: Destroy your enemy ships before they destroy you. Good luck.")
    print("----------------------------------------")

def Get_Player_Input(Ship_Board: Board) -> tuple[int, int] | None:

    while True:
        Row = input("Choose a Row: ")

        if Row.strip().lower() == "menu":
            Menu_Handler(Ship_Board)
            return

        if Validate_Player_Input(Row, Ship_Board.Number_of_Rows) == True:
            break

    while True:
        Column = input("Choose a Column: ")

        if Column.strip().lower() == "menu":
            Menu_Handler(Ship_Board)
            return

        if Validate_Player_Input(Column, Ship_Board.Number_of_Columns) == True:
            break

    return (int(Row), int(Column))

def Validate_Player_Input(Player_Input: str, Max_Limit: int): # AI usage No. 1, Max_Limit parameter suggestion.
    # The problem was that if the amount of rows and columns were different then I can't tell what the maximum number was that the input could take
    # I could've just added a parameter of Max_Limit and was ashamed as this was a simple and easy solution
    try:
        Converted_Player_Input = int(Player_Input)
        
        if (0 <= Converted_Player_Input <= Max_Limit) == False:
            print("Your input for rows or columns is out of bounds!")
            return False
        else:
            return True

    except ValueError:
        print("There are some illegal characters in your input. You can't have any special characters, spaces, or just an empty input.")
        return False
    
def Get_Gamemode() -> str:
    while True:
        Game_mode = input("Who do you want to play with? A player or a computer? [Player / Computer]: ").strip().lower()

        if Game_mode != "player" and Game_mode != "computer":
            print("You need to enter either player or computer for your game mode!")
        else:
            return Game_mode
        
def Menu_Handler(Ship_Board: Board) -> None:
    print("----- Game Menu -----")

    print("> Quit")
    print("> Restart")
    print("> Continue")

    if Game_State["Current Turn"] == 1 and Game_State["Player One Hits"] % 5 == 0:
        print("> Nuke (Oooh, I wonder what this does)")
    if Game_State["Current Turn"] == 2 and Game_State["Player Two Hits"] % 5 == 0:
        print("> Nuke (Oooh, I wonder what this does)")