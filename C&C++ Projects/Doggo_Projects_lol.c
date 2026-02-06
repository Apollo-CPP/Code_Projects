// PROJECT FOR NUMBER GUESSING GAME

// #include <stdio.h>

// int getNumToGuess();
// void clearScreen();
// bool tooHigh();
// bool tooLow();
// char continueGame();

// int main() {
//     int Number_to_Guess = 0;
//     int Turns_Used = 0;
//     int Player1_Guess = 0;
//     int Player2_Guess = 0;
//     char Continue_Playing_Decision;

//     do {
//         Number_to_Guess = getNumToGuess();
//         clearScreen();

//         while (Player2_Guess != Number_to_Guess) {
//             printf("Guess Number: ");
//             scanf("%d", &Player2_Guess);

//             if (tooHigh(Number_to_Guess, Player2_Guess)) {
//                 Turns_Used = Turns_Used + 1;
//                 continue;

//             } else if (tooLow(Number_to_Guess, Player2_Guess)) {
//                 Turns_Used = Turns_Used + 1;
//                 continue;

//             } else {
//                 Turns_Used = Turns_Used + 1;
//                 printf("Congratulations! You guessed the number: %d and it took you %d tries! \n", Number_to_Guess, Turns_Used);
                
//                 // Reset values here
//                 Player2_Guess = 0;
//                 Number_to_Guess = 1;
//                 Turns_Used = 0;
//                 break;
//             }
//         }

//         Continue_Playing_Decision = continueGame();

//     } while (Continue_Playing_Decision == 'Y' || Continue_Playing_Decision == 'y'); // Repeat the game until the player's decision to restart is Y or y to keep playing
// }

// int getNumToGuess() {
//     int Player1Number;
//     printf("Enter player for Player 2 to Guess: ");
//     scanf("%d", &Player1Number);
//     return Player1Number;
// }

// void clearScreen() {
//     for (int i = 0; i < 1000; i++) {
//         printf("\n"); // For loop to insert 1000 new lines to clear the screen!
//     }
// }

// // These functions are just making sure if the player's guess was close, too low, or too high! (Will give hint if close though)
// bool tooHigh(int Number_To_Guess, int player2_Guess) {
//     if (player2_Guess > Number_To_Guess) {
//         if ((player2_Guess - Number_To_Guess) <= 10) {
//             printf("Sooo close! Guess a little bit lower! \n");
//             return true;

//         } else {
//             printf("Too High! \n");
//         }

//         return true;
//     }

//     return false;
// }

// bool tooLow(int Number_To_Guess, int player2_Guess) {
//     if (player2_Guess < Number_To_Guess) {
//         if ((Number_To_Guess - player2_Guess) <= 10) {
//             printf("Sooo close! Guess a little bit higher! \n");
//             return true;

//         } else {
//             printf("Too Low! \n");
//         }

//         return true;
//     }

//     return false;
// }

// char continueGame() {
//     char Play_Again;

//     do {
//         printf("Would you like to play again? [Y / N]: ");
//         scanf("%c", &Play_Again);
//     } while (Play_Again != 'Y' && Play_Again != 'y' && Play_Again != 'N' && Play_Again != 'n'); // Ask player to confirm restarting the game until the player gives a valid answer
    
//     return Play_Again;
// }

// AN ADVENTURE PROJECT

// #include <stdio.h>
// #include <stdbool.h>

// int Get_User_Mode();
// int Get_Player_Decision();

// int Explore_Woods();
// int Explore_Pond();
// int Explore_Rock();
// int Fight_Orc_Decision();

// bool Check_For_Equal_Items(int Items);
// bool Check_For_Needed_Items(bool Obtained_Fingernail_of_Doom, bool Obtained_Wall_of_Ice);

// int Check_For_Play_Again();

// int main() {
//     int Play_Again_Decision = 0;

//     do {
//         bool Obtained_Wall_of_Ice = false;
//         bool Obtained_Fingernail_of_Doom = false;
//         bool Obtained_Devilish_Dicer_Sword = false;

//         int Items = 0;
//         int Player_Explore_Decision = 0;
//         int Player_Fight_Orc_Decision = 0;
        
//         int Mode = 0;
//         Mode = Get_User_Mode();

