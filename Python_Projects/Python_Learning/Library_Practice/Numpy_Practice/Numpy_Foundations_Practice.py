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

print("----- Normal Array Splitting -----")
Even_More_Number_Array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Split_Array = np.array_split(Even_More_Number_Array, 3) # Split an array into the amount of arrays that you want
print(Split_Array)
print(Split_Array[0]) # Gets the first array of the many splitted arrays
print("--------------------")

print("----- 2D Array Splitting Axis = 0 -----")
More_Two_Dimensional_Array = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
Split_Two_Dimensions = np.array_split(More_Two_Dimensional_Array, 2, axis=0) # Normal split
print(Split_Two_Dimensions)
print("--------------------")

print("----- 2D Array Splitting Axis = 1")
Split_Two_Dimensions = np.array_split(More_Two_Dimensional_Array, 2, axis=1) # Split corresponding elements in each array with the same index into columns
print(Split_Two_Dimensions)
print("--------------------")

print("----- Horizontal Split -----")
Split_Two_Dimensions = np.hsplit(More_Two_Dimensional_Array, 2) # Equivalent to normal splitting with axis=1
print(Split_Two_Dimensions)
print("--------------------")

print("----- Vertical Splitting -----")
Split_Two_Dimensions = np.vsplit(More_Two_Dimensional_Array, 2) # Equivalent to normal splitting with axis=0
print(Split_Two_Dimensions)
print("--------------------")

print("----- Searching in Numpy Arrays -----")
Random_Idk_Array = np.array([1, "yeet", True, "hmm", False, 56, "meh"])
print(np.where(Random_Idk_Array == "hmm")) # The np.where() function returns a Numpy array with the index of the value
print("--------------------")

print("----- Finding an even number by searching -----")
yeah_lot_numbers = np.array([56, 2, 8, 3, 78, 45, 213, 784])
print(np.where(yeah_lot_numbers % 2 == 0)) # Find equally divisible numbers - Even
print(np.where(yeah_lot_numbers % 2 == 1)) # Find all odd numbers
print("--------------------")

print("----- Searching through sorted arrays? -----")
actually_sorted = np.array([10, 15, 20, 25, 30, 35, 40])
not_sorted = np.array([5, 16, 8, 45, 23, 56, 89, 45, 7, 2, 8, 1])

# The np.searchsorted() function will assume that the array is ALREADY sorted and will return the index of the value you passed in to search. It will return the index where Numpy would insert it to maintain the sorted order.
print(np.searchsorted(actually_sorted, 15))
print(np.searchsorted(not_sorted, 45))
print(np.searchsorted(actually_sorted, 66)) # 7 - Numpy will put this value at index 7 to maintain the sorted order.

print(np.searchsorted(actually_sorted, 25, side="right")) # Optional parameter, side, this will basically tell Numpy to start sorting from a certain direction which is left or right
# I think right starts with 1 but left (default) starts with 0?

More_Numbers = np.array([1, 3, 5, 7])
print(np.searchsorted(More_Numbers, [2, 4, 6, 9])) # Will return a table of indexes on each corresponding number on where Numpy will insert these values to maintain the sorted order
print("--------------------")

print("----- Sorting Arrays -----")
Random_Numbers_Array = np.array([456, 568, 213, 768, 345, 556, 258, 484, 732])
Sorted_Array = np.sort(Random_Numbers_Array)
print(Sorted_Array)

Sort_This_Two_Dimensional_Array = np.array([ # Literally sorts every element in the array
    [346, 873, 388, 897, 324],
    [765, 567, 245, 787, 432]
])

Sorted_Two_Dimensional_Array = np.sort(Sort_This_Two_Dimensional_Array)
print(Sorted_Two_Dimensional_Array)
print("--------------------")

print("----- Filtering Arrays -----")
More_Arrays = np.array([5, 3, 9, 10, 58, 2])
This_idk_bool_array = np.array([True, True, False, True, False, False])

Filtered_Array = More_Arrays[This_idk_bool_array] # Filters the array by corresponding the values between the two arrays. The values that correspond with True will be included in the filtered array else excluded.

A_Filtered_List: list[int] = []

for element in np.nditer(More_Arrays): # You can also hard code the filtering instead because it's based on conditions
    if element % 2 == 0:
        A_Filtered_List.append(True)
    else:
        A_Filtered_List.append(False)

New_Array = More_Arrays[A_Filtered_List]
print(A_Filtered_List)
print(New_Array)
print("--------------------")

# ========== Numpy Official Documentation for Beginners ==========

# You can add dimensions by using np.newaxis() and np.expand_dims
Lot_of_Numbers = np.arange(1, (20) + 1)
print(Lot_of_Numbers)

# np.newaxis is equivalent to None
# Creates a VIEW of the original array and slices the original array's elements to keep them
# Yes, order DOES matter. If you put np.newaxis at the front and slice at the end, it will create more columns
Expanded_Columns = Lot_of_Numbers[np.newaxis, :]
print(Expanded_Columns)

# If you want to add more rows then slice at the front and np.newaxis at the end
Expanded_Rows = Lot_of_Numbers[:,  np.newaxis]
print(Expanded_Rows)

# Alternative Way: np.expand_dims()
Alternative_Column_Expansion = np.expand_dims(Lot_of_Numbers, axis=0)
print(Alternative_Column_Expansion)

Alternative_Row_Expansion = np.expand_dims(Lot_of_Numbers, axis=1)
print(Alternative_Row_Expansion)

# Filtering arrays
Even_Numbers_Array = Lot_of_Numbers[Lot_of_Numbers%2 == 0]
print(Even_Numbers_Array)

# Find even numbers that are greater than 10
Conditional_Array = Lot_of_Numbers[(Lot_of_Numbers%2 == 0) & (Lot_of_Numbers > 10)] # Use the & for and and | for or in conditional sorting
# Also use (condition) to separate conditions (NEEDED)
print(Conditional_Array)

# To find all values that are NOT zero, you can use the np.nonzero() function
print(np.nonzero(Even_Numbers_Array))

More_Random_Numbers_Array = np.array([[56, 1, 0], [3, 0, 0], [1, 6, 3], [82, 5, 1]])
print(np.nonzero(More_Random_Numbers_Array)) # Since it is a 2D array, the first array will be the rows and the second array will be the columns