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