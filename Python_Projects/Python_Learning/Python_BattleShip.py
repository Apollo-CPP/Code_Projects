import random

Game_Configuration: dict[str, int] = {
    "Random_Ship_Chance": 300,
    "Ship_Spawn_Chance": 50,
    
    "Minimum Rows and Columns": 5,
    "Maximum Rows and Columns": 10,
    "Max Ships": 10
}

Game_State: dict[str, int] = {
    "Current Turn": 1,

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
        self.Numbers_of_Ships: int = 0

    def Place_Ships(self) -> None:
        while self.Numbers_of_Ships < Game_Configuration["Max Ships"]:

            while True:
                Ship_Row = input(f"Ship {self.Numbers_of_Ships + 1} Row: ").strip()

                if not Ship_Row or Ship_Row.isalpha() or not Ship_Row.isdecimal():
                    print("Invalid Input.")
                    continue

                try:
                    if 0 <= int(Ship_Row) <= self.Number_of_Rows:
                        break
                    else:
                        print(f"You can only place your ships between Rows 0 and {self.Number_of_Rows}.")
                except ValueError:
                    print("Invalid Input.")

            while True:
                Ship_Column = input(f"Ship {self.Numbers_of_Ships + 1} Column: ").strip()

                if not Ship_Column or Ship_Column.isalpha() or not Ship_Column.isdecimal():
                    print("Invalid Input.")
                    continue

                try:
                    if 0 <= int(Ship_Column) <= self.Number_of_Columns:
                        break
                    else:
                        print(f"You can only place your ships between Columns 0 and {self.Number_of_Columns}.")
                except ValueError:
                    print("Invalid Input.")

            if (int(Ship_Row), int(Ship_Column)) in self.__Ship_Locations:
                print(f"Couldn't place Ship {self.Numbers_of_Ships + 1} in Row {Ship_Row} and Column {Ship_Column} because there is already a ship placed there!")
                continue

            self.__Ship_Locations.add((int(Ship_Row), int(Ship_Column)))
            self.Numbers_of_Ships += 1


    def Generate_Ships(self) -> None: # Updated - This is now from the computer only. There's a new function that will allow players to place their ships
        for i in range(self.Number_of_Rows):
            for j in range(self.Number_of_Columns):

                if self.Numbers_of_Ships >= Game_Configuration["Max Ships"]:
                    break

                Random_Chance: int = random.randint(0, Game_Configuration["Random_Ship_Chance"]) # Random Number from 0 to 300 (I put 300 for better probability and randomness)

                if Random_Chance <= Game_Configuration["Ship_Spawn_Chance"]: # Just check if the Random Chance is less than or equal to 50
                    self.__Ship_Locations.add((i, j))
                    self.Numbers_of_Ships += 1
                    print(f"Row: {i}, Column: {j}") # Debugging Purposes

        print("--------------------")

        if self.Numbers_of_Ships <= 0:
            print("Failed to generate ships for a board. Generating Ships Again...")
            self.Generate_Ships() # Recursion >:-D

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

    def Retrieve_Board_Symbol(self, Row_Index: int, Column_Index: int, Enemy_Ship_Locations: set[tuple[int, int]], Show_Answer: bool) -> str:
        Coordinates: tuple[int, int] = (Row_Index, Column_Index)
        # I know there's a lot of nesting but I hope I can improve this later

        if Show_Answer == True:
            
            if not self.Guessed_Coordinates.get(Coordinates): # Player did not guess these coordinates
                
                if Coordinates not in Enemy_Ship_Locations: # The coordinates that the player did not guess was not a ship. Return the "~" sign
                    return "~"
                else:
                    return "!" # The coordinates that the player did not guess was a ship. Return the "!" sign
            else:
                if Coordinates not in Enemy_Ship_Locations: # The player did guess the coordinates but it was not a ship. Return the "O" sign
                    return "O"
                else: # The player did guess the coordinates and it was a ship. Return the "X" sign
                    return "X"
                
        else:
            if not self.Guessed_Coordinates.get(Coordinates):
                return "~"
        
            if Coordinates not in Enemy_Ship_Locations:
                return "O"
            else:
                return "X"
        
    def Print_Ship_Board(self, Ship_Locations: set[tuple[int, int]], Show_Answer: bool) -> None:
        # print(*(Column_Number for Column_Number in range(len(self.Ship_Board[0]))), sep=" ") # AI Usage No. 2 - I was confused on how to print the elements using a comprehension but while also separating them with a space
        # Apparently all I had to do was just to unpackage it using the * sign
        # Later thought about it and changed it to the version below for readability

        for Column in range(self.Number_of_Columns):
            print(Column, end=" ")
        print()

        if Show_Answer == True:
            for i in range(self.Number_of_Rows):
                for j in range(self.Number_of_Columns):
                    print(self.Retrieve_Board_Symbol(i, j, Ship_Locations, Show_Answer=True), end=" ")
                print()
        else:
            for i in range(self.Number_of_Rows):
                for j in range(self.Number_of_Columns):
                    print(self.Retrieve_Board_Symbol(i, j, Ship_Locations, Show_Answer=False), end=" ")
                print()

    def Computer_Self_Play(self, Player_Board: Board) -> None: # Hey! This is only used when the Game mode is computer so that the computer can generate a random coordinate
        Empty_Spots = {
            (Row_Index, Column_Index)

            for Row_Index in range(self.Number_of_Rows)
            for Column_Index in range(Row_Index)
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
    print("2. Your input needs to be within the range of 0 - (Ship Row or Ship Column depending on which input you're putting in for) MINUS 1 because tables start at the index of 0 instead of 1")

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

        if Validate_Player_Input(Row, 0, Ship_Board.Number_of_Rows) == True: # I put 0 because it is not at the very beginning where you choose the amount of rows and columns you want and so that when you play, the player can properly guess without causing issues
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
        
        if (Min_Limit <= Converted_Player_Input <= Max_Limit) == False:
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
        Player_Ship_Board.Guessed_Coordinates.update({Guessed_Coordinates: False}) # Add coordinates as key and True or False if it is an enemy ship or not, in this case it is False because the guessed coordinates does not match any of the opponent's ships
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

    print(f"Player One Total Hits: {Game_State["Player One Total Hits"]}")
    print(f"Player Two Total Hits: {Game_State["Player Two Total Hits"]}")
    print(f"Final Score: {Game_State["Player One Score"]} - {Game_State["Player Two Score"]}")

    print("Thank You for playing BattleShip! (Python)")

    print("--------------------")

def Prompt_Player_for_Rows_and_Columns() -> tuple[int, int]:
    while True:
        Rows = input("How many Rows do you want: ")

        if Validate_Player_Input(Rows, Game_Configuration["Minimum Rows and Columns"], Game_Configuration["Maximum Rows and Columns"]) == True:
            break

    while True:
        Columns = input("How many Columns do you want: ")

        if Validate_Player_Input(Columns, Game_Configuration["Minimum Rows and Columns"], Game_Configuration["Maximum Rows and Columns"]) == True:
            break

    return (int(Rows), int(Columns))

def Check_for_Winner(Enemy_Ship_Board: Board) -> bool | None:
    if Enemy_Ship_Board.Numbers_of_Ships <= 0: # Check if the opponent has 0 ships

        # The player that has the current turn will win (before the turn switches to the opponent)
        if Game_State["Current Turn"] == 1:
            print("Player One has won!")
        elif Game_State["Current Turn"] == 2:
            print("Player Two has won!")
        
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
        Player_One = Board(Rows, Columns)
        Player_Two = Board(Rows, Columns)

        Player_One.Place_Ships()
        Player_Two.Place_Ships()

        while True:

            while True: # AI Usage No. 5 is also spread here as well with more while True loops
                Player_One_Coordinates = Get_Player_Input(Player_One)
                if Handle_Player_Input(Player_One_Coordinates, Player_One, Player_Two) == True:
                    break

            Win_Check = Check_for_Winner(Player_Two) # Pass in the opponent's board, so that the function can check if the opponent has all of their ships destroyed

            if Win_Check == True:
                Game_State["Player One Score"] += 1
                break

            Player_Two.Print_Ship_Board(Player_Two.Get_Ship_Locations(), Show_Answer=False)
            Game_State["Current Turn"] = 2 # Now just pass the turn to the opponent

            while True:
                Player_Two_Coordinates = Get_Player_Input(Player_Two)
                if Handle_Player_Input(Player_Two_Coordinates, Player_One, Player_Two) == True:
                    break

            Win_Check = Check_for_Winner(Player_One)

            if Win_Check == True:
                Game_State["Player Two Score"] += 1
                break

            Player_One.Print_Ship_Board(Player_One.Get_Ship_Locations(), Show_Answer=False)
            Game_State["Current Turn"] = 1

    elif Game_Mode == "computer":
        Player = Board(Rows, Columns)
        Computer = Board(Rows, Columns)

        Player.Place_Ships()
        Computer.Generate_Ships()

        while True:

            while True:
                Player_Coordinates = Get_Player_Input(Player)
                if Handle_Player_Input(Player_Coordinates, Player, Computer) == True:
                    break

            Win_Check = Check_for_Winner(Computer)

            if Win_Check == True:
                Game_State["Player One Score"] += 1
                break

            Computer.Print_Ship_Board(Computer.Get_Ship_Locations(), Show_Answer=False)
            Game_State["Current Turn"] = 2

            Computer.Computer_Self_Play(Player)
            Win_Check = Check_for_Winner(Player)

            if Win_Check == True:
                Game_State["Player Two Score"] += 1
                break

            Player.Print_Ship_Board(Player.Get_Ship_Locations(), Show_Answer=False)
            Game_State["Current Turn"] = 1

    if Prompt_User_to_Play_Again() == True:
        Play_BattleShip()
    else:
        Display_End_Game_Stats()

Play_BattleShip()