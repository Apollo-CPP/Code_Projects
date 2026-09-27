/*
    Hey Michael Lin,
    I wrote this code with a good amount of help from Artificial Intelligence (I'm sorry):
    I had to use it for some things such as dealing with errors that I didn't know (segmentation fault) or some really confusing bugs
    I also had to use it for some improvements and debugging
    I tried using structs, namespaces, and good variable names to try to improve readability

    Can you teach me how to organize and clean my code for better optimization so it's more readable and less messy?
    Also I don't know how to do pointers, it's kind of confusing :(
    I'm REALLY obsessed with optimization, security, and memory and I just heard that pointers are used for memory management (to prevent memory leaks)
*/

#include <iostream>
#include <string>
#include <random>
#include <typeinfo>
#include <cctype>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <ctime>
#include <limits>
using namespace std;

struct Game_Configuration {
    int Ship_Rows;
    int Ship_Columns;
    static const int Max_Ships = 10;
    static const int Ship_Spawn_Chance = 300;

    static const int Min_Ship_Rows_and_Columns = 4;
    static const int Max_Ship_Rows_and_Columns = 9;

    static const int Min_Input = 0;
    int Max_Row_Input = 0;
    int Max_Column_Input = 0;
};

struct Game_State {
    int Hits = 0;
    int Misses = 0;
    int Turns_Left = 10;
    int Ships = 0;
    
    vector<vector<bool>> Potential_Ship_Locations;
    vector<vector<bool>> User_Guessed_Locations;
};

struct Player_Data {
    int Total_Hits = 0;
    int Total_Misses = 0;
};

namespace Special_Keywords {
    const string MENU_KEYWORD = "MENU";
    const string QUIT_KEYWORD = "QUIT";
    const string RESTART_KEYWORD = "RESTART";
    const string CONTINUE_KEYWORD = "CONTINUE";
    static const int Restart_Signal = -2;
}

namespace Game_Logic {
    bool Check_For_Prohibited_Characters(const string User_Input);
    bool Check_For_Non_Digits(const string User_Input);
    int Convert_User_Input_To_Integer(const string User_Input);
    bool Coordinate_In_Bounds(const int Coordinate_Value, const int Min_Number, const int Max_Number);
    int Input_Row_And_Column_Values(Game_State& Current_Game_State, Game_Configuration& Current_Game_Settings, Player_Data& Player_Stats, const string Prompt, const int Min_Number, const int Max_Number);
}

namespace Set_Up_Game {
    void Display_Introduction_And_Instructions(const Game_State& Current_Game_State, const Game_Configuration& Current_Game_Settings);
    void Display_End_Game_Stats(const Player_Data& Player_Stats);
    void Randomize_Ships(Game_State& Current_Game_State, const Game_Configuration& Current_Game_Settings);
    char Retrieve_Ship_Grid_Symbol(const bool Player_Guessed, const bool Is_A_Ship, const bool Show_Ships);
    void Print_Grid(const vector<vector<bool>>& Ship_Grid, const vector<vector<bool>>& Player_Guessed_Table, const Game_Configuration& Current_Game_Settings, const bool Show_Ships);
    void Check_For_Zero_Ships(const int Number_of_Ships);
}

namespace Special_Functions {
    string To_Upper(string Player_Decision_Input);
    void Reset_Game_Values(Game_State& Current_Game_State, Game_Configuration& Current_Game_Settings, Player_Data& Player_Stats);
    string Menu_Handler(Game_State& Current_Game_State, Game_Configuration& Current_Game_Settings, Player_Data& Player_Stats, string Prompt);
    void Display_Menu(const Game_State& Current_Game_State, const Player_Data& Player_Stats);
    bool Check_For_Non_Letters(const string Player_Player_Again_Decision);
}

bool Game_Logic::Check_For_Prohibited_Characters(const string User_Input) {
    for (char c : User_Input) {
        if (isspace(c) || ispunct(c)) { // No spaces or symbols
            return true;
        }
    }

    return false;
}