//         switch (Mode) {
//             case 1: // The woods, the pond, a rock

//                 Player_Explore_Decision = Explore_Woods();

//                 if (Player_Explore_Decision == 1) {
//                     printf("You have found uncovered a Devilish Dicer Sword! This can be used for attacking monsters! \n");
//                     Obtained_Devilish_Dicer_Sword = true;
//                     Items++;

//                 } else if (Player_Explore_Decision == 2) {
//                     printf("You ignore it, but your curiousity of it had you trip over a small log scraping your head but continued along your journey! \n");
//                 }

//                 Player_Explore_Decision = Explore_Pond();

//                 if (Player_Explore_Decision == 1) {
//                     printf("You have discovered a Wall of Ice! This should be able to protect you on your journey! \n");
//                     Obtained_Wall_of_Ice = true;
//                     Items++;

//                 } else if (Player_Explore_Decision == 2) {
//                     printf("You don't think much of it and continue on. \n");
//                 }

//                 Player_Explore_Decision = Explore_Rock();

//                 if (Player_Explore_Decision == 1) {
//                     printf("You found a fingernail of doom! This will destroy your enemies on your journey! \n");
//                     Obtained_Fingernail_of_Doom = true;
//                     Items++;

//                 } else if (Player_Explore_Decision == 2) {
//                     printf("You are afraid of it and had your heart pounding so hard that you nearly pass out and quickly move on. \n");
//                 }

//                 Player_Fight_Orc_Decision = Fight_Orc_Decision();

//                 if (Player_Fight_Orc_Decision == 1) {
//                     bool Equal_Items = Check_For_Equal_Items(Items);

//                     if (!Equal_Items) {
//                         break;

//                     } else {
//                         bool Check_if_Player_has_Needed_Items = Check_For_Needed_Items(Obtained_Fingernail_of_Doom, Obtained_Wall_of_Ice);

//                         if (!Check_if_Player_has_Needed_Items) {
//                             printf("You attempt to battle the orc but you don't have the neccessary items to attack and defend yourself. You try to turn back and run but fall. You get sliced by the orc. Game Over! You lost! \n");

//                         } else {
//                             printf("You fight the orc and you win the battle! You won! Your journey is complete! \n");
//                         }
//                     }

//                 } else if (Player_Fight_Orc_Decision == 2) {
//                     printf("You try to flee but trip on a rock and fall. The orc rushes over to you and slices you. Game Over! You lost! \n");
//                 }

//                 break;

//             case 2: // The pond, the woods, a rock

//                 Player_Explore_Decision = Explore_Pond();

//                 if (Player_Explore_Decision == 1) {
//                     printf("You have discovered a Wall of Ice! This should be able to protect you on your journey! \n");
//                     Obtained_Wall_of_Ice = true;
//                     Items++;

//                 } else if (Player_Explore_Decision == 2) {
//                     printf("You don't think much of it but almost drowned in the pond and decided to continue on. \n");
//                 }

//                 Player_Explore_Decision = Explore_Woods();

//                 if (Player_Explore_Decision == 1) {
//                     printf("You have found uncovered a Devilish Dicer Sword! This can be used for attacking monsters! \n");
//                     Obtained_Devilish_Dicer_Sword = true;
//                     Items++;

//                 } else if (Player_Explore_Decision == 2) {
//                     printf("You ignore it, but your curiousity of it had you trip over a small log scraping your head but continued along your journey! \n");
//                 }

//                 Player_Explore_Decision = Explore_Rock();

//                 if (Player_Explore_Decision == 1) {
//                     printf("You found a fingernail of doom! This will destroy your enemies on your journey! \n");
//                     Obtained_Fingernail_of_Doom = true;
//                     Items++;

//                 } else if (Player_Explore_Decision == 2) {
//                     printf("You are afraid of it and had your heart pounding so hard that you nearly pass out and quickly move on. \n");
//                 }

//                 Player_Fight_Orc_Decision = Fight_Orc_Decision();

//                 if (Player_Fight_Orc_Decision == 1) {
//                     bool Equal_Items = Check_For_Equal_Items(Items);

//                     if (!Equal_Items) {
//                         break;

//                     } else {
//                         bool Check_if_Player_has_Needed_Items = Check_For_Needed_Items(Obtained_Fingernail_of_Doom, Obtained_Wall_of_Ice);

