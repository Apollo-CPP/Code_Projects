import numpy as np
# This file will be a practice for ufuncs (Universal Functions)
# They are accessible through Numpy

# Vectorization
# w3schools: Converting iterative statements into a vector based operation is called vectorization.

A_List_of_Numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Another_List_of_Numbers: list[int] = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
A_List_of_Sums: list[int] = []

# You can loop through both of the arrays by using the zip() function and adding them into a separate list to get the sums of the corresponding elements
for x, y in zip(A_List_of_Numbers, Another_List_of_Numbers):
    A_List_of_Sums.append(x + y)

print(A_List_of_Sums)

Array_of_Numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Another_Array_of_Numbers = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

# Or you can use ufunc and call the add() function instead
Array_of_Sums = np.add(Array_of_Numbers, Another_Array_of_Numbers) # Same thing, much simpler, and more concise
print(Array_of_Sums)

# There are also other operational functions like subtract(), multiply(), and divide()
Array_of_Products = np.multiply(Array_of_Numbers, Another_Array_of_Numbers)
print(Array_of_Products)

# You can create your own custom ufunc function by using np.frompyfunc()

# This function takes every element in the Numpy array and raises them to the power of 3
def Calculate_Exponent(Array: np.ndarray, Exponent: int):
    return Array ** Exponent

Calculate_Exponent = np.frompyfunc(Calculate_Exponent, 2, 1)
# First parameter is the function name, second parameter is the amount of parameters, and the third parameter is how many outputs the function will return or the amount of values returned

print(Calculate_Exponent([1, 2, 3, 4, 5], 3))

# To check if a function is a ufunc, we can use the np.ufunc() function

if type(Calculate_Exponent) == np.ufunc:
    print("It's a ufunc!")
else:
    print("Developer defined function")

# Some additional arithmatic functions
Power_Numbers_Array = np.array([2, 7, 3, 9])
Exponent_Numbers_Array = np.array([5, 2, 8, 3])

Powered_Numbers_Array = np.power(Power_Numbers_Array, Exponent_Numbers_Array)
# Each corresponding value index will be calculated. Example: The value two at index 0 to the power of the value 5 at the index 0. Basically 2^5.
print(Powered_Numbers_Array)

# You can get the remainder of the division calculation by using np.mod() or np.remainder(). They both do the EXACT same thing.
Dividend_Array = np.array([50, 15, 100, 30])
Divisor_Array = np.array([6, 3, 9, 2])

Remainder_Array = np.remainder(Dividend_Array, Divisor_Array)
print(Remainder_Array)