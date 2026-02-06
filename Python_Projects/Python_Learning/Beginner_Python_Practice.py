print("One line!")
print("One line and then..."); print("A second line..?"); print("A THIRD LINE??") # I guess you can put as much lines as you want? (Don't do this though because it's not clean honestly)

print("Hello World", end = " ")
print("Printed on same line wth lol")

print(3 + 3) # 6 - Print calculations
print("I am",15,"years old!") # Able to combine or concatenate strings with numbers >:O It also automatically enters a space too dang?

string_variable = "string thing lol"
number_Variable_thing = 15

print(string_variable) # Able to print variables!
print(number_Variable_thing)

# Casting
a_number = 15
a_number = float(a_number)
print(a_number) # Casting is just attempting to change a variable's type to another type

print(type(a_number)) # Can use the type function to print the type of a variable to confirm the variable's type

A = "Dylan"
a = 'Dylan'
# Apparently these are both the same thing

print(a)
print(A)

# Confirmed using type function
print(type(a))
print(type(A))

what, err, idk = "hi", "yeet", "lol" # You can create multiple variables and assign them values
print(what, err, idk) # Just ofund out you can print multiple variables just separate them with commas at the same time and it even adds an automatic space lol

what = err = idk = "lol ok" # You can also assign them the same value at the exact same time
print(what, err, idk)

more_string = "yes "
lot_string = "many lol"

print(more_string + lot_string) # Or you can do this to print concatenating variables

Same_Name_Variable = "lolol" # Global variable - Defined outside of a function

def this_random_function(me_want_string):
    Same_Name_Variable = "woah" # Local variable - Defined inside of a function
    global global_variable_lol # Force python to make a variable but it's global
    global_variable_lol = "yes"
    print(Same_Name_Variable)

this_random_function(Same_Name_Variable)
print(global_variable_lol) # I guess it worked
print("Me like " + global_variable_lol)

this_random_range = range(10)
print(this_random_range) # range(0, 10)

number_XD = 1
float_number = 5.3e5 # You can put e to put "to the power of 10 by ..?" This means 5.3 to the power of 10 (5) times.
complex_number = 1j # What the heck is this

print(number_XD)
print(float_number)
print(complex_number)

import random # My first module the random module >:D

my_random_range = random.randrange(1, 100)
my_random_number = random.randint(1, 100) # Generates a random number between 1 - 100

print(my_random_number)
print(my_random_range)

more_int_lol = 547
more_string_XD = "56584"
more_float_XD = 5368

print(int(more_string_XD) + more_float_XD) # More casting but just adding

Message = '''
    Hello! This is a multi-line string!
    Very cool for printing?
    Multiple lines! XD
'''

print(Message)

this_string_array = "Hi Guys" # Apparently strings can also be treated like arrays
print(this_string_array[1]) # i

for character in this_string_array: # Welp I guess you can also loop through them just like arrays
    print(character)

string_length = len(this_string_array)
print(string_length) # Prints the length of the string

this_another_string = "Yes another string"
print("ooga booga" in this_another_string) # Returns bool (True or False) if it finds a specified string in another string, in this case it is false
print("yes" in this_another_string) # It's case sensitive too
print("Yes" in this_another_string) # True
print("string" not in this_another_string) # not keyword can also be used to check if a specified string is not in another string

slicing_string = "Slice of Watermelon lol"
print(slicing_string[3:5]) # Prints characters from the 3rd index to the 5th index
print(slicing_string[:5]) # Prints characters from beginning to 5th index because there is no set beginning
print(slicing_string[9:]) # Prints characters from 9th index to the end
print(slicing_string[-1:-2]) # You can even slice backwards lol

Why_More_Strings = "Bro that's a little bit TOO MUCH strings there now XD"
print(Why_More_Strings.upper()) # Prints the uppercase of the string, basically all caps
print(Why_More_Strings.lower()) # Prints the lowercase of the string
print(Why_More_Strings.strip()) # Removes all whitespaces from the beginning and the end of the string

print(Why_More_Strings.replace("XD", "- you just got replaced lol")) # First parameter (find that string) and second parameter (replace it with this)
print(Why_More_Strings.split("TOO")) # I guess it just splits the string and replaces it with a comma?

print("XD" in Why_More_Strings) # Will return a bool, just checks if a specific string is inside of another string or if it contains that specific string (True)
print("MUCH" not in Why_More_Strings) # Will return false since it is in it. Meaning: Check if lol is not in Why_More_Strings