int Game_Logic::Convert_User_Input_To_Integer(const string User_Input) {
    try {
        const int Coordinate_Number = stoi(User_Input); // stoi (String to Integer) >> Try to convert the string to an integer
        return Coordinate_Number;
    } catch (...) {
        cout << "Error while attempting to convert Player's Input to an Integer!" << "\n"; // Debugging print statement incase anything goes wrong
        return -1;
    }
}

bool Game_Logic::Coordinate_In_Bounds(const int Coordinate_Value, const int Min_Number, const int Max_Number) {
    return Coordinate_Value >= Min_Number && Coordinate_Value <= Max_Number;
}

int Game_Logic::Input_Row_And_Column_Values(Game_State& Current_Game_State, Game_Configuration& Current_Game_Settings, Player_Data& Player_Stats, const string Prompt, const int Min_Number, const int Max_Number) {
    int Coordinate_Value;
    string User_Input;

    while (true) {
        cout << Prompt;
        getline(cin, User_Input);

        if (User_Input.empty()) {
            cout << "Your input is empty. Try Again." << "\n";
            continue;
        }

        if (Game_Logic::Check_For_Prohibited_Characters(User_Input)) {
            cout << "Your input contained prohibited characters (Spaces or Symbols). Try Again." << "\n";
            continue;
        }

        if (Special_Functions::To_Upper(User_Input) == Special_Keywords::MENU_KEYWORD) {
            string Player_Menu_Decision;

            Special_Functions::Display_Menu(Current_Game_State, Player_Stats);

            Player_Menu_Decision = Special_Functions::Menu_Handler(Current_Game_State, Current_Game_Settings, Player_Stats, "What would  you like to do?: ");

            if (Player_Menu_Decision == Special_Keywords::QUIT_KEYWORD) {
                exit(EXIT_SUCCESS);

            } else if (Player_Menu_Decision == Special_Keywords::RESTART_KEYWORD) {
                cout << "Successfully restarted game!" << "\n";
                return Special_Keywords::Restart_Signal;

            } else if (Player_Menu_Decision == Special_Keywords::CONTINUE_KEYWORD) {
                continue;
            }
        }

        if (Game_Logic::Check_For_Non_Digits(User_Input)) {
            cout << "Your input was not a digit or number. Try Again." << "\n";
            continue;
        }

        Coordinate_Value = Game_Logic::Convert_User_Input_To_Integer(User_Input);

        if (Coordinate_Value == -1) {
            cout << "Something wrong happened!" << "\n";
            continue;

        } else if (!(Game_Logic::Coordinate_In_Bounds(Coordinate_Value, Min_Number, Max_Number))) {
            cout << "Your input was out of bounds or not within in the range of " << Min_Number << " and " << Max_Number << ". Try Again." << "\n";
            continue;
        }

        return Coordinate_Value;
    }

    return 0;
}

bool Game_Logic::Check_For_Non_Digits(const string Set_Size_User_Input) {
    return !(all_of(Set_Size_User_Input.begin(), Set_Size_User_Input.end(), ::isdigit)); // Checks if every character is a digit
}

