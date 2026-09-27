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

# Or if you want both the quotient and the remainder then you can use the np.divmod() function
print(np.divmod(Dividend_Array, Divisor_Array))
# First array are the quotients and the second array are the remainders with corresponding indexes

# If you want the absolute values of an array then you can use the np.absolute() function
Random_Numbers_Array = np.array([-1, 6, -100, 37, -7])
print(np.absolute(Random_Numbers_Array))

# Rounding Decimals

# We can use the trunc() or fix() function to remove decimals from a floating point number and rounds to the integer that is closest to zero
Floating_Point_Array = np.array([6.2121212121, 8.333333, 5.7777777, 2.222222])
print(np.trunc(Floating_Point_Array))
print(np.fix(Floating_Point_Array)) # Do not use np.fix() as it is deprecated and slower than np.trunc()

# Or if you wanna do round then you can use the np.around() or np.round() function
print(np.around(Floating_Point_Array))
print(np.round(Floating_Point_Array))
# They both do the exact same thing

# If you want to round down a floating point number then use the np.floor() function
More_Floats_Array = np.array([-62.686921, 4.65992, 7.1111111111, 5.683928])
print(np.floor(More_Floats_Array))

# But if you want to round them up then use the np.ceil() function
print(np.ceil(More_Floats_Array))
print("---------------------------------------------")

# Moving onto performing logarithmatic
Ranged_Numbers = np.arange(1, 10)
print(Ranged_Numbers)

# Use the log2 function to perform log operations but with a base of 2
print(np.log2(Ranged_Numbers))
# Basically log2(<A Number in the Ranged_Numbers>) = x meaning, what power with the base 2 will equal to that Number in the Ranged_Numbers?

print(np.log10(Ranged_Numbers))
# Same thing as log2 but except it's log10, meaning with a base of 10.

import math

# You can also log with any base but since NumPy doesn't have that available, you can use the np.frompyfunc() with the math.log() function
nplog = np.frompyfunc(math.log, 2, 1)
print(nplog(Ranged_Numbers, 4)) # Log but with base 4

# Even more arithmatic NumPy functions
Lot_of_Numbers = np.arange(1, (10) + 1) # 1 - 10
Even_More_Numbers = np.arange(11, (20) + 1) # 11 - 20

# As we know the np.add() function adds every value with the corresponding index
print(np.add(Lot_of_Numbers, Even_More_Numbers))

# However, there is also an np.sum() function that adds every value in the array together
print(np.sum([Lot_of_Numbers, Even_More_Numbers])) # Adds every number from 1 to 20 (210)
print(np.sum([Lot_of_Numbers, Even_More_Numbers], axis=1)) # Adds every number from each array. First is numbers from 1 - 10 and then second is 11 - 20

# If you want the find the cumulative sum then you can use the np.cumsum() function
print(np.cumsum(Lot_of_Numbers)) # Finds the cumulative sum of numbers from 1 - 10
# Visualization: [1, 2, 3, 4, 5]
# This function basically keeps adding the previous number to the next number until the end
# First number is 1 because it is the starting number but the second number is 3 because it adds the first number (1) to the next number (2). This keeps repeating until the end

# NumPy Products

# If you want the product of an array then use np.prod()
print(np.prod(Lot_of_Numbers)) # Multiples every element just like np.add()
# 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800

# If you want the cumulative product then use np.cumprod()
print(np.cumprod(Lot_of_Numbers))

# Numpy Differences
# Differences work a little bit different than Numpy Addition

ok_lot_of_numbers = np.array([3, 8, 13, 25])

print(np.diff(ok_lot_of_numbers))
# It still goes through the elements one by one but except the value next subtracts them
# First element is 8 - 3, second is 13 - 8, and third and last is 25 - 13

print(np.diff(ok_lot_of_numbers, n=2))
# You can have the optional parameter, n, which is basically how many times you want to repeat it
# Currently you have [5, 5, 12] after the first difference but we do it again because n is 2.
# 5 - 5 = 0 and 12 - 5 = 7 - Leaving you with the final result of [0, 7]

# LCM (Lowest Common Multiple)

Random_Number_1 = 6
Random_Number_2 = 9

# Just finds the lowest common multiple between the two numbers
print(np.lcm(Random_Number_1, Random_Number_2))

LCM_Array = np.array([3, 7, 2]) # Find the lowest common multiple between all value
print(np.lcm.reduce(LCM_Array))

Another_Ranged_Array = np.arange(1, (10) + 1)
print(np.lcm.reduce(Another_Ranged_Array))

# GCD (Greatest Common Divisor) or HCF (Highest Common Factor)

Another_Number = 6
Also_Another_Random_Number = 8

print(np.gcd(Another_Number, Also_Another_Random_Number))
# The highest number that is able to divide both 8 and 6 is 2

GCD_Array = np.array([20, 8, 16, 32])
print(np.gcd.reduce(GCD_Array)) # 4 - The highest number that is able to be divided within all numbers in the array

# Some trigonometry with NumPy

print(np.pi) # Equivalent to math.pi

# sin(), cos(), and tan() function

# SOH, CAH, TOA
# Sin - Opposite over Hypotenuse
# Cos - Adjacent over Hypotenuse
# Tan - Opposite over Adjacent

print(np.sin(3/5))
print(np.cos(4/5))
print(np.tan(3/4))

Pi_Division_Array = np.array([np.pi, np.pi/2, np.pi/3, np.pi/4])
print(np.sin(Pi_Division_Array))

# Use np.deg2rad() function to convert degree values to radians
Degrees_Arary = np.array([90, 180, 270, 360])
print(np.deg2rad(Degrees_Arary))

# But if you want to convert radians to degrees then you can use the np.rad2deg() function instead
Random_Radians_Array = np.array([5.32385, 3.8953, 10.347592, 4.6848929])
print(np.rad2deg(Random_Radians_Array))

Some_Values = np.array([1, -1, 0.1])
print(np.arcsin(Some_Values))

Side_A = 3
Side_B = 4

# Use the np.hypot() function to find the hypotenuse of a right triangle
print(np.hypot(Side_A, Side_B)) # Returns a float