// // This is my file for practicing pointers and memory management!

// // #include <iostream>
// // #include <string>
// // #include <array>
// // #include <vector>
// // using namespace std;

// // string This_Array[] = {"Hello", "World", "Yes", "No"}; // Apparently arrays automatically decay into their memory address form already
// // string *pThis_Array = This_Array;

// // struct House_Example {
// //   int Bathrooms;
// //   int Bedrooms;
// //   int Square_Feet;  
// // };

// // int Get_House_Price(House_Example House) { // This makes a new copy
// //     return ((House.Bathrooms * 5000) + (House.Bedrooms * 10000) + (House.Square_Feet * 1000));
// // }

// // int Get_House_Price_Pointer(House_Example * pHouse) { // Pass by reference
// //     return ((pHouse -> Bathrooms * 5000) + (pHouse -> Bedrooms * 10000) + (pHouse -> Square_Feet * 1000));
// // }

// // // Get_House_Price_Pointer Analogy: Instead of getting your house to the appraiser, the appraiser comes to your house
// // // Void Pointers return just the memory address of a variable

// // int add_numbers(int a, int b) { // Original / Base function for the pointer add function
// //     return a + b;
// // }

// // int (*Add_Numbers_Pointer)(int, int) = add_numbers; // Declare the pointer function
// // // function type(*Pointer_Function_Name)(parameter types) = (the original / base function)

// // int main() {
// //     vector<vector<bool>> *Vector_Pointer = new vector<vector<bool>>;
// //     cout << Vector_Pointer << endl;

// //     (*Vector_Pointer).resize(4, vector<bool>(4, false)); // Dereference pointer (turning it back to its original form of the vector array) then resizing it

// //     for (int i = 0; i < 4; i++) {
// //         for (int j = 0; j < 4; j++) {
// //             cout << (*Vector_Pointer)[i][j] << " ";
// //         }

// //         cout << "\n";
// //     }

// //     (*Vector_Pointer).clear();
// //     (*Vector_Pointer).resize(0);
// //     (*Vector_Pointer).shrink_to_fit();

// //     Vector_Pointer->resize(2, vector<bool>(5, true)); // This is also another way of dereferencing a pointer

// //     for (int i = 0; i < 2; i++) {
// //         for (int j = 0; j < 5; j++) {
// //             cout << (*Vector_Pointer)[i][j] << " ";
// //         }

// //         cout << "\n";
// //     }

// //     Vector_Pointer->clear(); // Set everything to 0
// //     Vector_Pointer->resize(0);
// //     Vector_Pointer->shrink_to_fit(); // Make sure it is 0

// //     delete Vector_Pointer; // Delete the pointer
// //     cout << Vector_Pointer << endl;

// //     Vector_Pointer = nullptr; // Declare as a null pointer, pointing to absolutely nothing
// //     cout << Vector_Pointer << endl;

// //     auto* My_Auto_2D_Vector_Array_Pointer = new vector<vector<bool>>(3, vector<bool>(3, true)); // Apparently auto is equivalent to the line below it, it just "deduces" the type
// //     // It figures out the type and automatically converts the type to it
// //     // auto = vector<vector<bool>>
// //     vector<vector<bool>>* My_Regular_2D_Vector_Array_Pointer = new vector<vector<bool>>(4, vector<bool>(4, false));

// //     House_Example House;
// //     House_Example *pHouse;

// //     House.Bathrooms = 3; // Refer to a struct variable using dot operator if it's normal
// //     House.Bedrooms = 3;
// //     House.Square_Feet = 2100;

// //     pHouse->Bathrooms = 2; // If it's a pointer then use the -> operator to tell the compiler that we're using a pointer
// //     pHouse->Bedrooms = 2;
// //     pHouse->Square_Feet = 2400;

// //     cout << House.Bathrooms << "\n";
// //     cout << House.Bedrooms << "\n";
// //     cout << House.Square_Feet << "\n";

// //     cout << pHouse->Bathrooms << "\n";
// //     cout << pHouse->Bedrooms << "\n";
// //     cout << pHouse->Square_Feet << "\n";

// //     int *x, y; // Declares one pointer and one integer, NOT two pointers

// //     cout << x;
// //     cout << y;

// //     cout << sizeof(string) << endl; // Size of the string type and it outputs 32

// //     cout << This_Array << endl; // Since arrays decay into their memory address form when printed, these print statements will print the same thing
// //     cout << pThis_Array << endl;

// //     cout << sizeof(This_Array) << endl; // Prints the size of the array's memory address size (128) - Size of Array * The Elements Type (5 * 32) - Memory Bytes
// //     cout << sizeof(pThis_Array) << endl; // Prints memory bytes depending on your system (32-bit or 64-bit)

// //     // Pointer Arithmetic

// //     cout << sizeof(int) << "\n"; // Gets the size of an integer (varying depending if you have a 32-bit or 64-bit system) but for me it is 4 bytes

// //     int These_Numbers[] = { 1, 2, 3, 4, 5 };
// //     int *pThese_Numbers = These_Numbers;