void Set_Up_Game::Display_Introduction_And_Instructions(const Game_State& Current_Game_State, const Game_Configuration& Current_Game_Settings) { // Displays the Introduction and Instructions to explain how to play
    cout << "----------------------------- Introduction ---------------------------" << "\n";
	cout << "Welcome to Battleship (C++)!" << "\n";
	cout << "Your goal is to locate the randomized ships using coordinates and blow them up." << "\n";
	cout << "There are a randomized amount of ships. The maximum amount of ships there can be is " << Current_Game_Settings.Max_Ships << "\n";
	cout << "Depending on the amount of ships there are, your turns will be increased by the amount of ships + 5 just in case there are a large number of ships." << "\n";
	cout << "It looks like there are " << Current_Game_State.Ships << " Ships for you to destroy." << "\n";
	cout << "You got " << Current_Game_State.Turns_Left << " Turns. Good Luck." << "\n";
	
	cout << "----------------------------- Input Rules -----------------------------" << "\n";
    cout << "1. Your input CANNOT contain any Spaces or Symbols. Only numbers / digits for inputting coordinates." << "\n";
	cout << "2. Your input CANNOT be empty." << "\n";
	cout << "3. Your input CANNOT just have spaces." << "\n";
    cout << "4. Your input can should be within the range of 0 - (Your Ship Grid Row or Column Size - 1), with 0 being the first Row / Column because C++ tables start with the index of 0." << "\n";
    cout << "5. If you want to quit the game then simply input Quit. You will confirm if you want to Quit or not. Y to exit the game and N to continue playing." << "\n";
	
	cout << "--------------------------- Ship Grid Keys ----------------------------" << "\n";
	cout << ". = Unknown" << "\n";
	cout << "O = Miss" << "\n";
	cout << "X = Hit" << "\n";
	cout << "\n";

    cout << "---------------------------- Special Inputs ---------------------------" << "\n";
    cout << "Menu - Open the Menu, view your stats, and have options to quit, restart, or continue" << "\n";
    cout << "Quit - Stop and Exit the game. You will confirm your choice by using [Y / N]" << "\n";
    cout << "Restart - You can restart the game during the game or play the game again at the end of the game in a [Y / N] format" << "\n";
    cout << "Continue - Continue playing the game" << "\n";
    cout << "\n";
    cout << "-----------------------------------------------------------------------" << "\n";
	
	cout << "Objective: Locate the ships and destroy them all." << "\n";
	cout << "-----------------------------------------------------------------------" << "\n";
}

void Set_Up_Game::Display_End_Game_Stats(const Player_Data& Player_Stats) {
    cout << "Game Over!" << "\n";

	cout << "--------------- End Game Stats ---------------" << "\n";
	cout << "Total Hits: " << Player_Stats.Total_Hits << "\n";
	cout << "Total Misses: " << Player_Stats.Total_Misses << "\n";

	cout << "Thank You For Playing Battleship (C++)" << "\n";
	cout << "- Created by Dylan Zhang" << "\n";
	cout << "\n";
}

void Set_Up_Game::Randomize_Ships(Game_State& Current_Game_State, const Game_Configuration& Current_Game_Settings) {
    auto& Game_Table = Current_Game_State.Potential_Ship_Locations;
    auto& Player_Guessed_Table = Current_Game_State.User_Guessed_Locations;
    srand(time(NULL));

    for (int Row = 0; Row < Current_Game_Settings.Ship_Rows; Row++) {
        for (int Column = 0; Column < Current_Game_Settings.Ship_Columns; Column++) {
            int Random_Chance = rand() % (Game_Configuration::Ship_Spawn_Chance) + 1;

            if (Current_Game_State.Ships >= Current_Game_Settings.Max_Ships) {
                break;
            }

            if (Random_Chance <= 50) {
                Game_Table[Row][Column] = true;
                Current_Game_State.Ships++;
                // cout << "Row is: " << Row << ", Column is: " << Column << "\n"; // Debugging Purposes
            }
        }
    }

    // Current_Game_State.Turns_Left = Current_Game_State.Ships + 5;
}

char Set_Up_Game::Retrieve_Ship_Grid_Symbol(const bool Player_Guessed, const bool Is_A_Ship, const bool Show_Ships) {
    if (Show_Ships == true && Is_A_Ship == true) {
        return 'X';
    }

    if (Player_Guessed == true) {
        if (Is_A_Ship == true) {
            return 'X';

        } else {
            return 'O';
        }
    } else {
        return '.';
    }
}

