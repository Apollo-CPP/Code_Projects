# My code is EXTREMELY messy. There are many while loops everywhere
# There are also repeated code for validation
# Also MANY if statements, especially in the Retrieve_Board_Symbol() function, where there are nested if statements
# I apologize in advance if you try to read my code

import random

Game_Configuration: dict[str, int] = {    
    "Minimum Rows and Columns": 5,
    "Maximum Rows and Columns": 10,
    "Max Ships": 10
}

Game_State: dict[str, int] = {
    "Current Turn": 1, # Shows the current turn of the game. 1 for Player One and 2 for Player Two or Computer

    "Player One Score": 0,
    "Player Two Score": 0
}

class Board:
    def __init__(self, Amount_of_Rows: int, Amount_of_Columns: int, Player_Name: str):
        self.__Ship_Locations: set[tuple[int, int]] = set() # I set this to a private variable because it's literally the answers
        # self.Ship_Board: list[list[bool | None]] = [[None for _ in range(Amount_of_Columns)] for _ in range(Amount_of_Rows)] # Sets up new board with x elements (columns) and y rows
        # Realized I didn't even need the Ship_Board list at all. Rarely even used.
        self.Guessed_Coordinates: dict[tuple[int, int], bool] = dict() # Reverted it back to a dictionary for more efficient checking for the function Retrieve_Board_Symbol()
        # Implemented to prevent double guessing and wasting a turn but also for efficiently retrieving the Board symbols (~ for unknown, X for hit, and O for miss)
        self.Number_of_Rows: int = Amount_of_Rows
        self.Number_of_Columns: int = Amount_of_Columns
        self.Numbers_of_Ships: int = 0
        self.Player_Name_PlaceHolder = Player_Name # Used for distinguishing the different boards when printed so the players do not get confused on which boards are theirs

    def Place_Ships(self) -> None:
        while self.Numbers_of_Ships < Game_Configuration["Max Ships"]:

            while True:
                Ship_Row = input(f"Ship {self.Numbers_of_Ships + 1} Row: ").strip() # I have to put a + 1 because you can't start with Ship 0.

                if Validate_Player_Input(Ship_Row, 0, self.Number_of_Rows) == True: # Check if the input is less than or greater than 0 and less than 10
                    break

            while True:
                Ship_Column = input(f"Ship {self.Numbers_of_Ships + 1} Column: ").strip()

                if Validate_Player_Input(Ship_Column, 0, self.Number_of_Columns) == True:
                    break

            if (int(Ship_Row), int(Ship_Column)) in self.__Ship_Locations:
                print(f"Couldn't place Ship {self.Numbers_of_Ships + 1} in Row {Ship_Row} and Column {Ship_Column} because there is already a ship placed there!")
                continue

            self.__Ship_Locations.add((int(Ship_Row), int(Ship_Column)))
            self.Numbers_of_Ships += 1


    def Generate_Ships(self) -> None: # Updated - This is now for the computer only. There's a new function that will allow players to place their ships
        All_Coordinates = {
            (Row_Index, Column_Index)

            for Row_Index in range(self.Number_of_Rows)
            for Column_Index in range(self.Number_of_Columns)
        }

        self.__Ship_Locations = set(random.sample(tuple(All_Coordinates), Game_Configuration["Max Ships"])) # AI Usage No. 6. I literally forgot about the random.sample() function. I could've replaced my entire RNG Ship Generation with that one line alone.
        # random.sample() is basically random.choice() but it returns UNIQUE choices with the amount of times you want. (How did I forget about this function??)
        self.Numbers_of_Ships = len(self.__Ship_Locations)

        for Coordinate in self.__Ship_Locations:
            print(f"Row: {Coordinate[0]}, Column: {Coordinate[1]}") # Debugging Purposes

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

    def Retrieve_Board_Symbol(self, Coordinates: tuple[int, int], Enemy_Guessed_Coordinates: dict[tuple[int, int], bool], Show_Answer: bool) -> str:
        Check_If_Enemy_Guessed_The_Coordinates = Enemy_Guessed_Coordinates.get(Coordinates)

        if Show_Answer == True:

            if Check_If_Enemy_Guessed_The_Coordinates == None: # The opponent did not guess the coordinates
                return "!" if (Coordinates in self.__Ship_Locations) == True else "~" # Return "!" if the Coordinates was a ship, return "~" if it was not a ship
            else: # The opponent did guess the coordinates
                return "X" if Check_If_Enemy_Guessed_The_Coordinates == True else "O" # Return "X" if the Coordinates was a ship, return "O" if it was not a ship
            
        else:
            if Check_If_Enemy_Guessed_The_Coordinates == None: # The opponent did not guess the coordinates so just return "~"
                return "~"
            else: # The opponent did guess the coordinates
                return "X" if Check_If_Enemy_Guessed_The_Coordinates == True else "O" # Return "X" if it was a ship, return "O" if it was not a ship

    def Print_Ship_Board(self, Enemy_Guessed_Coordinates: dict[tuple[int, int], bool], Show_Answer: bool) -> None:
        # print(*(Column_Number for Column_Number in range(len(self.Ship_Board[0]))), sep=" ") # AI Usage No. 2 - I was confused on how to print the elements using a comprehension but while also separating them with a space
        # Apparently all I had to do was just to unpackage it using the * sign
        # Later thought about it and changed it to the version below for readability

        print(f"----- {self.Player_Name_PlaceHolder}'s Board -----") # Place Holder name so that when ship boards are printed, the players will not get confused
        print("  ", end="") # Formatting purposes
        for Column in range(self.Number_of_Columns):
            print(f"{Column} ", end="") # Space in between for formatting purposes
        print()

        for i in range(self.Number_of_Rows):
            print(i, end=" ") # Space for formatting purposes

            for j in range(self.Number_of_Columns):
                print(self.Retrieve_Board_Symbol((i, j), Enemy_Guessed_Coordinates, Show_Answer), end=" ")
            print()

    def Computer_Self_Play(self, Player_Board: Board) -> None: # Hey! This is only used when the Game mode is computer so that the computer can generate a random coordinate
        Empty_Spots = {
            (Row_Index, Column_Index)

            for Row_Index in range(self.Number_of_Rows)
            for Column_Index in range(self.Number_of_Columns)
            if (Row_Index, Column_Index) not in self.Guessed_Coordinates
        }

        if not Empty_Spots:
            return

        Random_Coordinate = random.choice(tuple(Empty_Spots)) # AI usage No. 3 - I was COMPLETELY stupid. All I had to do was covert the set to a list or a tuple. bruh.
        
        if Random_Coordinate not in Player_Board.Get_Ship_Locations():
            print(f"Computer has chosen Row: {Random_Coordinate[0]} and Column: {Random_Coordinate[1]}. Computer has missed.")
            self.Guessed_Coordinates.update({Random_Coordinate: False})
        else:
            print(f"Computer has chosen Row: {Random_Coordinate[0]} and Column: {Random_Coordinate[1]}. Computer has hit a ship!")
            self.Guessed_Coordinates.update({Random_Coordinate: True})


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
    print("2. Your input needs to be within the range of 0 - (Ship Row or Ship Column depending on which input you're putting in for) MINUS 1 because tables start at the index of 0 instead of 1.")

    print("----- SHIP BOARD KEYS -----")
    print("~ = Unknown (Possible Ship).")
    print("X = Hit, nice you hit a ship!")
    print("O = Miss, better luck next time.")
    print("! (Only shown at the end of the game or by quitting or restarting) = Revealed Ship")

    print("----- SPECIAL INPUTS -----")
    print("MENU - Opens up the Menu")
    print("QUIT (Needs to be in the Menu) - Stop and Exit the game and confirm your choice")
    print("RESTART (Needs to be in the Menu) - Restarts the game and also requires confirmation")
    print("CONTINUE (Needs to be in the Menu) - Simply continues the game")
    print("NUKE (Needs to be in Menu and requires 5 ships destroyed) - Destroy everything in a 3 mile radius of the coordinate (including the coordinate).", end="\n")

    print("Objective: Destroy your enemy ships before they destroy you. Good luck.")
    print("----------------------------------------")