//                         if (!Check_if_Player_has_Needed_Items) {
//                             printf("You attempt to battle the orc but you don't have the neccessary items to attack and defend yourself. You try to turn back and run but fall. You get sliced by the orc. Game Over! You lost! \n");

//                         } else {
//                             printf("You fight the orc and you win the battle! You won! Your journey is complete! \n");
//                         }
//                     }

//                 } else if (Player_Fight_Orc_Decision == 2) {
//                     printf("You try to flee but trip on a rock and fall. The orc rushes over to you and slices you. Game Over! You lost! \n");
//                 }

//             case 3: // the rock, the ponds, the woods

//                 Player_Explore_Decision = Explore_Rock();

//                 if (Player_Explore_Decision == 1) {
//                     printf("You found a fingernail of doom! This will destroy your enemies on your journey! \n");
//                     Obtained_Fingernail_of_Doom = true;
//                     Items++;

//                 } else if (Player_Explore_Decision == 2) {
//                     printf("You are afraid of it and had your heart pounding so hard that you nearly pass out and quickly move on. \n");
//                 }

//                 Player_Explore_Decision = Explore_Pond();

//                 if (Player_Explore_Decision == 1) {
//                     printf("You have discovered a Wall of Ice! This should be able to protect you on your journey! \n");
//                     Obtained_Wall_of_Ice = true;
//                     Items++;

//                 } else if (Player_Explore_Decision == 2) {
//                     printf("You don't think much of it but almost drowned in the pond and decided to continue on. \n");
//                 }

//                 Player_Explore_Decision = Explore_Woods();

//                 if (Player_Explore_Decision == 1) {
//                     printf("You have found uncovered a Devilish Dicer Sword! This can be used for attacking monsters! \n");
//                     Obtained_Devilish_Dicer_Sword = true;
//                     Items++;

//                 } else if (Player_Explore_Decision == 2) {
//                     printf("You ignore it, but your curiousity of it had you trip over a small log scraping your head but continued along your journey! \n");
//                 }

//                 Player_Fight_Orc_Decision = Fight_Orc_Decision();

//                 if (Player_Fight_Orc_Decision == 1) {
//                     bool Equal_Items = Check_For_Equal_Items(Items);

//                     if (!Equal_Items) {
//                         break;

//                     } else {
//                         bool Check_if_Player_has_Needed_Items = Check_For_Needed_Items(Obtained_Fingernail_of_Doom, Obtained_Wall_of_Ice);

//                         if (!Check_if_Player_has_Needed_Items) {
//                             printf("You attempt to battle the orc but you don't have the neccessary items to attack and defend yourself. You try to turn back and run but fall. You get sliced by the orc. Game Over! You lost! \n");

//                         } else {
//                             printf("You fight the orc and you win the battle! You won! Your journey is complete! \n");
//                         }
//                     }

//                 } else if (Player_Fight_Orc_Decision == 2) {
//                     printf("You try to flee but trip on a rock and fall. The orc rushes over to you and slices you. Game Over! You lost! \n");
//                 }

//             default:
//                 break;
//             }

//         Play_Again_Decision = Check_For_Play_Again();

//         if (Play_Again_Decision == 2) {
//             printf("Goodbye! \n");
//             break;
//         }

//     } while (Play_Again_Decision == 1);

//     return 0;
// }

// int Get_User_Mode() {
//     int Player_Mode_Decision = 0;

//     printf("What mode do you want to play? [1, 2, or 3]: ");
//     scanf("%d", &Player_Mode_Decision);

//     return Player_Mode_Decision;
// }

// int Get_Player_Decision() {
//     int Explore_Decision = 0;
//     printf("Explore Decision: ");
//     scanf("%d", &Explore_Decision);

//     return Explore_Decision;
// }

// int Explore_Woods() {
//     int Player_Explore_Decision = 0;

//     do {
//         printf("You found yourself wondering through the woods and see a circle poking out behind a tree. It looks like a handle for something..? Do you wish to explore it? [1 - Yes, 2 - No] \n");
//         Player_Explore_Decision = Get_Player_Decision();
//     } while (Player_Explore_Decision != 1 && Player_Explore_Decision != 2);

//     return Player_Explore_Decision;
// }

