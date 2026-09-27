import random
import enum

def random_function(pos_only, /, standard_arg, *, keyword_arg): # Positional arguments first, then standard (regular) arguments, and lastly keyword arguments, with that specific set up
    print(pos_only)
    print(standard_arg)
    print(keyword_arg)

random_function(2, "dfg", keyword_arg="me")

numbers: list[int] = [0, 1, 2, 3, 4, 5]

print(" ", end="")
print(*(x for x in range(5)), sep=" ") # A comprehension

me = "435", 4, "dg", 45.63 # Apparently assigned a variable multiple values turns it into a TUPLE of values
print(me) # Proven here
print(type(me)) # Proven here as well

# Difference between == and is (Equality vs. Identity)
This_Number: int = 10
Another_Number: int = 10

print(This_Number == Another_Number) # True, because == compares their values and 10 equals to 10
print(This_Number is Another_Number) # This is false because they are both not the exact same thing in memory

This_Number = Another_Number # However, equating one to another will change their memory addresses to become to variable that you just set it to
print(This_Number is Another_Number) # Now this evaluates to True because they are both the same thing in memory

# I usually write a dictionary like this for better readability
Woah_a_dictionary: dict[str, str] = {
    "meme": "oh",
    "yeahhh": "yeeeet",
    "brrrrr": "yes"
}

# I wrote it like that so much that I forgot you can write a dictionary like this way as well lol
Okay_another_dictionary: dict[str, str] = {"yesh": "ooga", "yeaaaaa": "oof", "ded": "eee"}

Random_Number = random.randint(0, 5)
print(Random_Number)

# Match and case are like if statements but are usually used for patterns
match Random_Number:
    case 0:
        print("It got 0")
    case 1:
        print("It got 1")
    case 2:
        print("It got 2")
    case _: # case _, is a default if no other cases are reached
        print(f"It got this number: {Random_Number}")

class Colors(enum.Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"

Favorite_Color = input("What is your favorite color?: ")

match Favorite_Color:
    case Colors.RED:
        print("Woah nice")
    case Colors.BLUE:
        print("also a good choice >:D")
    case Colors.GREEN:
        print("Less popular choice but okay")
    case _:
        print(f"Okay not bad ig, {Favorite_Color} is not a bad color")

def remembering_function(number: int, this_list: list[int] = []): # Apparently default values are evaluating only once and functions 
    this_list.append(number)
    print(this_list)

# [1]
remembering_function(1)
# [1, 2]
remembering_function(2)
# [1, 2, 3]
remembering_function(3)

def setting_default(number: int, another_list: None | list[int] = None):
    # To avoid a function always using a past value, set it to None and then set it to an empty list so that it will establish another separate list
    if another_list is None:
        another_list = []

    another_list.append(number)
    print(another_list) # Now only prints values separately instead of combining all previous values

setting_default(5)
setting_default(100)
setting_default(435)

# Challenge: Find all prime and composite numbers from 1 - 100

for i in range(1, (100) + 1): # Numbers from 1 - 100
    Factors: list[int] = []

    for j in range(1, i):
        if i % j == 0: # Check if the current number is even or divisible by j
            Factors.append(j)

    if len(Factors) <= 1: # Check if the length of the list is one (Only one factor, being one)
        print(f"{i} is Prime! It has no factors other than 1 and itself!")
    else:
        print(f"{i} is Composite! It has other factors than 1 and itself! Factors of {i}: {[x for x in Factors]}")

class Point:
    __match_args__ = ("x", "y") # __match_args__ is the dunder / magic method for the match keyword

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

X_Coordinate = int(input("What is the X Coordinate?: "))
Y_Coordinate = int(input("What is the Y Coordinate?: "))

Point_A = Point(X_Coordinate, Y_Coordinate)

match Point_A:
    case Point(x=0, y=0):
        print("Origin!")
    case Point(x=x, y=y) if x == y:
        print("Both coordinates have the same number!")
    case Point(x, y):
        print("This is a point, a coordinate!")
    case _:
        print("What?")

def arguments_function(ooga_string: str, meme_number: int, yeahyeah: float):
    print(ooga_string)
    print(meme_number)
    print(yeahyeah)

arguments_function("woah", 21, 69.420) # These are positional arguments, just passing in information to the function, which will correspond to the order defined in the function parameters
arguments_function(meme_number = 420, yeahyeah = 23.48, ooga_string = "rge") # These are keyword arguments, you pass in the parameter names first and then pass in the values you actually want to pass. They don't need to be in order

pairs: list[tuple[str, int]] = [("Four", 4), ("Two", 2), ("Three", 3), ("One", 1)]
pairs.sort(key=lambda x: x[0]) # Lambdas are anonymous functions with a single expression, they are used for quick action without needing to define a whole function just for it
print(pairs)