def Get_Player_Input(Ship_Board: Board) -> tuple[int, int]: # I put it able to return type None for the Menu

    while True:
        Row = input("Choose a Row: ")

        if Validate_Player_Input(Row, 0, Ship_Board.Number_of_Rows) == True:
            break

    while True:
        Column = input("Choose a Column: ")

        if Validate_Player_Input(Column, 0, Ship_Board.Number_of_Columns) == True:
            break

    return (int(Row), int(Column))

def Validate_Player_Input(Player_Input: str, Min_Limit: int, Max_Limit: int): # AI usage No. 1, Max_Limit parameter suggestion.
    # The problem was that if the amount of rows and columns were different then I can't tell what the maximum number was that the input could take
    # I could've just added a parameter of Max_Limit and was ashamed as this was a simple and easy solution

    if not Player_Input or Player_Input.isalpha() or not Player_Input.isdecimal(): # AI usage No. 4, Apparently the .isdecimal() function detects characters that can be used to form numbers in base 10. All I had to do was to reverse the condition for it??
        print("Invalid Input.")
        return False

    try:
        Converted_Player_Input = int(Player_Input)
        
        if (Min_Limit <= Converted_Player_Input < Max_Limit) == False: # I put a -1 to subtract 1 because it is for indexing and indexing starts at 0. If I pass in the int 5 for 5 rows, the max index would be 4.
            print("Your input for rows or columns is out of bounds!")
            return False
        else:
            return True

    except ValueError:
        print("There are some illegal characters in your input. You can't have any special characters, spaces, or just an empty input.")
        return False
    