// //     cout << pThese_Numbers << "\n";

// //     pThese_Numbers++; // Adds four bytes because the size of an int is 4 bytes
// //     cout << pThese_Numbers << "\n";

// //     pThese_Numbers += 5; // This will add 20 bytes because it adds 4 bytes each time it is incremented (5 * (size of integer type or 4 for me))
// //     cout << pThese_Numbers << "\n"; // Nevermind, I have no clue what happened? It's not adding up correctly

// //     // Character Pointers?
// //     const char *p = "Hello, World!";
// //     cout << p << "\n";
// //     const char **p1 = &p; // Apparently pointers can point to other pointers?

// //     cout << p1 << endl; // Prints the memory address of p1
// //     cout << *p1 << endl; // Prints the actual value of p1 or p since p1 is a reference to p

// //     // Uninitialized pointers and null pointers

// //     int *p_Uninitialized_Pointer;
// //     int *Null_Pointer = nullptr;

// //     cout << p_Uninitialized_Pointer << "\n"; // Prints memory address of this Uninitialized Pointer
// //     cout << Null_Pointer << "\n"; // It printed 0, according to the video null pointers are defaulted to be set to 0 so I'll just assume it'll be 0 when printing null pointers

// //     cout << *p_Uninitialized_Pointer << endl; // I got a segmentation fault on this line, apparently you can't dereference and print Uninitialized pointers
// //     cout << *Null_Pointer << endl; // I also got a segmentation fault on this line, you can't dereference and print Null Pointers

// //     int First_Number = 5;
// //     int Second_Number = 45;

// //     int Sum = (*Add_Numbers_Pointer)(First_Number, Second_Number); // Use add number pointer function to add these numbers
// //     cout << Sum;

// //     int* This_Number = new int;
// //     *This_Number = 5;

// //     cout << This_Number << endl;
// //     cout << *This_Number << endl;
// //     delete This_Number;

// //     cout << This_Number << endl;

// //     This_Number = nullptr;
// //     cout << This_Number << endl;

// //     int Random_Thing = 5;
// //     int *skibidi = &Random_Thing;

// //     cout << skibidi << endl; // Prints memory address
// //     cout << *skibidi << endl; // Dereference pointer and print the "contents" of the variable

// //     return 0;
// // }

// #include <iostream>
// #include <string>
// #include <memory>
// #include <string>
// #include <limits>
// #include <cctype>

// class Vehicle {
//     public:
//         int Price;
//         int Speed;
//         int Wheels;
//         bool Owned = false;
//         std::string Status;

//         void Purchase_Vehicle(int& Player_Money, bool& Vehicle_Ownership) {
//             std::string Purchase_Decision;

//             do {
//                 std::cout << "Are you sure you want to buy this vehicle? [Y / N]: ";
//                 std::getline(std::cin, Purchase_Decision);
//             } while (Purchase_Decision != "Y" && Purchase_Decision != "y" && Purchase_Decision != "N" && Purchase_Decision != "n");

//             if (Purchase_Decision == "N" || Purchase_Decision == "n") {
//                 std::cout << "Not buying car!" << std::endl;
//                 return;
//             }

//             if (Player_Money < Price) {
//                 std::cout << "Not enough money! You have " << Player_Money << ", the price is " << Price << ", and you need " << (Player_Money - Price) << " more!" << std::endl;

//             } else {
//                 std::cout << "Successfully purchased car!" << std::endl;
//                 Player_Money -= Price;
//                 Vehicle_Ownership = true;
//             }
//         }

//         void Print_Vehicle_Properties(const int& Price, const int& Speed, const int& Wheels, const bool& Owned) {
//             std::cout << "Price: " << Price << std::endl;
//             std::cout << "Maximum Speed: " << Speed << std::endl;
//             std::cout << "Wheels: " << Wheels << std::endl;
//             std::cout << "Owned: " << Owned << std::endl;
//         }
// };

// class Car : public Vehicle {
//     public:
//         int Price = 70000;
//         int Wheels = 4;
//         int Speed = 80;
//         bool Owned = false;
//         std::string Status;

//         void Start_Car() {
//             if (Owned == false) {
//                 return;
//             }

//             std::cout << "The car has started!" << std::endl;
//             Status = "Started";
//         }

//         void Stop_Car() {
//             if (Owned == false) {
//                 return;
//             }

//             std::cout << "The car has stopped!" << std::endl;
//             Status = "Stopped";
//         }

//         void Honk() {
//             if (Owned == false) {
//                 return;
//             }

//             std::cout << "Honk Honk!" << std::endl;
//         }
// };

// class Bike : public Vehicle {
//     public:
//         int Price = 250;
//         int Wheels = 2;
//         int Speed = 10;
//         bool Owned = false;
//         std::string Status;

//     void Ride_Bike() {
//         if (Owned == false) {
//             return;
//         }

//         std::cout << "Riding Bike!" << std::endl;
//         Status = "Riding";
//     }

//     void Stop_Bike() {
//         if (Owned == false) {
//             return;
//         }