More_String_bro = "ooga booga" 
Yeah_ok = "yeeeeet"
Combine_Boi = More_String_bro + Yeah_ok
print(Combine_Boi) # Just join the two strings together / Concatenation

This_a_thing = 45

print(f"A variable is {This_a_thing}") # Formatted strings!
print(f"A times 2 lol is {This_a_thing * 2}") # Can even perform operations in it too lol

My_Bool = True # Equivalent to 1
MY_Other_Bool = False # Equivalent to 0

def This_True_Function():
    return True

if This_True_Function(): # Can use functions to evaluate booleans
    print("Yeah it true!")
else:
    print("ok false")

This_ok_Variable_lolol = 47
print(This_ok_Variable_lolol:=5) # Sets and prints the new value of This_ok_Variable_lolol

other_thing = {483, 196, 28, 385}
another_number = {486, 274, 185, 329, 593}
this_idk_variable = other_thing|another_number # I think this means combining also it's known as the "walrus" operator

for element in this_idk_variable:
    print(element)

these_numbers = [1, 2, 3, 4, 5]

if (count := len(these_numbers)) == 5:
    print("Five elements!")

this_dictionary = {
    "dzhann57": 1,
    "dzhann757": 2,
    "bzhan17": 3
}

for username in this_dictionary:
    print(username) # Prints Keys

for i in this_dictionary:
    print(this_dictionary[i]) # Prints keys' values

Weather = "Sunny"

match Weather: # Just like switch and case in C++ lol
    case "Rainy":
        print("Bring an Umbrella!")
    case "Windy":
        print("Lotta winds here")
    case "Sunny":
        print("Shineeeeee")
    case _: # Like default in C++ but except it's just an underscore (_) followed by a colon
        print("Unknown weather?")


The_Day = 3
Month = 4

match The_Day:
    case 1 | 2 | 3 | 4 | 5 if Month == 5: # Use or ( | ) operator to combine also you for some reason don't need the 'and' keyword after combining
        print("It's a weekday")
    case 6 | 7:
        print("It's the weekends")
    case _:
        print("What just happened?")

this_ok_number = 0

while this_ok_number < 5:
    print(this_ok_number)
    this_ok_number += 1

else: # I guess you can put an else statement here to signify that the while loop is done? Yes, you can also do this in for loops
    print("Ok it stopped")

My_Range = range(0, (20) + 1, 2) # Added 1 to make it inclusive and step is 2 so it's like 0, 2, 4, 6, 8...

if 8 in My_Range:
    print("Wow 8 is in range!")

Fruits = ["Strawberry", "Bananna", "Blueberry"]
Opinions = ["Best", "Nice", "Pretty Good"]

for fruit in Fruits: # Nested loops
    for opinion in Opinions:
        print(fruit, opinion)

def Greet_Friend(name = "Friend"): # Set a parameter equal to something as a DEFAULT value
    print(f"Hello, {name}")

Greet_Friend("Dylan") # "Hello, Dylan"
Greet_Friend() # "Hello, Friend"

def Pet_Information(Animal, Name):
    print(f"The animal is {Animal} and its name is {Name}!")

Pet_Information(Name = "Apollo", Animal = "Dog") # You can pass arguments as keywords and the order doesn't matter
Pet_Information("Yeah", Name = "o k") # Can also mix keyword and normal arguments but positional (regular) arguments MUST come first!

def yeah():
    print("yeah!")

print(yeah.__name__) # Just prints the function's name

this_variable_what = lambda number : number * 5 # Basically lambda's a like "to go" functions, a short-mini function
print(this_variable_what(5))

these_random_numbers_lol = [4, 2, 57, 25, 9, 27, 6, 1, 8, 45, 345]
these_even_numbers = list(filter(lambda element : element % 2 == 0, these_random_numbers_lol))

for element in these_even_numbers:
    print(element)

def countdown(x): # Recursion - Calling the same function inside of the function itself
    if x <= 0:
        print("Countdown has finished.")
    else:
        print(x)
        countdown(x - 1)

countdown(10)

import sys
print(sys.getrecursionlimit()) # There obviously is a limit but can be set using sys.setrecusionlimit()

def this_generator_function(): # Yield pauses execution, saves the data, and continues where it is left off also it's memory efficient
    yield 1
    yield 2
    yield 3

for value in this_generator_function():
    print(value)

this_gen = this_generator_function()

print(next(this_gen))
print(next(this_gen))
print(next(this_gen)) # Adding another one will raise a StopIteration error

