import numpy as np

# Numpy provides the random module, which can be used to generate a random number
First_Random_Number = np.random.randint(1, (100) + 1) # Start (Inclusive) and End (Exclusive)
print(First_Random_Number)

Random_Float = np.random.rand() # This function generates a random float between 0 to 1
print(Random_Float)

# You can even generate a random array as well but with an extra parameter, size
Random_Array = np.random.randint(100, size=5) # This generates a One Dimensional array with random numbers from 1 to 100 with the size of 5
print(Random_Array)

# You can also generate 2D arrays
Random_Two_Dimensional_Array = np.random.randint(100, size=(2, 2)) # Generates a 2D Array from 1 - 100 with the size of 2 rows and 2 columns
print(Random_Two_Dimensional_Array)

Float_2D_Array = np.random.rand(3, 2) # Generates a 2D Array with 3 rows and 2 columns filled with random floats from 0 - 1 
print(Float_2D_Array)

Float_1D_Array = np.random.rand(3) # Generates a 1D array with 3 elements filled with random floats from 0 - 1
print(Float_1D_Array)

Randomly_Picked_Number = np.random.choice(np.arange(1, (10) + 1)) # Pick a randon number from 1 - 10
print(Randomly_Picked_Number)

# Generate a 2D Array with 3 rows and 5 columns and fill them with random numbers ranging from 1 - 5
Random_Number_From_2D_Array = np.random.choice([1, 2, 3, 4, 5], size=(3, 5))
print(Random_Number_From_2D_Array)

# ========== Data Distribution ==========
# We can create a randomized array using probability by putting the optional parameter, p.
# p takes in a list of floats, which all must add up to 1. If it doesn't then Python will raise a ValueError
# This creates a 1D Array with 100 integers, more specifically 1, 3, 7, 9, and 10.
# 20% to get 1, 10% to be 3, 40% to be 7, 10% to be 9, and 20% to be 10. (All floats / percentages must add up to 1.0 or 100%)
Probability_Array = np.random.choice([1, 3, 7, 9, 10], p=[0.2, 0.1, 0.4, 0.1, 0.2], size=(100))
print(Probability_Array)

# Creates a 2D array with all numbers from 1 - 10 having an equal 10% chance to be chosen with 10 rows and 10 columns
# The amount of possible elements and the size of p must be the same as well
Chance_2D_Array = np.random.choice(np.arange(1, (10) + 1), p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], size=(10, 10))
print(Chance_2D_Array)

# We can randomize the elements in the array by using the shuffle() function
Lot_of_Numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
np.random.shuffle(Lot_of_Numbers) # This function mixes the elements randomly
print(Lot_of_Numbers)

# We can also use the permutation() function to generate a random combination out of all of the possible combinations of the array
Combo_Array = np.array([1, 2, 3, 4, 5])
Random_Combo = np.random.permutation(Combo_Array)
print(Random_Combo)

# ========== This is the starting point of where I need to use other modules for Numpy data visualization ==========

import matplotlib
import matplotlib.pyplot as plt
import seaborn

# w3schools definition of seaborn: Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
# Displots (Distribution plots) are takes an array and plots a curve, basically graphing

# seaborn.displot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # Both of these are histograms
# seaborn.displot([0, 1, 2, 3, 4, 5])

# seaborn.displot(np.arange((20) + 1), kind="kde") # Displays a graph but it's a curve?
# plt.show()

# x = np.random.normal(size=(2, 3))
# print(x)

# y = np.random.normal(loc=1, scale=2, size=(2,3))
# loc is center of the curve, scale is how wide it is, and size is just the size of the array or shape of it
# print(y)

# seaborn.displot(y, kind="kde")

# seaborn.displot(np.random.normal(size=(1000)), kind="kde")
# plt.show()

# Binomial distribution is basically probability like a fipping a coin with the amount of trials and setting a percentage for an outcome. You can also set the size of the returned array as well.

# data = {
#     "normal": np.random.normal(loc=50, scale=5, size=1000),
#     "binomial": np.random.binomial(n=100, p=0.5, size=1000)
# }

# Binomial_Probability = np.random.binomial(100, 0.5, 1000) # "Flipping a coin" - Numbers from 0 - 100 with a 50% of getting a random number, returning a 1D array with 100 numbers
# print(Binomial_Probability)

# seaborn.displot(Binomial_Probability)

# seaborn.displot(data, kind="kde")
# plt.show()

# Poisson Distribution

# Random_Poisson = np.random.poisson(lam=2, size=100)
# print(Random_Poisson)

# seaborn.displot(Random_Poisson, kind="kde")
# plt.show()

# data = {
    # "normal": np.random.normal(loc=50, scale=7, size=1000),
    # "poisson": np.random.poisson(lam=50, size=1000)
# }

# seaborn.displot(data, kind="kde")
# plt.show()

# Uniform Distribution
# Random_Uniform = np.random.uniform(size=10000)
# print(Random_Uniform)

# seaborn.displot(Random_Uniform, kind="kde")
# plt.show()

# Logistic Distribution
# w3schools: Logistic Distribution is used to describe growth.
# w3schools: Used extensively in machine learning in logistic regression, neural networks etc.

# Random_Logistic = np.random.logistic(loc=1, scale=2, size=(2,3))
# print(Random_Logistic)

# seaborn.displot(np.random.logistic(size=(1000)), kind="kde")
# plt.show()

# Multinomial Distribution
# A generalization of binomial, it has more outcomes than just 2.
# Random_Multinomial = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
# A pvals added must equal to one.
# print(Random_Multinomial)

# Exponential Distribution (Similar to Poisson)
# w3schools: Exponential distribution is used for describing time till next event e.g. failure/success etc.

# Random_Exponential = np.random.exponential(scale=2, size=(2, 3))
# print(Random_Exponential)

# seaborn.displot(np.random.exponential(size=1000), kind="kde")
# plt.show()

# Chi Square Distribution (What the heck)
# w3schools: Used as a basis to verify hypothesis??

# Random_Chi_Square = np.random.chisquare(df=2, size=(2, 3))
# df = Degree of Freedom??
# print(Random_Chi_Square)

# seaborn.displot(np.random.chisquare(df=1, size=1000), kind="kde")
# plt.show()

# Rayleigh Distribution
# w3schools: Rayleigh distribution is used in signal processing.

# Random_Rayleigh = np.random.rayleigh(scale=2, size=(2,3))
# print(Random_Rayleigh)

# seaborn.displot(np.random.rayleigh(size=1000), kind="kde")
# plt.show()

# Pareto Distribution
# w3schools: A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

# Random_Pareto = np.random.pareto(a=2, size=(2, 3))
# Apparently, a is a shape parameter?
# print(Random_Pareto)

# seaborn.displot(np.random.pareto(a=2, size=1000), kind="kde")
# plt.show()

# Zipf Distribution
# w3schools: Zipf distributions are used to sample data based on zipf's law.
# Zipf's laws: In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.

# Random_Zipf = np.random.zipf(a=2, size=(2, 3))
# a is the distribution parameter
# print(Random_Zipf)

# Sample_Zipf = np.random.zipf(a=2, size=1000)
# seaborn.displot(Sample_Zipf[Sample_Zipf < 10], kind="kde") # Plot values that are in the array that are less than 10
# plt.show()