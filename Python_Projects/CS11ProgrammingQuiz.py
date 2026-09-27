#This is a MadLibs project
#My name: Dylan Zhang
#Who I collaborated with: N/A
print("************************************")
print("| |")
print("| Welcome to MadLibs | ")
print("| |")
print("************************************") # Missing "" to make it a string (Added quotes)

# For line 11 it was supposed to be a multi-line print function and it missed one " ' " (Added one ' and print function)
print('''MadLibs is a fill-in-the-blanks story
game. The player must choose words based on the
given prompts, and the computer will return a
short story that includes the words the user chose.''')
play = input("Do you want to play MadLibs?(y/n) ") # Misspelled input (Changed onput to input)
if play == "y": # Missed one more = sign to make the interpreter compare if it's equal to the string "y" AND missed colon (:) for if statement syntax (Added another = sign)

    # Indented EVERY line from here from line 14 to line 35 for if statement syntax rules

    person_name = input("Choose a name for a person: ")
    place = input("Choose a place: ")
    noun_1 = input("Choose a singlular noun: ")
    animal_1 = input("Choose an animal: ") # Missing quotes for inputting (Added quotes)
    adjective_1 = input("Choose an adjective for a feeling: ")
    adjective_2 = input("Choose an adjective: ")
    adjective_3 = input("Choose an adjective: ") # Missing equal sign to set value for variable as an input (Added = sign)
    animal_2 = input("Choose an animal: ")
    food = input("Choose a food: ")
    print("""
    Over break I am going camping with """ +person_name+""". It is important
    to be prepared when camping at place , so I made sure to pack a
    sleeping bag, flashlight, and a """ +noun_1+""". The possibility of seeing a
    """ +animal_1+""" makes me feel """ +adjective_1+""". I am excited to go
    hiking on the """ +adjective_2+""" trail. If I see a """ +adjective_3 +""" """
    +animal_2+"""
    on the hike, I will take it home as my new pet! The best part of
    camping is eating """ +food+""" by the campfire!
    """)
    print("Thanks for playing! Goodbye!")
else:
    print("Goodbye!")
    # Indented line 39 for if statement syntax rules