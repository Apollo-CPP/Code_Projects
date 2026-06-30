# Hey Michael! I left some comments on some parts where I used AI. Oh yeah, do you know any websites where I can get a human reviewer to look over my code? I had to use AI to review it but it did catch some nice errors though.

import random

Game_Board_Size: int = 3
Game_Board: list[list[str | None]] = [[None for _ in range(Game_Board_Size)]  for _ in range(Game_Board_Size)]
# Board_Comprehension = [[None for _ in range(3)] for _ in range(3)] This is also equivalent to Game_Board but as a nested loop comprehension
# Please don't laugh at me. Uh... I may or may not used AI for list comprehension 💀

Player_Marker: str = "X"
Opponent_Marker: str = "O"

def Get_Player_Mode() -> str:
    while True:
        Player_Mode = input("Do you want to play with another player or a computer? [Player / Computer]: ")

        if str.upper(Player_Mode) == "PLAYER" or str.upper(Player_Mode) == "COMPUTER":
            return str.upper(Player_Mode)
        else:
            print(f"\'{Player_Mode}\' is not recognized as a choice. Enter player or computer to choose.")

def Get_Empty_Spaces() -> set[tuple[int, int]]:
    return {
        (Row_Index, Column_Index)

        for Row_Index, Row in enumerate(Game_Board)
        for Column_Index, value in enumerate(Row)
        if value is None
    }

def Validate_Player_Choice(Player_Input: str) -> bool:
    try:
        Converted_Player_Input = int(Player_Input)

        # if Converted_Player_Input < 0 or Converted_Player_Input >= len(Game_Board):
        #     print("Out of bounds!")
        #     return False
        # else:
        #     return True

        if Converted_Player_Input not in range(0, len(Game_Board)): # I just learned, by myself (yay), that I can just do this. Better alternative for readability and consiceness than the original code above.
            # I only put len(Game_Board) because size is 3 and I want the player to be only able to guess from 0 - 2 and the end is exclusive so it works :D
            print("Out of bounds!")
            return False
        else:
            return True

    except ValueError:
        print("Value Error has been hit!")
        return False

def Computer_Random_Decision() -> None:
    # Valid_Random_Choice: bool = False
    # Computer_Choice: str | None = None

    # Empty_Spots: set[tuple[int, int]] = {(Row_Index, Column_Index) for Row_Index, Row in enumerate(Game_Board) for Column_Index, Column in enumerate(Row) if Column is None} # Very long list comprehension, I'm going to expand it for readability

    # Empty_Spots: set[tuple[int, int]] = { # I learned this from AI
    #     (Row_Index, Column_Index)

    #     for Row_Index, Row in enumerate(Game_Board)
    #     for Column_Index, value in enumerate(Row)
    #     if value is None
    # }

    Empty_Spots = Get_Empty_Spaces() # Turned into a function

    if not Empty_Spots:
        return

    Random_Row, Random_Column = random.choice(tuple(Empty_Spots))
    # random.choice picks a random element from a sequence (something indexable that's why I had to convert the set into an indexable table)

    # Random_Row, Random_Column = random.sample(tuple(Empty_Spots), 1)[0]
    
    # random.sample((Tuple, List, or Dictionary), # of random elemnts) will a return a list containing random elements
    # The [0] fetches the first ranom element in that list
    # I use tuple(Empty_Spots) because since Python 3.11, Python no longers supports automatic list to set conversion anymore
    # Computer_Choice gets a random tuple containing ints that are Empty spots in the Game_Board one time
    # Learned this from some AI and some from the official Python documentation

    Game_Board[Random_Row][Random_Column] = Opponent_Marker
    print(f"Computer has placed a {Opponent_Marker} on Row {Random_Row} and Column {Random_Column}!")
    Print_Game_Board()

    # Below is the original code, which has the Computer keep guessing, even random positions that aren't valid, until it gets a random position that is None
    # while Valid_Random_Choice == False:
    #     Random_Row = random.randint(0, 2)
    #     Random_Column = random.randint(0, 2)

    #     Computer_Choice = Game_Board[Random_Row][Random_Column]

    #     if Computer_Choice == Player_Marker or Computer_Choice == Computer_Marker:
    #         print(f"Computer has tried to place {Computer_Marker} on Row {Random_Row} and Column {Random_Column} but there is already a {Computer_Choice} marker on that spot!")
            
    #     elif Computer_Choice is None:
    #         print(f"Computer has placed {Computer_Marker} at Row {Random_Row} and Column {Random_Column}!")

    #         Game_Board[Random_Row][Random_Column] = Computer_Marker
    #         Valid_Random_Choice = True
    #         Print_Game_Board()