class This_Class:
    def __init__(self, name):
        self.Name = name
        print(f"The class' name is {self.Name}")
    
    def __iter__(self):
        self.this_class_number = 5
        print(f"Class number will start at: {self.this_class_number}")
        return self

    def __next__(self):
        if self.this_class_number >= 100: # Stop the iteration from going on infinitely
            raise StopIteration # Raises this custom errror to stop the iteration
        else:
            print("Skip counted by 5!")
            self.this_class_number += 5
            x = self.this_class_number + 5
            return x
    
this_random_class = This_Class("lol")
this_class_iterator = iter(this_random_class)

for x in this_class_iterator:
    print(x)

import datetime

print(datetime.datetime.now())
print(datetime.datetime(2010, 6, 21, 6, 30).strftime("%A, %B, %d, %Y, %I, %M, %p")) # String format time basically just formats the time format into a readable string format

# Some built-in math functions

this_minimum_number = min(556, 23, 776, 45, 13, 5) # Finds the lowest number
this_maximum_number = max(56, 34, 78, 435, 3, 56, 2) # Finds the greatest number

print(this_minimum_number)
print(this_maximum_number)

this_absolute_number = abs(-386.39) # Finds the absolute value of that number or the distance from the number 0 - Always POSITIVE
print(this_absolute_number)

this_powed_number = pow(3, 4) # Three to the power of 10 (4 times) or 3 x 3 x 3 x 3 also equivalent to 3 ** 4
print(this_powed_number)

# More Math Thing
import math # The math library provides additional math functions if needed

square_root_number_thing = math.sqrt(64) # 8
print(square_root_number_thing)

ceil_this_number = math.ceil(3.2) # Prints 4 because ceil always rounds UP to the nearest number
floor_this_number = math.floor(7.6) # Prints 7 because floor always rounds DOWN to the nearest number

print(ceil_this_number)
print(floor_this_number)

pie_lolol = math.pi # Literally just pi
print(pie_lolol)

def error_handle_thing(input_thing: str) -> bool:
    try: # Try function basically attempts to do an operation
        this_idk_input = int(input_thing)
        return True
    except: # Except alone runs when ANY errors occur
        print("Oh no error!")
        return False

def error_handle_number_two(more_input: str) -> bool:
    try:
        this_input_lol = int(more_input)
        return True
    except NameError: # Except but with a certain error code runs when that error code is hit, you can also have as much except blocks as you like
        print("no")
    else: # ONLY runs when no errors are hit
        print("Oh wow! No errors fr?")
    finally: # ALWAYS runs no matter what
        print("Last and final piece of block lol")

pls_user_input_number = input("Pls input number lol: ")

if error_handle_thing(pls_user_input_number) == True:
    print("yay")
else:
    print("oh no")

this_error_number = 15

if type(this_error_number) is not int:
    # raise Exception("The variable is not of type int!") # Raise - Throw an error
    raise TypeError("The variable is not of type int!") # You can also raise those certain errors too
else:
    print("oh it is an int")

def mutiply_idk_number(number: int) -> int:
    return number * 0.5486

this_big_number_XD = 84769
print(f"This big number is: {mutiply_idk_number(this_big_number_XD):,}") # You can even perform operations in f strings. Functions, if statements, rounding, etc.
print(f"This item is {'Expensive' if this_big_number_XD >= 10000 else 'Cheap'}") # In line if statement operation in printing an f string

# The None Keyword

def this_none_function() -> None:
    yeah_idk_here = 5

this_none_idk = None

print(this_none_idk) # Literally prints None with letters N o n e
print(type(this_none_idk)) # Type is NoneType
print(bool(None)) # Always evaluates to false

this_another_none = this_none_function()
print(this_another_none) # Functions that return nothing evaluates to None

print("hi guy")
idkwhat = input() # Blank input
print(f"ohio: {idkwhat}")

yeah_meh = input("Wut name boi: ") # Inputting with prompt
print(f"oh hi guy {yeah_meh}")

print(f"Hello: {input("What is your name?: ")}") # I guess you can also do this! It asks for the input first and then prints it out

Keep_Inputting_lol = True

while Keep_Inputting_lol == True:
    this_idk_input_number = input("pls enter a number pls guy: ")

    try:
        this_idk_input_number = int(this_idk_input_number)
        Keep_Inputting_lol = False
    except:
        print("HEY BOI I SAID ENTER A NUMBER")