// int Explore_Pond() {
//     int Player_Explore_Decision = 0;

//     do {
//         printf("You see an object that looks a shiny, through the ponds. Do you go closer near the lily pads to inspect it? [1 - Yes, 2 - No] \n");
//         Player_Explore_Decision = Get_Player_Decision();
//     } while (Player_Explore_Decision != 1 && Player_Explore_Decision != 2);

//     return Player_Explore_Decision;
// }

// int Explore_Rock() {
//     int Player_Explore_Decision = 0;

//     do {
//         printf("You see a dark yet glowing item behind a rock. You are scared but curious. Do you want to see it? [1 - Yes, 2 - No] \n");
//         Player_Explore_Decision = Get_Player_Decision();
//     } while (Player_Explore_Decision != 1 && Player_Explore_Decision != 2);

//     return Player_Explore_Decision;
// }

// int Fight_Orc_Decision() {
//     int Player_Explore_Decision = 0;
//     do {
//         printf("You have encountered an orc! Do you want to fight it? [1 - Fight, 2 - Flee]: \n");
//         Player_Explore_Decision = Get_Player_Decision();
//     } while (Player_Explore_Decision != 1 && Player_Explore_Decision != 2);

//     return Player_Explore_Decision;
// }

// bool Check_For_Equal_Items(int Items) {
//     if (Items >= 3) { // Check for Full Hands - Too Heavy
//         printf("You try to fight the orc but your hands are full and are heavy. You fall down due to the heaviness and get sliced by the orc. Game Over! You lost! \n");
//         return false;

//     } else if (Items <= 1) { // Check for insufficient amount of items (Not enough items to defeat the orc)
//         printf("You try to fight the orc but you have an insufficient amount of items, which is not enough. You try to flee but trip on a rock and get sliced by the orc. Game Over! You Lost! \n");
//         return false;
//     }

//     return true;
// }

// bool Check_For_Needed_Items(bool Obtained_Fingernail_of_Doom, bool Obtained_Wall_of_Ice) {
//     if (Obtained_Fingernail_of_Doom == false || Obtained_Wall_of_Ice == false) {
//         return false;
//     }

//     return true;
// }

// int Check_For_Play_Again() {
//     int Play_Again_Decision = 0;

//     do {
//         printf("Want to play again? [1 - Yes, 2 - No]: ");
//         scanf("%d", &Play_Again_Decision);
//     } while (Play_Again_Decision != 1 && Play_Again_Decision != 2);

//     return Play_Again_Decision;
// }

// I just showed what Doggo what pointer is

// #include <stdio.h>

// int main() {
//     int x = 5;
//     int *alias_thingy;

//     alias_thingy = &x;
//     (*alias_thingy) = x;

//     printf("%d \n", x);
//     printf("%d \n", alias_thingy);
//     printf("%d \n", *alias_thingy);

//     return 0;
// }

// PROJECT FOR ADDING, SUBTRACTING, MULTIPLYING, AND DIVIDING FRACTIONS

// #include <stdio.h>

// int Get_Symbol();
// void Calculate_User_Input(int first_numerator, int first_denominator, int second_numerator, int second_denominator, int *Sum_Numerator, int *Sum_Denominator, int Arthimatic_Number);

// int main() {
//     int first_numerator, first_denominator, second_numerator, second_denominator, Sum_Numerator, Sum_Denominator;
//     int Arithmatic_Number;

//     Arithmatic_Number = Get_Symbol();

//     printf("Enter first fraction #/#: ");
//     scanf("%d/%d", &first_numerator, &first_denominator);

//     printf("Enter second fraction #/#: ");
//     scanf("%d/%d", &second_numerator, &second_denominator);

//     Calculate_User_Input(first_numerator, first_denominator, second_numerator, second_denominator, &Sum_Numerator, &Sum_Denominator, Arithmatic_Number);

//     printf("The answer is: %d/%d", Sum_Numerator, Sum_Denominator);

//     return 0;
// }

// int Get_Symbol() {
//     int Symbol_Number = 0;

//     do {
//         printf("1. + \n");
//         printf("2. - \n");
//         printf("3. * \n");
//         printf("4. / \n");

//         printf("Choose the arithmatic symbol: ");
//         scanf("%d", &Symbol_Number);
        