def Get_Player_Choice(Marker: str, Mode: str) -> None:
    # Valid_Row_Choice: bool | None = False
    # Valid_Column_Choice: bool | None = False
    # Valid_Chosen_Spot: bool = False

    Row_Choice: int | None = None
    Column_Choice: int | None = None

    # Empty_Spots: set[tuple[int, int]] = {
    #     (Row_Index, Column_Index)
    #     for Row_Index, Row in enumerate(Game_Board)
    #     for Column_Index, value in enumerate(Row)
    #     if value is None
    # }

    Empty_Spots = Get_Empty_Spaces() # Turned into a function

    if not Empty_Spots:
        return

    while True:
        while True:
            Player_Row_Input: str = input("Choose a Row: ")

            if Validate_Player_Choice(Player_Row_Input) == False:
                continue
            else:
                Row_Choice = int(Player_Row_Input)
                break

        while True:
            Player_Column_Input: str = input("Choose a Column: ")

            if Validate_Player_Choice(Player_Column_Input) == False:
                continue
            else:
                Column_Choice = int(Player_Column_Input)
                break

        if tuple((Row_Choice, Column_Choice)) not in Empty_Spots:
            
            if Mode == "PLAYER":
                if Marker == Player_Marker:
                    print(f"Player One tried to place {Player_Marker} on Row {Row_Choice} and Column {Column_Choice} but there is already a {Game_Board[Row_Choice][Column_Choice]} on that spot!")
                elif Marker == Opponent_Marker:
                    print(f"Player Two tried to place {Opponent_Marker} on Row {Row_Choice} and Column {Column_Choice} but there is already a {Game_Board[Row_Choice][Column_Choice]} on that spot!")

            elif Mode == "COMPUTER":
                print(f"You tried to place your {Marker} on that spot but there is already a {Game_Board[Row_Choice][Column_Choice]} on that spot!")

        else:
            Game_Board[Row_Choice][Column_Choice] = Marker
            Print_Game_Board()
            break


        # Player_Coordinate_Spot: str = Game_Board[Row_Choice][Column_Choice]

        # if Player_Coordinate_Spot == Opponent_Marker or Player_Coordinate_Spot == Player_Marker:
        #     print(f"You tried to place your {Player_Marker} on Row {Row_Choice} and Column {Column_Choice} but there is already a {Player_Coordinate_Spot} on that spot!")

        #     Row_Choice = None
        #     Column_Choice = None

        #     # Valid_Row_Choice = False
        #     # Valid_Column_Choice = False
        #     continue
        
        # else:
        #     Game_Board[Row_Choice][Column_Choice] = Marker

        #     if Player_Mode == "PLAYER":
        #         if Marker == Player_Marker:
        #             print(f"Player One has placed {Player_Marker} on Row {Row_Choice} and Column {Column_Choice}!")
        #         elif Marker == Opponent_Marker:
        #             print(f"Player Two has placed {Opponent_Marker} on Row {Row_Choice} and Column {Column_Choice}!")
        #     else:
        #         print(f"You have placed {Player_Marker} on Row {Row_Choice} and Column {Column_Choice}!")

        #     Print_Game_Board()

        #     # Valid_Chosen_Spot = True