def Handle_Player_Input(Guessed_Coordinates: tuple[int, int], Player_Ship_Board: Board, Enemy_Ship_Board: Board) -> bool:

    if Guessed_Coordinates in Player_Ship_Board.Guessed_Coordinates: # AI Usage No. 5, I couldn't figure out how to prevent the player from double guessing without the executor moving onto the opponent's turn
        print(f"You have already guessed Row: {Guessed_Coordinates[0]} and Column: {Guessed_Coordinates[1]}. Guess Again.")
        return False

    if not Guessed_Coordinates in Enemy_Ship_Board.Get_Ship_Locations(): # Check if the guessed coordinates matches with an enemy ship
        Player_Ship_Board.Guessed_Coordinates.update({Guessed_Coordinates: False})
        print(f"Row: {Guessed_Coordinates[0]} and Column: {Guessed_Coordinates[1]}. Miss.")
    else:
        Player_Ship_Board.Guessed_Coordinates.update({Guessed_Coordinates: True})
        Enemy_Ship_Board.Numbers_of_Ships -= 1
        print(f"Row: {Guessed_Coordinates[0]} and Column: {Guessed_Coordinates[1]}. Hit!")

    return True
    
def Get_Gamemode() -> str:
    while True:
        Game_mode = input("Who do you want to play with? A player or a computer? [Player / Computer]: ").strip().lower()

        if Game_mode != "player" and Game_mode != "computer":
            print("You need to enter either player or computer for your game mode!")
        else:
            return Game_mode

def Display_End_Game_Stats() -> None:
    print("--------------------")
    
    print(f"Final Score: {Game_State["Player One Score"]} - {Game_State["Player Two Score"]}")
    print("Thank You for playing BattleShip! (Python)")

    print("--------------------")

def Prompt_Player_for_Rows_and_Columns() -> tuple[int, int]:
    while True:
        Rows = input("How many Rows do you want: ").strip()

        if Validate_Player_Input(Rows, Game_Configuration["Minimum Rows and Columns"], (Game_Configuration["Maximum Rows and Columns"] + 1)) == True: # Had to put a + 1 here because the Validate_Player_Input() function does not include the Max_Limit number
            break

    while True:
        Columns = input("How many Columns do you want: ").strip()

        if Validate_Player_Input(Columns, Game_Configuration["Minimum Rows and Columns"], (Game_Configuration["Maximum Rows and Columns"] + 1)) == True: # Same thing here too
            break

    return (int(Rows), int(Columns))