void Set_Up_Game::Print_Grid(const vector<vector<bool>>& Ship_Grid, const vector<vector<bool>>& Player_Guessed_Table, const Game_Configuration& Current_Game_Settings, const bool Show_Ships) {
    cout << "\n";

    if (Show_Ships == true) {
        cout << "- Answer Grid - " << "\n";
        cout << "  ";

    } else {
        cout << " - Ship Grid - " << "\n";
        cout << "  ";
    }

    for (int Column = 0; Column < Current_Game_Settings.Ship_Columns; Column++) {
        cout << Column << " ";
    }

    cout << "\n";

    for (int Row = 0; Row < Current_Game_Settings.Ship_Rows; Row++) {
        cout << Row << " ";
        
        for (int Column = 0; Column < Current_Game_Settings.Ship_Columns; Column++) {
            
            char Ship_Grid_Symbol = Set_Up_Game::Retrieve_Ship_Grid_Symbol(Player_Guessed_Table[Row][Column], Ship_Grid[Row][Column], Show_Ships);
            cout << Ship_Grid_Symbol << " ";
        }

        cout << "\n";
    }

    cout << "\n";
}

void Set_Up_Game::Check_For_Zero_Ships(const int Number_of_Ships) {
    if (Number_of_Ships <= 0) {
        cout << "How Unlucky! The randomizer has returned 0 ships for you to destroy. The game will now be exited." << "\n";
        exit(EXIT_SUCCESS);
    }
}

string Special_Functions::To_Upper(string Player_Decision_Input) {
    transform(Player_Decision_Input.begin(), Player_Decision_Input.end(), Player_Decision_Input.begin(), ::toupper);
    return Player_Decision_Input;
}

void Special_Functions::Reset_Game_Values(Game_State& Current_Game_State, Game_Configuration& Current_Game_Settings, Player_Data& Player_Stats) {
    auto& Game_Array = Current_Game_State.Potential_Ship_Locations;
    auto& Player_Guessed_Array = Current_Game_State.User_Guessed_Locations;

    Current_Game_State.Hits = 0;
    Current_Game_State.Misses = 0;
    Current_Game_State.Turns_Left = 0;
    Current_Game_State.Ships = 0;

    Current_Game_Settings.Ship_Rows = 0;
    Current_Game_Settings.Ship_Columns = 0;

    Current_Game_Settings.Max_Row_Input = 0;
    Current_Game_Settings.Max_Column_Input = 0;

    if (Game_Array.empty() || Player_Guessed_Array.empty()) {
        return;   
    }

    Game_Array.clear();
    Player_Guessed_Array.clear();

    Game_Array.resize(0);
    Player_Guessed_Array.resize(0);

    Game_Array.shrink_to_fit();
    Player_Guessed_Array.shrink_to_fit();
}

