import random

Max_Guesses = 5
Player_Guesses = 0

Min = 1
Max = 100
Random_Number = random.randint(Min, Max)

print("Welcome to guess the number game!")
print("A random number has been generated from 1 - 100, guess the number correctly and you win!")
print("There will also be hints for you to guess lower or higher to help you guess the  number")
print("You can also input QUIT (and variants) to quit the game")

def Convert_Player_Guess_To_Int(User_Input):

    try:
        Converted_Guss = int(User_Input)
        return True
    
    except ValueError:
        print("Value Error hit!")
        return False
    
    except TypeError:
        print("Type Error hit!")
        return False

def Check_Guess_In_Range(Player_Guess):

    if Player_Guess < Min or Player_Guess > Max:
        print("Your guess is out of range (1 - 100)!")
        return False
    
    return True

def Give_Player_Hint(Player_Guess):

    if Player_Guess < Random_Number and Player_Guess > Min:
        print("Guess Higher!")

    elif Player_Guess > Random_Number and Player_Guess < Max:
        print("Guess Lower!")

    else:
        print("What just happened?")

while Player_Guesses < Max_Guesses:
    Player_Guess_Number = input("Guess: ")

    if Player_Guess_Number.upper() == "QUIT":
        print("Goodbye!")
        break
    
    elif Convert_Player_Guess_To_Int(Player_Guess_Number) == False:
        print("Failed to convert player's guess into an integer!")

    else:
        Player_Guess_Number = int(Player_Guess_Number)
        Player_Guesses += 1
        print(f"Guesses Left: {Max_Guesses - Player_Guesses}")

        if Player_Guess_Number == Random_Number:
            print(f"Nice. You guessed the random number {Random_Number}")
            break

        elif Player_Guesses >= Max_Guesses:
            print(f"Game Over! You've ran out of guesses! The random number was {Random_Number}!")
            break
        
        else:

            if Check_Guess_In_Range(Player_Guess_Number) == False:
                print("Player's Guess is out of range!")

            else:
                Give_Player_Hint(Player_Guess_Number)