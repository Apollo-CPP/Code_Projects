import numpy as np

My_Array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(My_Array.dtype) # Short for data type, will print the array's data type

Data_Type_Array = np.array([34, 6, 23, 34], dtype="int") # You can have an optional key word argument "dtype"
print(Data_Type_Array.dtype)

# Error_Data_Type_Array = np.array(["ooga booga", "maaaaaa", "ofoffooffofoo", "??"], dtype="i") # If an array can't be converted into a certain data type then Python will raise a ValueError

# You can use the astype() function, which returns a new array that has been converted to a new datatype

# New_Array = My_Array.astype(My_Array, 'f')
# print(New_Array.dtype)

Convert_To_Bool = np.array([1, 0, 3])
Me_Convert_Bool = Convert_To_Bool.astype(bool)
print(Me_Convert_Bool)

My_Copy = My_Array.copy()
My_View = My_Array.view()

My_View[0] = 593
print(My_Array) # View affects original array

Three_Dimensional_Array = np.array([
    
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    
    [
        ["!", "@", "#"],
        ["$", "%", "^"],
        ["&", "*", "("]
    ],
    
    [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ]
    
])
print(Three_Dimensional_Array.shape) # (3, 3, 3) - First layer, Second Layer, and Third layer with the amount of elements each layers hold
# The amount of numbers displayed is the amount of dimensions

Reshape_Me_Array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Reshaped_2D_Array = Reshape_Me_Array.reshape(2, 5) # Reshapes an array - (x, y) - x is the amount of more arrays you want to create and y is the amount of elements are in x array
print(Reshaped_2D_Array)
# Example: (2, 5) - Create 2 separate arrays with 5 elements in each array

Reshape_Again = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
Reshaped_Into_3D = Reshape_Again.reshape(2, 3, 2) # One array with 12 elements --> Two arrays with 6 elements, --> 3 Arrays in the Two arrays with 2 elements, basically dividing the elements into more arrays for more dimensions
print(Reshaped_Into_3D)
print(Reshaped_Into_3D.base) # Returned the original array so it returned a view?

Another_Array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# Another_Array.reshape(3, 4) # You can't just reshape an array with any size because the amount of elements needs to match the reshaping or else Python will raise a ValueError

Unknown_Reshaping = Another_Array.reshape(3, -1) # Let's just say you don't know how many elements are going to be in an array, put -1 and NumPy will calculate it for you, but you can't pass -1 in more than one dimensions
print(Unknown_Reshaping)

# You can also "flatten" an array, basically just means converting an array to a 1D Array
Flattened_Array = Three_Dimensional_Array.reshape(-1) # Just pass in -1 in the reshape() function to flatten an array
print(Flattened_Array)

# To loop through a NumPy array, you can simply use a for loop. However, NumPy array has dimensions so it can be extremely tedious and inefficient

for x in Three_Dimensional_Array:
    for y in x:
        for z in y:
            if z == Three_Dimensional_Array[-1, -1, -1]:
                print(z)
            else:
                print(z, end=" ")

# To solve this, we can use the NumPy's nditer() function, which returns every element in the array so we don't have to write many for loops
for element in np.nditer(Three_Dimensional_Array):
    if element == Three_Dimensional_Array[-1, -1, -1]:
        print(element)
    else:
        print(element, end=" ")
        
# I guess you can change the data types while iterating through the array?

Convert_Array_pls = np.array([1, 2, 3, 4, 5])

for element in np.nditer(Convert_Array_pls, flags=["buffered"], op_dtypes=["S"]):
    print(element, end=" ")
    
print()


# Slice while printing
Slicing_Loop_Array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

for element in np.nditer(Slicing_Loop_Array[1::2, ::2]):
    print(element, end=" ")
    
print()