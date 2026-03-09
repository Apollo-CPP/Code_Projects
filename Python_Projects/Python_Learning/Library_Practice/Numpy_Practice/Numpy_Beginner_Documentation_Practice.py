# ========== Numpy Official Documentation for Beginners ==========

import numpy as np

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

# Generating random numbers in an array

My_RNG = np.random.default_rng() # Creates a generator based off of the PCG64 generator
print(My_RNG.random(10)) # Generates random floats between 0.0 and 1.0
print("--------------------")
My_RNG_Array = My_RNG.integers((10) + 1, size=(4, 4)) # Generates whole numbers from 0 to 10 (End is exclusive and starting point is 0 by DEFAULT) in a 2D 4x4 array
print(My_RNG_Array)
print("--------------------")

# You can use np.unique() to find only unique numbers in the array
print(np.unique(My_RNG_Array)) # Find unique values!
print("--------------------")

Unique_Values, Value_Indexes = np.unique(My_RNG_Array, return_index=True) # You can even return their indexes as well, just make sure to put two variables since it returns two things
print(Unique_Values) # Print the unique values
print("--------------------")
print(Value_Indexes) # Print their indexes
print("--------------------")

Value_Counts = np.unique(My_RNG_Array, return_counts=True)
print(Value_Counts) # Returns the amount of occurences a value has
print("--------------------")

# Transposing and reshaping arrays

Transposing_Array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# Reshapes to 5 rows and 2 columns
print(Transposing_Array.reshape(5, 2)) # Reshaping basically changes the dimensions of the array, it needs to multiply up to the amount of elements in the array

# Rearranges the array's axes or shape. 5 rows and 2 columns becomes 2 rows and 5 columns
print(Transposing_Array.reshape(5, 2).transpose())
print(Transposing_Array.reshape(5, 2).T) # Numpy also provides the attribute or property T for a numpy array, which basically shows the transposed version of the array

# Reversing arrays

Reverse_Me_Array = np.arange(1, (10) + 1)
Two_Dimensional_Reverse_Me_Array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# We can use the np.flip() function ro reverse Numpy arrays
print(np.flip(Reverse_Me_Array)) # Reverses all elements

# Reverses the order of the lists and the elements in those lists
print(np.flip(Two_Dimensional_Reverse_Me_Array))

# Axis=0 only reverses the order of the lists (vertical)
print(np.flip(Two_Dimensional_Reverse_Me_Array, axis=0))

# Axis=1 only reverses the elements inside of the lists of the NumPy Array
print(np.flip(Two_Dimensional_Reverse_Me_Array, axis=1))

# "Flattening" arrays (Converting arrays back to 1 dimensional arrays)

Random_2D_Array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Use the flatten() function to convert an array back to 1D
print(Random_2D_Array.flatten())

# You can also use the ravel() function to do this as well
print(Random_2D_Array.ravel())

# The difference between flatten() and ravel() is that flatten creates a copy of the array but ravel() creates a view of the array