//     } while (Symbol_Number != 1 && Symbol_Number != 2 && Symbol_Number != 3 && Symbol_Number != 4);

//     return Symbol_Number;
// }

// void Calculate_User_Input(int first_numerator, int first_denominator, int second_numerator, int second_denominator, int *Sum_Numerator, int *Sum_Denominator, int Arthimatic_Number) {

//     switch (Arthimatic_Number) {
//         case 1:
//             (*Sum_Denominator) = first_denominator * second_denominator;

//             first_numerator = first_numerator * second_denominator;
//             second_numerator = second_numerator * first_denominator;

//             (*Sum_Numerator) = first_numerator + second_numerator;
//             break;

//         case 2:
//             (*Sum_Denominator) = first_denominator * second_denominator;

//             first_numerator = first_numerator * second_denominator;
//             second_numerator = second_numerator * first_denominator;

//             (*Sum_Numerator) = first_numerator - second_numerator;
//             break;

//         case 3:
//             (*Sum_Numerator) = first_numerator * second_numerator;
//             (*Sum_Denominator) = first_denominator * second_denominator;
//             break;

//         case 4:
//             (*Sum_Numerator) = first_numerator * second_denominator;
//             (*Sum_Denominator) = first_denominator * second_numerator;
//             break;

//         default:
//             break;
//     }
// }

// #include <stdio.h>

// #define SENTENCE_LENGTH 50

// int main() {
//     char phrase[SENTENCE_LENGTH], capitalArray[100], lowercaseArray[100], punctuationArray[100];

//     int i = 0, capitals = 0, lowercase = 0, punctuation = 0, choice;
//     printf("Please enter a Phrase: \n");
//     fgets(phrase, SENTENCE_LENGTH, stdin);

//     do {
//         capitals = 0;
//         lowercase = 0;
//         punctuation = 0;

//         for (i = 0; phrase[i] != '\0'; i++) {
            
//             if (phrase[i] >= 'A' && phrase[i] <= 'Z') {
//                 capitalArray[capitals] = phrase[i];
//                 capitals++;

//             } else if (phrase[i] >= 'a' && phrase[i] <= 'z') {
//                 lowercaseArray[lowercase] = phrase[i];
//                 lowercase++;

//             } else if (phrase[i] != ' ') {
//                 punctuationArray[punctuation] = phrase[i];
//                 punctuation++;
//             }
//         }

//         printf("1) Display %d capital letters. \n", capitals);
//         printf("2) Display %d lowercase letters. \n", lowercase);
//         printf("3) Display %d punctuation letters. \n", punctuation);
//         printf("0) Exit \n");
//         printf("Enter the type of character you want to display? \n");

//         if (choice == 1) {

//             printf("Capital letters. \n");

//             for (i = 0; i < capitals; i++) {
//                 printf("%c", capitalArray[i]);
//             }

//         } else if (choice == 2) {

//             printf("Lowercase letters. \n");
            
//             for (i = 0; i < lowercase; i++) {
//                 printf("%c", lowercaseArray[i]);
//             }

//         } else if (choice == 3) {

//             printf("Puncutation letters. \n");

//             for (i = 0; i < punctuation; i++) {
//                 printf("%c", punctuationArray[i]);

//             }

//         } else if (choice > 3) {
//             printf("Invalid answer, please try again! \n");
//         }

//         printf("\n");
//         scanf("%d", &choice);
//     } while (choice != 0);

    

//     return 0;
// }

// I tried to help Doggo with this project 9 homework but I failed miserably. I HAD to use AI for it and tried correlating it to his Project 5 homework. I'm sorry that I used Artificial Intelligence.

#include <stdio.h>

int maxLength = 500;

void Input_Phrase(char *phraseTable, FILE *Input_File);
void countCharacters(char *phraseTable, int *uppercase, int *lowercase, int *punctuations, char *uppercaseTable, char *lowercaseTable, char *punctuationTable);
void displayMenu(char *phraseTable, int uppercase, int lowercase, int punctations, char *uppercaseTable, char *lowercaseTable, char *punctuationTable);
void saveStats(char *phraseTable, int uppercase, int lowercase, int punctuations, FILE *statsFile);
void printPhrase_BasedonUserChoice(char *Table, int Size);

