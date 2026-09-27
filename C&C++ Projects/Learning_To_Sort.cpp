#include <iostream>
#include <vector>

void Print_Table(const auto* Array, const int Size) {
    for (int i = 0; i < Size; i++) {
        std::cout << Array[i] << " ";
    }

    std::cout << "\n";
}

void Print_Array(const auto& Vector_Array) {
    for (const auto& Element : Vector_Array) {
        std::cout << Element << " ";
    }

    std::cout << "\n";
}

int main() {
    std::string My_Table[] = {"o", "a", "c", "y", "z"};
    int Size = sizeof(My_Table)/sizeof(My_Table[0]);

    std::vector<int> My_Int_Array = {56, 23, 878, 34, 67, 456, 34, 19, 95, -34, 569, -293, 85, -45};

    // Bubble sorting where the largest value (right) floats to the top and lowest value (left) sinks to the bottom
    std::string temp;

    for (int i = 0; i < Size - 1; i++) { // Repeat the inner loop
        Print_Table(My_Table, Size);

        std::cout << "\n";

        for (int j = 0; j < Size - i - 1; j++) { // Swaps values in the entire array once
            if (My_Table[j] > My_Table[j + 1]) { // If value is larger than the next value then swap that value
                temp = My_Table[j]; // Store smaller value in temp

                My_Table[j] = My_Table[j + 1]; // Swap big with smaller value position
                My_Table[j + 1] = temp; // Smaller value is now at larger value's position
            }
        }
    }

    Print_Array(My_Int_Array); // Before

    std::sort(My_Int_Array.begin(), My_Int_Array.end()); // Or just be lazy and use C++ array features to sort the array instead (Abstraction)

    Print_Array(My_Int_Array); // After (Sorted)

    return 0;
}