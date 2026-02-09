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

# We can also enumerate through Numpy arrays using the ndenumerate() function

for i, element in np.ndenumerate(Three_Dimensional_Array):
    print(f"{element} at index {i}")

Number_Array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i, element in np.ndenumerate(Number_Array):
    print(f"{element} at {i}")

# You can also join Numpy Arrays

Yeetus = np.array([1, 2, 3, 4, 5])
Woah = np.array([6, 7, 8, 9, 10])

Woah = np.concatenate((Yeetus, Woah))
print(Woah)

Two_Dimensional_Array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

Another_Two_Dimensional_Array = np.array([
    [11, 12, 13, 14, 15], 
    [16, 17, 18, 19, 20]
])

print("----- Concatenate Axis 0 -----")
Concatenated_Array = np.concatenate((Two_Dimensional_Array, Another_Two_Dimensional_Array), axis=0)
print(Concatenated_Array)
print("--------------------")

print("----- Concatenate Axis 1 -----")
Concatenated_Array = np.concatenate((Two_Dimensional_Array, Another_Two_Dimensional_Array), axis=1)
print(Concatenated_Array)
print("--------------------")

Me_Stack = np.array([1, 2, 3])
Me_Also_Stack = np.array([4, 5, 6])
Me_Stack_Three = np.array([7, 8, 9])

print("----- Stacked Axis 0 -----")
Stacked_Array = np.stack((Me_Stack, Me_Also_Stack, Me_Stack_Three)) # Stacks arrays starting from the first array to the last array, axis=0 is default
print(Stacked_Array)
print("--------------------")

print("----- Stacked Axis 1 -----")
Stacked_Array = np.stack((Me_Stack, Me_Also_Stack, Me_Stack_Three), axis=1) # Stacks arrays VERTICALLY
print(Stacked_Array)
print("--------------------")

print("----- Horizontal Stack -----")
Horizontally_Stacked_Array = np.hstack((Me_Stack, Me_Also_Stack, Me_Stack_Three)) # Returns a list of all elements horizontally
print(Horizontally_Stacked_Array)
print("--------------------")

print("----- Vertical Stack -----")
Vertically_Stacked_Array = np.vstack((Me_Stack, Me_Also_Stack, Me_Stack_Three)) # Equivalent to np.stack()
print(Vertically_Stacked_Array)
print("--------------------")

print("----- Depth Stacked -----")
Depth_Stacked_Array = np.dstack((Me_Stack, Me_Also_Stack, Me_Stack_Three)) # Equivalent to Stacked Axis 1 or np.stack() with axis=1? (I don't know it looks like it added another dimension?)
print(Depth_Stacked_Array)
print("--------------------")

print("----- Splitting Array -----")
Even_More_Number_Array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Split_Array = np.array_split(Even_More_Number_Array, 3) # Split an array into the amount of arrays that you want
print(Split_Array)
print(Split_Array[0]) # Gets the first array of the many splitted arrays

More_Two_Dimensional_Array = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
Split_Two_Dimensions = np.array_split(More_Two_Dimensional_Array, 2, axis=0) # Normal split
print(Split_Two_Dimensions)

Split_Two_Dimensions = np.array_split(More_Two_Dimensional_Array, 2, axis=1) # Split corresponding elements in each array with the same index into columns
print(Split_Two_Dimensions)