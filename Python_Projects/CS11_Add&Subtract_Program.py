def Convert_User_Input_To_Integer(User_Input):
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

    if not User_Input or len(User_Input) == 0 or User_Input.isspace():
        print("You either entered nothing or just put spaces")
        return False
    
    for character in User_Input:
        if character.isalpha() or character.isspace():
            print("The input contained letters or some spaces!")
            return False
        
    if Convert_User_Input_To_Integer(User_Input) == False:
        print("Something wrong happened when attempting to convert User Input to an integer!")
        return False
        
    return True

def Check_For_Quitting(User_Input):
    if User_Input.upper() == "QUIT":
        print("Goodbye!")
        return True
    
    return False

def Add_Numbers(Value_A, Value_B):
    return Value_A + Value_B

def Subtract_Numbers(Value_A, Value_B):
    return Value_A - Value_B


print("Welcome to my Programming Quiz assignment where I have to make a program for adding and subtracting numbers!")
print("Choose the operator and then enter in the two numbers.")
print("Input QUIT (and variants) to quit the game!")

while True:
    Quit_Decision = False
    Operator = None
    Value_A = None
    Value_B = None

    while True:
        Operator = input("What arithmetic operator do you want to use? [1 - Addition and 2 - Subtraction]: ")

        if Check_For_Quitting(Operator) == True:
            Quit_Decision = True
            break

        elif Validate_User_Input(Operator) == False:
            print("Your input is not valid!")
            continue

        elif int(Operator) != 1 and int(Operator) != 2:
            print("Only 1 and 2 only for adding and subtracting!")
            continue

        else:
            Operator = int(Operator)
            break

    if Quit_Decision == True:
        break

    while True:
        Value_A = input("What is the first number?: ")

        if Check_For_Quitting(Value_A) == True:
            Quit_Decision = True
            break

        elif Validate_User_Input(Value_A) == False:
            print("Your input is not valid!")
            continue

        else:
            Value_A = int(Value_A)
            break

    if Quit_Decision == True:
        break

    while True:
        Value_B = input("What is the second number?: ")

        if Check_For_Quitting(Value_B) == True:
            Quit_Decision = True
            break

        elif Validate_User_Input(Value_B) == False:
            print("Your input is not valid!")
            continue

        else:
            Value_B = int(Value_B)
            break


    if Quit_Decision == True:
        break

    if Operator == 1:
        print("The Answer is: " + str(Add_Numbers(Value_A, Value_B)))
    elif Operator == 2:
        print("The Answer is: " + str(Subtract_Numbers(Value_A, Value_B)))