def Check_for_Winner(Player_Ship_Board: Board, Enemy_Ship_Board: Board) -> bool | None:
    if Enemy_Ship_Board.Numbers_of_Ships <= 0: # Check if the opponent has 0 ships

        # The player that has the current turn will win (before the turn switches to the opponent)
        if Game_State["Current Turn"] == 1:
            print("Player One has won!")
            Game_State["Player One Score"] += 1

        elif Game_State["Current Turn"] == 2:
            print("Player Two has won!")
            Game_State["Player Two Score"] += 1

        Player_Ship_Board.Print_Ship_Board(Enemy_Ship_Board.Guessed_Coordinates, Show_Answer=True)
        Enemy_Ship_Board.Print_Ship_Board(Player_Ship_Board.Guessed_Coordinates, Show_Answer=True)
        
        print(f"Current Score: {Game_State["Player One Score"]} - {Game_State["Player Two Score"]}")
        
        return True
    else:
        return None
    
def Prompt_User_to_Play_Again() -> bool:
    while True:
        Restart_Choice = input("Do you want to play again? [Yes / No]: ").strip().lower()

        if Restart_Choice == "yes":
            return True
        elif Restart_Choice == "no":
            return False
        else:
            print(f"Did not recognize {Restart_Choice} as a valid input.")

def Play_BattleShip():
    Display_Introduction_and_Instructions()

    Rows, Columns = Prompt_Player_for_Rows_and_Columns()
    Game_Mode = Get_Gamemode()
    
    if Game_Mode == "player":
        Player_One = Board(Rows, Columns, "Player One")
        Player_Two = Board(Rows, Columns, "Player Two")

        Player_One.Place_Ships()
        Player_Two.Place_Ships()

        while True:

            while True: # AI Usage No. 5 is also spread here as well with more while True loops
                Player_One_Coordinates = Get_Player_Input(Player_One)
                if Handle_Player_Input(Player_One_Coordinates, Player_One, Player_Two) == True:
                    break

            Win_Check = Check_for_Winner(Player_One, Player_Two) # Pass in the opponent's board, so that the function can check if the opponent has all of their ships destroyed

            if Win_Check == True:
                break

            Player_Two.Print_Ship_Board(Player_One.Guessed_Coordinates, Show_Answer=False)
            Game_State["Current Turn"] = 2 # Now just pass the turn to the opponent

            while True:
                Player_Two_Coordinates = Get_Player_Input(Player_Two)
                if Handle_Player_Input(Player_Two_Coordinates, Player_Two, Player_One) == True:
                    break

            Win_Check = Check_for_Winner(Player_Two, Player_One)

            if Win_Check == True:
                break

            Player_One.Print_Ship_Board(Player_Two.Guessed_Coordinates, Show_Answer=False)
            Game_State["Current Turn"] = 1

    elif Game_Mode == "computer":
        Player = Board(Rows, Columns, "Player One")
        Computer = Board(Rows, Columns, "Computer")

        Player.Place_Ships()
        Computer.Generate_Ships()

        while True:

            while True:
                Player_Coordinates = Get_Player_Input(Player)
                if Handle_Player_Input(Player_Coordinates, Player, Computer) == True:
                    break

            Win_Check = Check_for_Winner(Player, Computer)

            if Win_Check == True:
                break

            Computer.Print_Ship_Board(Player.Guessed_Coordinates, Show_Answer=False)
            Game_State["Current Turn"] = 2

            Computer.Computer_Self_Play(Player)
            Win_Check = Check_for_Winner(Computer, Player)

            if Win_Check == True:
                break

            Player.Print_Ship_Board(Computer.Guessed_Coordinates, Show_Answer=False)
            Game_State["Current Turn"] = 1

    if Prompt_User_to_Play_Again() == True:
        Play_BattleShip()
    else:
        Display_End_Game_Stats()

Play_BattleShip()