string Special_Functions::Menu_Handler(Game_State& Current_Game_State, Game_Configuration& Current_Game_Settings, Player_Data& Player_Stats, const string Prompt) {
    string Player_Menu_Decision;

    while (true) {
        cout << "What would you like to do?: ";
        getline(cin, Player_Menu_Decision);

        if ((Special_Functions::To_Upper(Player_Menu_Decision) != Special_Keywords::QUIT_KEYWORD) && (Special_Functions::To_Upper(Player_Menu_Decision) != Special_Keywords::RESTART_KEYWORD) && (Special_Functions::To_Upper(Player_Menu_Decision) != Special_Keywords::CONTINUE_KEYWORD)) {
            continue;
        }

        if (Special_Functions::To_Upper(Player_Menu_Decision) == Special_Keywords::QUIT_KEYWORD) {
            string Player_Quit_Decision;

            do {
                cout << "Are you sure you want to quit? [Y / N]: ";
                getline(cin, Player_Quit_Decision);
            } while ((Special_Functions::To_Upper(Player_Quit_Decision) != "Y") && (Special_Functions::To_Upper(Player_Quit_Decision) != "N"));

            if (Player_Quit_Decision == "Y") {
                cout << "Quitting Game..." << "\n";

                if (Current_Game_State.Potential_Ship_Locations.size() <= 0) {
                    return Special_Keywords::QUIT_KEYWORD;

                } else {
                    Set_Up_Game::Print_Grid(Current_Game_State.Potential_Ship_Locations, Current_Game_State.User_Guessed_Locations, Current_Game_Settings, true);
                    Set_Up_Game::Display_End_Game_Stats(Player_Stats);

                    cout << "Successfully quit game!" << "\n";
                    return Special_Keywords::QUIT_KEYWORD;
                }

            } else if (Player_Quit_Decision == "N") {
                continue;
            }


        } else if (Special_Functions::To_Upper(Player_Menu_Decision) == Special_Keywords::RESTART_KEYWORD) {
            string Player_Restart_Decision;

            do {
                cout << "Are you sure you want to restart? [Y / N]: ";
                getline(cin, Player_Restart_Decision);
            } while ((Special_Functions::To_Upper(Player_Restart_Decision) != "Y") && (Special_Functions::To_Upper(Player_Restart_Decision) != "N"));

            if (Player_Restart_Decision == "Y") {
                cout << "Restarting Game..." << "\n";

                if (Current_Game_State.Potential_Ship_Locations.size() <= 0) {
                    cout << "Restarted Game!" << "\n";
                    return Special_Keywords::RESTART_KEYWORD;

                } else {
                    Set_Up_Game::Print_Grid(Current_Game_State.Potential_Ship_Locations, Current_Game_State.User_Guessed_Locations, Current_Game_Settings, true);
                    Special_Functions::Reset_Game_Values(Current_Game_State, Current_Game_Settings, Player_Stats);
                    cout << "Restarted Game!" << "\n";

                    return Special_Keywords::RESTART_KEYWORD;
                }

            } else if (Player_Restart_Decision == "N") {
                continue;
            }
            
        } else if (Special_Functions::To_Upper(Player_Menu_Decision) == Special_Keywords::CONTINUE_KEYWORD) {
            cout << "Continuing Game!" << "\n";
            return Special_Keywords::CONTINUE_KEYWORD;
        }
    }
}

void Special_Functions::Display_Menu(const Game_State& Current_Game_State, const Player_Data& Player_Stats) {
    cout << "--------------------" << "\n";
    cout << "        Menu        " << "\n";
    cout << "--------------------" << "\n";
    cout << "\n";

    cout << " ------ Stats ------" << "\n";
    cout << "Total Hits: " << Player_Stats.Total_Hits << "\n";
    cout << "Total Misses: " << Player_Stats.Total_Misses << "\n";
    cout << "Turns Left: " << Current_Game_State.Turns_Left << "\n";
    cout << "Ships Left: " << Current_Game_State.Ships << "\n";
    cout << "\n";

    cout << " ----- Options -----" << "\n";
    cout << "> 1. Quit" << "\n";
    cout << "> 2. Restart" << "\n";
    cout << "> 3. Continue Playing" << "\n";
    cout << "--------------------" << "\n";
    cout << "\n";
}

bool Special_Functions::Check_For_Non_Letters(const string Player_Play_Again_Decision) {
    for (char c : Player_Play_Again_Decision) {
        if (!(isalpha(c))) {
            return true;
        }
    }

    return false;
}

