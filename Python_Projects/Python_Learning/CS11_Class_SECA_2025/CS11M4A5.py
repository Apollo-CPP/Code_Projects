# This is my code for the Module 4, Assignment 5, 3 Mini Programming Assignment! >:-D
# Scripted on November 22, 2025 for my CS-11 class

import math

Image_A = ''''

,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
|1/2| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | + | ' | <-    |
|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|
| ->| | Q | W | E | R | T | Y | U | I | O | P | ] | ^ |     |
|-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |
| Caps | A | S | D | F | G | H | J | K | L | \ | [ | * |    |
|----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|
|    | < | Z | X | C | V | B | N | M | , | . | - |          |
|----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|
| ctrl |  | alt |                          |altgr |  | ctrl |
'------'  '-----'--------------------------'------'  '------'

'''

Image_B = '''
 .------------------------------------------,
| .---------------------------------------, |
| | _~_                                   | |
| |  \/  Texas Instruments     T I - 8 6  | |
| | .-----------------------------------, | |
| | |                                   | | |
| | | 1 + 1                             | | |
| | |                                   | | |
| | |                                2  | | |
| | |                                   | | |
| | | 6 * 8                             | | |
| | |                               48  | | |
| | |                                   | | |
| | | _                                 | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | `-----------------------------------' | |
| |                                       | |
| `---------------------------------------' |
|     M1      M2      M3      M4      M5    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  F1 | |  F2 | |  F3 | |  F4 | |  F5 |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|-------.________          ________,--------|
|                `--------'                 |
|                                           |
|          QUIT    MODE        _,-._        |
|  .-----, .-----, .-----,  /\ \_^_/ /\     |
|  | 2nd | | EXIT| | MORE| / /   |   \ \    |
|  `-----' `-----' `-----' |<|   O   |>|    |
|  alpha   LINK x  INS     \ \  _|_  / /    |
|  .-----, .-----, .-----,  \/ / v \ \/     |
|  |ALPHA| |x-VAR| | DEL |     -._,-        |
|  `-----' `-----' `-----'                  |
|  SOLVER  SIMULT  POLY   CATLG-VARS        |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |GRAPH| |TABLE| | PRGM| |CUSTM| |CLEAR|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  10x  A  SIN-1 B COS-1 C TAN-1 D pi   E   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LOG | | SIN | | COS | | TAN | |  ^  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ex   F  x-1  G  [    H  ]    I  CALC J   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LN  | | EE  | |  (  | |  )  | |     |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ./~  K  MATRX L VECTR M CPLX N  MATH O   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | X2  | |  7  | |  8  | |  9  | |  x  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  /_   P  CONS Q  CONV R  STRNG S LIST T   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  ,  | |  4  | |  5  | |  6  | |  -  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  RCL  =  BASE U  TEST V  MEM  W  STAT X   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | STO>| |  1  | |  2  | |  3  | |  +  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  OFF     CHAR Y  :    z  ANS  _  ENTRY    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | ON  | |  0  | |  .  | | (-) | |ENTER|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  -------                                  |
`\                                         /'
  `-._                                 _.-'
      `--.__                     __.--'
            ``----.._____,,---
'''

def Convert_Input_To_Int(User_Input):
    try:
        Converted_Input = int(User_Input)
        return True
    except ValueError:
        print("Value Error hit!")
        return False
    except TypeError:
        print("Type Error hit!")
        return False
    
def Validate_User_Input(User_Input):

    if not User_Input or len(User_Input) == 0:
        print("You entered nothing??")
        return False

    elif Convert_Input_To_Int(User_Input) == False:
        print("Failed to convert your input! :(")
        return False
    
    return True

def Check_For_User_Quitting(User_Input):
    if User_Input == "Quit":
        return True
    else:
        return False
    
while True:
    print("Welcome to Module 4, Assignment 5, Mini Programming Practice!")
    print("Enter -1 to Quit!")

    while True:
        print("Area of a circle calculator")
        print("Formula = pi * Radius^2")

        Radius = input("What is the radius of the circle?: ")

        if Check_For_User_Quitting(Radius) == True:
            print("Goodbye!")
            break

        elif Validate_User_Input(Radius) == False:
            print("Failed validation check!")
            continue

        elif Convert_Input_To_Int(Radius) == False:
            print("Failed to convert Radius into an integer!")
            continue

        else:
            Area_of_Circle = math.pi * math.pow(int(Radius), 2)
            print("The radius of the circle is " + str(Area_of_Circle))
            break

    while True:
        print("Expression Calculator: (a - b) + (a * b)")

        Value_A = input("What is the value of A?: ")

        if Check_For_User_Quitting(Value_A) == True:
            print("Goodbye!")
            break

        elif Validate_User_Input(Value_A) == False:
            print("Failed validation check!")
            continue

        elif Convert_Input_To_Int(Value_A) == False:
            print("Failed to convert Value A into an integer!")
            continue

        Value_B = input("What is the value of B?: ")

        if Check_For_User_Quitting(Value_B) == True:
            print("Goodbye!")
            break

        elif Validate_User_Input(Value_B) == False:
            print("Failed validation check!")
            continue

        elif Convert_Input_To_Int(Value_B) == False:
            print("Failed to convert Value B into an integer!")
            continue

        Answer_of_Expression = (int(Value_A) - int(Value_B)) + (int(Value_A) * int(Value_B))
        print("The answer of the expression is: " + str(Answer_of_Expression))
        break

    while True:
        Image_Decision = input("What ASCII image do you want to see? (1 or 2): ")

        if Check_For_User_Quitting(Image_Decision) == True:
            print("Goodbye!")
            break

        elif Validate_User_Input(Image_Decision) == False:
            print("Failed to convert Image Decision into an integer!")
            continue

        if int(Image_Decision) == 1:
            print(Image_A)
            break

        elif int(Image_Decision) == 2:
            print(Image_B)
            break

        else:
            print("Your input has to be 1 or 2, your input " + Image_Decision + " is not a valid input!")
            continue

    break