def Check_For_Win_and_Tie(Mode: str) -> bool | None:
    Win_Combinations: tuple[tuple[tuple[str | None, ...], ...], ...] = (

        (
            # Horizontal
            (Game_Board[0][0], Game_Board[0][1], Game_Board[0][2]),
            (Game_Board[1][0], Game_Board[1][1], Game_Board[1][2]),
            (Game_Board[2][0], Game_Board[2][1], Game_Board[2][2]),
        ),

        (
            # Vertical
            (Game_Board[0][0], Game_Board[1][0], Game_Board[2][0]),
            (Game_Board[0][1], Game_Board[1][1], Game_Board[2][1]),
            (Game_Board[0][2], Game_Board[1][2], Game_Board[2][2])

        ),

        (
            # Diagonal
            (Game_Board[0][0], Game_Board[1][1], Game_Board[2][2]),
            (Game_Board[0][2], Game_Board[1][1], Game_Board[2][0])
        )
    )

    for Win_Group in Win_Combinations:

        for Win_Combo in Win_Group:

            if Win_Combo.count(None) <= 0 and Win_Combo.count(Win_Combo[0]) >= len(Win_Combo): # Had to use AI for checking winning combinations (I did not know how to ;-;)

                if Win_Combo[0] == Player_Marker:

                    if Mode == "PLAYER":
                        print("Player One has won!")
                        return True # Player won

                    elif Mode == "COMPUTER":
                        print("Player has won!")
                        return True # Player won

                elif Win_Combo[0] == Opponent_Marker:

                    if Mode == "PLAYER":
                        print("Player Two has won!")
                        return True # Opponent or other player has won
                    
                    elif Mode == "COMPUTER":
                        print("Computer has won!")
                        return True # Computer won
            
    for Row in Game_Board:
        for element in Row:
            if element is None:
                return None # Game is still on-going

    print("No one has won! There is a tie!")        
    return False # There is a tie!

def Print_Game_Board() -> None:
    print()

    print("  ", end="") # Had to a good amount of AI for those numbers on top and on the sides for making the board look nicer
    for Column in range(len(Game_Board[0])):
        print(Column, end=" ")
    print()

    for i, Row in enumerate(Game_Board):
        print(i, end=" ")

        for element in Row:
            print(element if element is not None else "-", end=" ")

        print()

    print()

def Cleanup_Game() -> None:
    global Player_Marker, Opponent_Marker

    # for Row in Game_Board: # This was the original code but apparently setting element to None doesn't work because element is a copy of the elements in the table?
    #     for element in Row:
    #         element = None

    # for i in range(len(Game_Board)): # Had to use AI and learned that I had to use enumerate to index it to actually change the table itself. I should've known this since I did C++ before Python bruh
    #     for j in range(len(Game_Board[i])):
    #         Game_Board[i][j] = None

    Player_Marker, Opponent_Marker = Opponent_Marker, Player_Marker

    for Row_Index in range(Game_Board_Size):
        for Column_Index in range(len(Game_Board[Row_Index])):
            Game_Board[Row_Index][Column_Index] = None

def Prompt_Play_Again() -> bool:
    while True:
        Player_Restart_Decision = str.upper(input("Do you want to play again? [Y / N]: "))

        if Player_Restart_Decision != "Y" and Player_Restart_Decision != "N":
            print("Couldn't recognize input. Put Y or N to make your choice to play again.")
            continue
        
        elif Player_Restart_Decision == "Y":
            return True
        
        elif Player_Restart_Decision == "N":
            return False
        
print("Welcome to Tic-Tac-Toe!")
print("Your goal is to get 3 in a row to win!")

while True:

    Player_Mode = Get_Player_Mode()
    Print_Game_Board()

    if Player_Mode == "PLAYER":
        while True:
            
            print("Player One's Turn!")
            Get_Player_Choice(Player_Marker, Player_Mode)

            Game_Status_Check_1 = Check_For_Win_and_Tie(Player_Mode)

            if Game_Status_Check_1 == True or Game_Status_Check_1 == False:
                break

            print("Player Two's Turn!")
            Get_Player_Choice(Opponent_Marker, Player_Mode)

            Game_Status_Check_2 = Check_For_Win_and_Tie(Player_Mode)

            if Game_Status_Check_2 == True or Game_Status_Check_2 == False:
                break

    elif Player_Mode == "COMPUTER":
        while True:
            Get_Player_Choice(Player_Marker, Player_Mode)

            Game_Status_Check_1 = Check_For_Win_and_Tie(Player_Mode)

            if Game_Status_Check_1 == True or Game_Status_Check_1 == False:
                break

            Computer_Random_Decision()

            Game_Status_Check_2 = Check_For_Win_and_Tie(Player_Mode)

            if Game_Status_Check_2 == True or Game_Status_Check_2 == False:
                break


    User_Play_Again_Choice = Prompt_Play_Again()

    if User_Play_Again_Choice == True:
        Cleanup_Game()
    else:
        print("Goodbye!")
        break