void Play_BattleShip_Game() {
    Player_Data Player_Stats;
    Game_State Current_Game_State;
    Game_Configuration Game_Settings;

    vector<vector<bool>>& Ship_Table = Current_Game_State.Potential_Ship_Locations;
    vector<vector<bool>>& Player_Guessed_Table = Current_Game_State.User_Guessed_Locations;

    while (true) {
        cout << "Enter the amount of Rows and Colums (Min: " << Game_Settings.Min_Ship_Rows_and_Columns << ", Max: " << Game_Settings.Max_Ship_Rows_and_Columns << ")" << "\n";

        Game_Settings.Ship_Rows = Game_Logic::Input_Row_And_Column_Values(Current_Game_State, Game_Settings, Player_Stats, "Enter the amount of Rows: ", Game_Settings.Min_Ship_Rows_and_Columns, Game_Settings.Max_Ship_Rows_and_Columns);

        if (Game_Settings.Ship_Rows == Special_Keywords::Restart_Signal) {
            continue;
        }

        Game_Settings.Ship_Columns = Game_Logic::Input_Row_And_Column_Values(Current_Game_State, Game_Settings, Player_Stats, "Enter the amount of Columns: ", Game_Settings.Min_Ship_Rows_and_Columns, Game_Settings.Max_Ship_Rows_and_Columns);

        if (Game_Settings.Ship_Columns == Special_Keywords::Restart_Signal) {
            continue;
        }

        Ship_Table.resize(Game_Settings.Ship_Rows, vector<bool>(Game_Settings.Ship_Columns, false));
        Player_Guessed_Table.resize(Game_Settings.Ship_Rows, vector<bool>(Game_Settings.Ship_Columns, false));

        Game_Settings.Max_Row_Input = Game_Settings.Ship_Rows - 1;
        Game_Settings.Max_Column_Input = Game_Settings.Ship_Columns - 1;

        Set_Up_Game::Randomize_Ships(Current_Game_State, Game_Settings);
        Set_Up_Game::Display_Introduction_And_Instructions(Current_Game_State, Game_Settings);
        Set_Up_Game::Print_Grid(Ship_Table, Player_Guessed_Table, Game_Settings, false);

        Set_Up_Game::Check_For_Zero_Ships(Current_Game_State.Ships);

        while (true) {
            int Row, Column;

            Row = Game_Logic::Input_Row_And_Column_Values(Current_Game_State, Game_Settings, Player_Stats, "Enter a Row: ", Game_Settings.Min_Input, Game_Settings.Max_Row_Input);

            if (Row == Special_Keywords::Restart_Signal) {
                break;
            }

            Column = Game_Logic::Input_Row_And_Column_Values(Current_Game_State, Game_Settings, Player_Stats, "Enter a Column: ", Game_Settings.Min_Input, Game_Settings.Max_Column_Input);

            if (Column == Special_Keywords::Restart_Signal) {
                break;
            }

            if (Player_Guessed_Table[Row][Column] == true) {
                cout << "You have already guessed (" << Row << ", " << Column << "). Try Again." << "\n";
                continue;
            }

            Current_Game_State.Turns_Left--;
            Player_Guessed_Table[Row][Column] = true;

            if (Ship_Table[Row][Column] == true) {
                Player_Stats.Total_Hits++;
                Current_Game_State.Hits++;
                cout << "You have hit a ship!" << "\n";

            } else {
                Player_Stats.Total_Misses++;
                cout << "You have missed!" << "\n";
            }

            Set_Up_Game::Print_Grid(Ship_Table, Player_Guessed_Table, Game_Settings, false);

            if (Current_Game_State.Hits >= Current_Game_State.Ships) {
                cout << "You have destroyed every ship! You win!" << "\n";
                break;

            } else if (Current_Game_State.Turns_Left <= 0) {
                cout << "You have ran out of turns!" << "\n";
                break;

            } else {
                cout << "You have " << Current_Game_State.Turns_Left << " turns left!" << "\n";
            }
        }

        break;
    }

    Set_Up_Game::Print_Grid(Ship_Table, Player_Guessed_Table, Game_Settings, true);
    Set_Up_Game::Display_End_Game_Stats(Player_Stats);
}

int main() {
    string Player_Play_Again_Decision;

    do {
        Play_BattleShip_Game();

        do {
            cout << "Would you like to play again? [Y / N]: ";
            getline(cin, Player_Play_Again_Decision);
        } while ((Special_Functions::To_Upper(Player_Play_Again_Decision) != "Y") && (Special_Functions::To_Upper(Player_Play_Again_Decision) != "N"));


    } while (Player_Play_Again_Decision == "Y");

    return 0;
}