//         std::cout << "Bike has stopped!" << std::endl;
//         Status = "Stopped";
//     }

//     void Ring_Bell() {
//         if (Owned == false) {
//             return;
//         }
        
//         std::cout << "Ring Ring!" << std::endl;
//     }
// };

// int main() {
//     auto Vehicle_Unique_Pointer = std::make_unique<Vehicle>();
//     auto Car_Unique_Pointer = std::make_unique<Car>();
//     auto Bike_Unique_Pointer = std::make_unique<Bike>();

//     int Cash {};

//     while (true) {
//         std::string Cash_String;
//         std::cout << "How much money do you start with?: ";
//         std::getline(std::cin, Cash_String);

//         auto Contains_Digits = [](const std::string& s) {
//             for (char c : s) {
//                 if (!std::isdigit(c)) {
//                     return true;
//                 }
//             }

//             return false;
//         };

//         if (Cash_String.empty() || Contains_Digits(Cash_String) == true) {
//             std::cout << "Invalid Input. Try Again." << std::endl;
//             continue;
//         }

//         try {
//             Cash = std::stoi(Cash_String);
//             break;

//         } catch (...) {
//             std::cerr << "Something went wrong while trying to convert Cash_String to an int!" << std::endl;
//         }
//     }
    
//     while (true) {
//         std::string Item;
        
//         do {
//             std::cout << "Welcome to the Car Dealership! What Vehicle would you like to buy? [Car / Bike]: ";
//             std::getline(std::cin, Item);

//             if (std::cin.fail()) {
//                 std::cin.clear();
//                 std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
//             }

//         } while ((Item != "Car" && Item != "Bike") || std::cin.fail());

//         if (Item == "Car") {
//             std::string Buy_Decision;

//             Car_Unique_Pointer->Print_Vehicle_Properties(Car_Unique_Pointer->Price, Car_Unique_Pointer->Speed, Car_Unique_Pointer->Wheels, Car_Unique_Pointer->Owned);

//             do {
//                 std::cout << "Would you like to purchase this car for " << Car_Unique_Pointer->Price << "? [Y / N]: ";
//                 std::getline(std::cin, Buy_Decision);
//             } while (Buy_Decision != "Y" && Buy_Decision != "N");

//             if (Buy_Decision == "Y") {
//                 Vehicle_Unique_Pointer->Purchase_Vehicle(Cash, Car_Unique_Pointer->Owned);

//             } else {
//                 std::cout << "Returning back to shop!" << std::endl;
//             }
//         }
//     }

//     return 0;
// }

// #include <iostream>

// void Add_Numbers_Reference(int& a, int& b, int& answer) {
//     answer = a + b;   
// }

// int Add_Numbers_Pointers(int *a, int *b) {
//     return (*a) + (*b);
// }

// int Add_All_Numbers_In_Table(const int *Table, const int Size) { // Must declare Raw C-Style arrays with a pointer because they automatically decay into pointers
//     int Answer = 0;

//     for (int i = 0; i < Size; i++) {
//         Answer += Table[i];
//     }

//     return Answer;
// }

// int main() {
//     int *first_a = new int; // Must point to something so declare as a variable with a type
//     int *first_b = new int;
//     int *first_answer = new int;

//     // int *first_a, *first_b, *first_answer; // Put asterisk on all variables so the compiler knows that all variables are all pointers
//     // Ignore line 385 comment, the pointer's memory address pointed to absolutely nothing

//     int second_a, second_b, second_answer;
    
//     int My_Table[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
//     int Size = sizeof(My_Table)/sizeof(My_Table[0]);
    
//     std::cout << "Value of A: ";
//     std::cin >> (*first_a); // First, it dereferences the pointer back into its integer form and then the std::cin is able to insert a value into the integer form not the pointer form

//     std::cout << "Value of B: ";
//     std::cin >> (*first_b);

//     (*first_answer) = Add_Numbers_Pointers(first_a, first_b);
//     std::cout << (*first_answer) << std::endl;

//     std::cout << "Value of A: ";
//     std::cin >> second_a;

//     std::cout << "Value of B: ";
//     std::cin >> second_b;

//     Add_Numbers_Reference(second_a, second_b, second_answer); // Pass the answer as it is passing by reference so it modifies the ORIGINAL copy and doesn't make a new one. You also don't have to say second_answer = ... but just call the function
//     std::cout << second_answer << std::endl;

//     const int Answer = Add_All_Numbers_In_Table(My_Table, Size);
//     std::cout << Answer << std::endl;

//     std::string *Something_lol = new std::string;
//     (*Something_lol) = "Hello!";

//     std::cout << Something_lol->length() << std::endl; // Can also use the arrow -> without dereferencing the variable (*variable).length() to variable->length()

//     delete first_a; // Make sure  the delete the pointers so the are cleaned up and don't ause a memory leak
//     delete first_b;
//     delete first_answer;

//     first_a = nullptr; // Ensure setting them to null pointers so that they aren't dangling in memory
//     first_b = nullptr;
//     first_answer = nullptr;

//     return 0;
// }