int main() {
    char phrase[maxLength];
    char uppercaseTable[maxLength];
    char lowercaseTable[maxLength];
    char punctuationTable[maxLength];

    int choice = -1;
    
    FILE *Story_File;
    
    Story_File = fopen("story.txt", "r");

    if (Story_File == NULL) {
        printf("Error while attempting to open the input file!");
        return -1;
    }
    
    Input_Phrase(phrase, Story_File);
    fclose(Story_File);
    
    int uppercase = 0, lowercase = 0, punctuation = 0;
    countCharacters(phrase, &uppercase, &lowercase, &punctuation, uppercaseTable, lowercaseTable, punctuationTable);
    
    do {
        printf("=== The Main Menu === \n");
        printf("Your Phrase: %s \n", phrase);
        printf("1. Display character counts \n");
        printf("2. Save character counts to stats.txt \n");
        printf("0. Exit \n");
        printf("Choice: ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1:
                displayMenu(phrase, uppercase, lowercase, punctuation, uppercaseTable, lowercaseTable, punctuationTable);
                break;
            
            case 2:
                FILE *Stats_File;
                Stats_File = fopen("stats.txt", "w");
    
                if (Stats_File == NULL) {
                    printf("Error while attempting to open the output file!");
                    return -1;
                } else {
                    saveStats(phrase, uppercase, lowercase, punctuation, Stats_File);
                    fclose(Stats_File);
                    printf("Successfully saved phrase to stats.txt \n");
                }
                
                break;
                
            case 0:
                printf("Goodbye! \n");
                break;
        }
    } while (choice != 0);
    
    return 0;
}

void Input_Phrase(char* phraseTable, FILE *Input_File) {
    printf("Enter a phrase: ");
    fgets(phraseTable, maxLength, Input_File);
}
void countCharacters(char *phraseTable, int *uppercase, int *lowercase, int *punctuations, char *uppercaseTable, char *lowercaseTable, char *punctuationTable) {
    
    for (int i = 0; phraseTable[i] != '\0' ; i++) {
        
        if (phraseTable[i] >= 'A' && phraseTable[i] <= 'Z') {
            (*uppercase)++;
            uppercaseTable[i] = phraseTable[i];
            
        } else if (phraseTable[i] >= 'a' && phraseTable[i] <= 'z') {
            (*lowercase)++;
            lowercaseTable[i] = phraseTable[i];
            
        } else if (phraseTable[i] != ' ') {
            (*punctuations)++;
            punctuationTable[i] = phraseTable[i];
        }
    }
}
void displayMenu(char *phraseTable, int uppercase, int lowercase, int punctuations, char *uppercaseTable, char *lowercaseTable, char *punctuationTable) {
    int choice;
    
    do {
        printf("=== Display Menu === \n");
        printf("1. Show uppercase count \n");
        printf("2. Show lowercase count \n");
        printf("3. Show punctuation count \n");
        printf("0. Exit \n");
        printf("Option: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                printf("Uppercases: %d \n", uppercase);
                printPhrase_BasedonUserChoice(uppercaseTable, sizeof(uppercaseTable)/sizeof(uppercaseTable[0]));
                break;
                
                case 2:
                    printf("Lowercases: %d \n", lowercase);
                    printPhrase_BasedonUserChoice(lowercaseTable, sizeof(lowercaseTable)/sizeof(lowercaseTable[0]));
                    break;
                    
                case 3:
                    printf("Punctuations: %d \n", punctuations);
                    printPhrase_BasedonUserChoice(punctuationTable, sizeof(punctuationTable)/sizeof(punctuationTable[0]));
                    break;
                    
                case 0:
                    printf("Goodbye! \n");
                    break;
                    
                default:
                    printf("Not an option. \n");
        }
    } while (choice != 0);
}
void saveStats(char *phraseTable, int uppercase, int lowercase, int punctuations, FILE *statsFile) {
    fprintf(statsFile, "Saved Phrase: %s \n", phraseTable);
    fprintf(statsFile, "Uppercase: %d, Lowercase: %d, Punctuations: %d \n", uppercase, lowercase, punctuations);
}

void printPhrase_BasedonUserChoice(char *Table, int Size) {
    for (int i = 0; i < Size; i++) {
        printf("%c ", Table[i]);
    }
}