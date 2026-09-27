import typing

# Data Structures are just different ways to store data, each with their own benefits and drawbacks
# In this python file, I will be learning the most basic data structures of Python following the Python Documentation
# Key Point: Index ALWAYS starts at 0 and NOT 1

# The first data structure is a list, which is ordered
My_List: list[typing.Any] = [] # Use the hard brackets to create an empty list or by the list() constructor

# To append or add items into a list, use the append method
My_List.append(4)
My_List.append("meme")
My_List.append(True)
My_List.append(3.14)
My_List.append("yeet")
print(My_List)

# To remove items, use the remove method
My_List.remove(4)
My_List.remove(3.14)
print(My_List)

# However, if you want to add a value at a certain index, then you can use the insert method
My_List.insert(2, "lol") # Insert string "lol" at index 2
print(My_List)

# If you want to instead remove the very last item in the list then you can use the pop method
My_List.pop()
print(My_List)

# But for the pop method, you can also specify an index to remove an item at a specific index
My_List.pop(1)
print(My_List)

# You can also use the del (short for delete) keyword to remove values
My_List.append(5.385) # Int 5 is added!
print(My_List)

del My_List[My_List.index(5.385)] # Now it's gone!
print(My_List)

# If you want to find the index of a certain value in a list then you can use the index method
print(My_List.index("meme")) # Prints 0 because the string "meme" is at index 0

# If you want to sort a list then you can use the sort method
My_List.sort()
print(My_List)

# If you want to clear the entire list, use the clear method
My_List.clear()
print(My_List)

My_List.append(3)
My_List.append(10)
My_List.append(-5)
My_List.append(1)
My_List.append(6)

print(My_List)

# If you want to reverse the list, then use the reverse method
My_List.reverse()
print(My_List)

My_List.append(3)
My_List.append(3)
print(My_List)

# If you want the amount of times that a certain value appears in a list then use the count method
print(My_List.count(3)) # 3 because the  number 3 is in the list 3 times!

# Slicing Lists!
# Basically a "range" in the lists
# Slicing is done by indexing by followed by a start, stop, and step kind of like a range but with colons ":"
# Start is included, stop is excluded, and step is like skipping numbers

print(My_List[1:-1]) # Get me all values from the second item to the last (-1 just means the very last value in the list)
print(My_List[::2]) # Get me all values by skip counting by 2. Basically values at index 0, 2, 4, 6, 8...

# If you want to copy a list then you can use the copy method
Another_List = My_List.copy() # Equivalent to My_List[:]

# List comprehensions are a short way to create lists and put data in them
My_List.clear()
Another_List.clear()

# Example of a list comprehension
My_List = [x for x in range(10)] # Basically just creates a list for numbers 0 to 9

# This is equivalent to...
for i in range(10):
    Another_List.append(i)

print(My_List)
print(Another_List)

# List comprehensions start with the value at the start then as it goes from left to right, it corresponds to the start to the end of the expression
My_List.clear()
Another_List.clear()

My_List = [(x, y) for x in range(5) for y in range(5)] # Every single combination from 0 - 5
# This is equivalent to...

for x in range(5):
    for y in range(5):
        Another_List.append((x, y))

print(My_List)
print(Another_List)

# You can even add conditions in a list comprehension
My_List.clear()
Another_List.clear()

My_List = [(x, y) for x in range(1, 5) for y in range(1, 5) if (x * y) % 2 == 0] # Find all possible combinations of two numbers ranging from 1 - 4 when multiplied are even only
# This is equivalent to...

for i in range(1, 5):
    for j in range(1, 5):
        if (i * j) % 2 == 0:
            Another_List.append((i, j))
# However, list comprehensions can sometimes become too long so it's sometimes better to just write it out without list comprehensions

print(My_List)
print(Another_List)

# You can also NEST list comprehensions
This_Matrix: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# This is equivalent to...
Another_Matrix: list[list[int]] = [[number for number in This_Matrix[i]] for i in range(len(This_Matrix))]
print(This_Matrix)
print(Another_Matrix)

# Oh wait I forgot to talk about the extend method, it basically just adds all elements from another iterable to the end of the list
My_List.clear()

My_List.append(5)
My_List.append("meme")
My_List.append(False)
My_List.extend(range(10)) # Adds all numbers from 0 to 9 at the end of the list
print(My_List)

My_List.clear()
Another_List.clear()

del My_List
del Another_List

# The next data structure are tuples. They are also ordered like lists. However, they are immutable meaning unchangeable but there are workarounds
# To create a tuple, there are three ways: Curly brackets, tuple constructor, or adding a comma a value

My_Tuple = () # Curly Brackets
Another_Tuple = tuple(()) # Tuple constructor
Yet_Another_Tuple = "meme", # Notice that comma at the end

print(type(My_Tuple))
print(type(Yet_Another_Tuple))
print(type(Yet_Another_Tuple))
# They're all tuples!

# Like I said, tuples are IMMUTABLE, which means that they are UNCHANGEABLE. That means that tuples have no adding or removing methods at all but like I also said, there are workarounds
# The first workaround is to convert it to a list, add / remove items, and then convert it right back
My_Tuple = []
print(type(My_Tuple))

My_Tuple.append("woah")
My_Tuple.append(13.5)
My_Tuple.append(True)
My_Tuple.append("yeah")
My_Tuple.append(False)

My_Tuple = tuple(My_Tuple)
print(type(My_Tuple))
print(My_Tuple)

Actually_a_Tuple = "meme", True, 383.46, "refef"
# When assigning a variable multiple values, Python just turns it into a tuple of values instead

print(Actually_a_Tuple)
print(type(Actually_a_Tuple))

# To unpack a tuple, just use the * sign on it
print(*Actually_a_Tuple)

# Like lists, you can also nest tuples!
Nested_Tuple = My_Tuple, "hi", 42.5, True
print(Nested_Tuple)

del My_Tuple
del Another_Tuple
del Yet_Another_Tuple
del Actually_a_Tuple
del Nested_Tuple

# The next type of common data structures are sets, which are very fast but are unordered, meaning they CANNOT be indexed, and they do not allow duplicates.
# To create a set, you can use the curly brackets {} (make sure to add items to make it a set or python will default it to a dictionary instead) or the set() constructor

My_Set = {"apple", "orange", "tangerine", "lemon", "dragon fruit"}
Another_Set = set(())

# If you tried to make an empty set with the curly brackets {} then it would be a dictionary
Actually_a_Dictionary = {}
print(type(Actually_a_Dictionary))
del Actually_a_Dictionary

# Sets do not allow duplicate values so if they are any duplicate values, it will be removed
Duplicates_Set = {"apples", "blueberries", "bananas", "strawberries", "apples"}
print(Duplicates_Set)

Duplicates_Set.clear()

# Since sets do not allow duplicates, True & 1 and False and 0 are also considered duplicates
Duplicates_Set = {"hi", True, 3.14, 0, "yeet", 1, False}
print(Duplicates_Set)

Duplicates_Set.clear()
del Duplicates_Set

# To add items to a set, use the add method
My_Set.add("dragon fruit")
print(My_Set)

# To remove items from a set, use the remove or discard method
My_Set.remove("apple")
print(My_Set)

# You can also add sets to other sets by using the update function
Another_Set = {"mango", "strawberry", "blueberry"}
print(Another_Set)

My_Set.update(Another_Set)
print(My_Set)

# Unlike the remove method, disard does not raise an error if it does not find the specified value to remove
My_Set.discard("yeet") # Discard a value that doesn't exist
print(My_Set) # Runs successfully without crashing the program

# You can also use the pop method to remove an item but it removes a random item, it could literally be anything in the set
My_Set.pop()
print(My_Set)

# Unlike other basic data structures, set has unique mathematical  methods like difference, intersection, union, etc. with two versions which are returning a new set and modifying the set

My_Set.clear()
Another_Set.clear()

# Starting with the union method, which returns a new set that combines two sets into one set

My_Set = {"apple", "banana", "orange"}
Another_Set = {"orange", "tangerine", "strawberry"}

Yet_Another_Set = My_Set.union(Another_Set)
print(Yet_Another_Set)

# The alternative is the update method, which does the same thing as the union method but instead modifies the set in place
Yet_Another_Set.clear()

Yet_Another_Set = My_Set.update(Another_Set)
print(Yet_Another_Set) # None, since it returned nothing
print(My_Set) # Updates the set

My_Set.clear()
Another_Set.clear()

My_Set = {"apple", "banana", "orange"}
Another_Set = {"orange", "tangerine", "strawberry"}

# There is also a shortcut for the union / update method, which are the | and |= operators
Yet_Another_Set = My_Set | Another_Set # Union
print(Yet_Another_Set)

Yet_Another_Set.clear()

My_Set |= Another_Set # Update
print(My_Set)

My_Set.clear()
Another_Set.clear()

# Next is the difference and difference_update method, which returns elements that are present in the original set but not in the specified sets

My_Set = {1, 2, 3, 4, 5}
Another_Set = {3, 4, 5, 6, 7, 8}
# 3, 4, and 5 are in the second set but 1 and 2 are not so the result will be a set containing the numbers 1 and 2

Yet_Another_Set = My_Set.difference(Another_Set)
print(Yet_Another_Set)

Yet_Another_Set.clear()

# difference_update will do the same thing as difference but modify the original set instead of returning a new set
My_Set.difference_update(Another_Set)
print(My_Set)

My_Set.clear()
My_Set = {1, 2, 3, 4, 5}

# These methods also have shortcuts, which are - and -=

Yet_Another_Set = My_Set - Another_Set
print(Yet_Another_Set)

Yet_Another_Set.clear()

My_Set -= Another_Set
print(My_Set)

My_Set.clear()
My_Set = {1, 2, 3, 4, 5}

# Next are the interection and intersection_update methods, which returns a set or modifies the set based on elements that are present in both of the sets

Yet_Another_Set = My_Set.intersection(Another_Set)
print(Yet_Another_Set) # {3, 4, 5} because the values 3, 4, and 5 are in both of My_Set and Another_Set

Yet_Another_Set.clear()

My_Set.intersection_update(Another_Set)
print(My_Set)

My_Set.clear()
My_Set = {1, 2, 3, 4, 5}

# They also have their own shortcuts, which are & and &=

Yet_Another_Set = My_Set & Another_Set
print(Yet_Another_Set)

Yet_Another_Set.clear()

My_Set &= Another_Set
print(My_Set)

My_Set.clear()
My_Set = {1, 2, 3, 4, 5}

# The last mathematical method is the symmetric_difference and symmetric_difference_update methods (wow cool naming Python lol), which returns a set or modifies the set based on unique values on each set, meaning the same value from a set cannot exist the other set

Yet_Another_Set = My_Set.symmetric_difference(Another_Set)
print(Yet_Another_Set) # {1, 2, 6, 7, 8} because the values 3, 4, and 5 exist in both of the sets, it only grabs unique values

Yet_Another_Set.clear()

My_Set.symmetric_difference_update(Another_Set)
print(My_Set)

My_Set.clear()
My_Set = {1, 2, 3, 4, 5}

# They also have their own shortcuts, which are ^ and ^=

Yet_Another_Set = My_Set ^ Another_Set
print(Yet_Another_Set)

Yet_Another_Set.clear()

My_Set ^= Another_Set
print(My_Set)

My_Set.clear()
Another_Set.clear()

del My_Set
del Another_Set
del Yet_Another_Set

# Set has a bit more methods but they are used for comparison with other sets (or other basic data structures like lists and tuples), which are isdisjoint, issuperset, and issubset
# These methods return bools (True or False)

Big_Set: set[int] = {1, 2, 3, 4, 5}
Small_Set: set[int] = {6, 7, 8, 9, 10}

# Starting off with isdisjoint, according to Python, it checks if two sets have a null intersection, to put it simply it checks if two sets have no elements in common with each other

print(Big_Set.isdisjoint(Small_Set)) # True, both sets share absolutely no elements at all
Small_Set = {4, 5, 8, 9, 10} # However, if I just modify the Small_Set a little bit...

print(Big_Set.isdisjoint(Small_Set)) # It will now return False because both sets share the value 4 and 5
Small_Set = {6, 7, 8, 9, 10}

# Unlike other methods, the isdisjoint method does NOT have an operator equivalent to it sadly so it's only just set.isdisjoint(iterable)

# Next is the issuperset method, which checks if all elements in the small set are in the big set

print(Big_Set.issuperset(Small_Set)) # This is false because none of the elements in the Small Set are in the Big Set
print(Small_Set.issuperset(Big_Set)) # This is also false as well since you can't have a smaller set be a "parent" set of a larger set

Small_Set = {2, 3, 4} # But if I modify it just a little bit...
print(Big_Set.issuperset(Small_Set)) # This is true because the elements in the Small Set are inside of the Big Set
print(Small_Set.issuperset(Big_Set)) # Yeah, still false

Small_Set.add(10) # {2, 3, 4, 10}
print(Big_Set.issuperset(Small_Set)) # If a Small Set contains any values that are not in the Big Set then it will be false

Small_Set.remove(10)

# The issuperset has two operators which are the > and the >= operators, however unlike the mathematical operators, they don't return a new set or modify the original set
# The >= operator is the one that is equivalent to the issuperset method

print(Big_Set >= Small_Set)

# However, the > operator just means that the two sets cannot be equal, that's literally it
Small_Set = {1, 2, 3, 4, 5} # Now this is equal to the Big Set

print(Big_Set > Small_Set) # Even though the Big Set and Small Set are equal to each other, it still evaluates to false because of the missing equal sign
Small_Set = {6, 7, 8, 9, 10}

# Lastly is the issubset method, which is literally the exact opposite of the issuperset method. It just checks if a set's elements are in a larger set

print(Small_Set.issubset(Big_Set)) # False because none of the values in the Small Set are in the Big Set
print(Big_Set.issubset(Small_Set)) # This is also False because of the same reasoning above

Small_Set = {1, 2, 3}

print(Small_Set.issubset(Big_Set)) # True, the elements in Small Set are in the Big Set
print(Big_Set.issubset(Small_Set)) # False, the big set is much larger than the small set and has more elements

# The issubset also has two operators like the issuperset method, which are the < and <= operators
# The <= operator is the one that is equivalent to the issubset method

print(Small_Set <= Big_Set)

# The < operator just means that the two sets cannot be equal
Small_Set = {1, 2, 3, 4, 5} # Setting them to be equal to each other

print(Small_Set < Big_Set) # False, it will evaluate to False either way despite being equal

Small_Set.clear()
Big_Set.clear()

del Small_Set
del Big_Set

# The last basic data structure that Python offers is the dictionary or in short, just dict.
# A dictionary works like an actual dictionary, where a word or key has its own definition or value
# To create a dictionary, use the curly braces or {} or the dict() constructor

My_Dictionary = {}
Another_Dictionary = dict()

# To initialize a dictionary with values, start with a key (string), separate it with a colon (:) and then input whatever value you want

My_Dictionary = {"yeetus": 420, "yeehaw": True, "meme": 67.69}

# However, initializing a dictionary with values using the dict constructor requires a plain text and then setting it equal to a value

Another_Dictionary = dict(meme = True, boom = "bam", no = 3.14)

print(My_Dictionary)
print(Another_Dictionary)

# To add values to a dictionary, use the hard brackets, put a key inside of it, and then set the entire thing to a new value

My_Dictionary["what"] = 20.99
print(My_Dictionary)

# You can also use the update method to add items in a dictionary but it is most practically used for adding in multiple items instead of just one item
# It takes in multiple keys and values or an iterable as an argument

My_Dictionary.update(woah = "yessir", yeah = "KABOOM")
print(My_Dictionary)

# To remove a value, there are multiple ways and they are the pop and popitem methods
# For the pop method, you need to specify the key to remove both key and value from the dictioanry

My_Dictionary.pop("yeetus")
print(My_Dictionary)

# However, the popitem method removes the last value that was addede into the dictionary
My_Dictionary.popitem()
print(My_Dictionary) # It removed the key "yeah" and its value because it was the last thing that was inserted into the dictioanry

# Or an alternativ way to remove an item is by using the del keyword

del Another_Dictionary["no"]
print(Another_Dictionary)

# To access values in a dictionary, just index by key

print(Another_Dictionary["meme"]) # Prints the value of the key

# However, if you  want specific information from a dictionary, there are the keys, values, and items attributes or properties

print(My_Dictionary.keys())
print(My_Dictionary.values())

# Items is basically both the keys and their values in a tuple, grouped in a list and then for some reason all of that in another tuple

print(My_Dictionary.items())

# Or you can loop through the keys and values

for key in My_Dictionary.keys():
    print(key)

for value in My_Dictionary.values():
    print(value)

for item in My_Dictionary.items():
    print(item)

# Another way to get values from a dictionary is to use the get method

print(My_Dictionary.get("meme")) # Will attempt to try to find the key meme and return the value then print it

# If the get method fails to find the key then it will return None as a default value

print(My_Dictionary.get("random value")) # Printed None

# Just found this out right now at the time of writing this but apparently you can also use the fromkeys method to also create a dictionary?
# It takes in an iterable as the first parameter and then a default value as the second one (Value will become None if the second parameter is missing)
# Returns a new dictionary, doesn't modify the original one)

print(dict.fromkeys(["woah", "YEET", "kachow"], 3.14))

# Also just found this out right now but you can also look up / access values using the setdefault method like the get method but instead it inserts the given key and value if it doesn't exist

My_Dictionary.setdefault("meme")
print(My_Dictionary) # The key "meme" already exists inside of the dictionary so it will just print it out without any changes

My_Dictionary.setdefault("KACHOW", 100)
print(My_Dictionary) # Since it doesn't exist, it will automatically insert the key "KACHOW" with the given value 100

# If you want to copy a dictionary then use the copy method

Yet_Another_Dictionary = My_Dictionary.copy()
print(Yet_Another_Dictionary)

# If you want to clear a dictionary then use the clear method

Yet_Another_Dictionary.clear()
print(Yet_Another_Dictionary)

del Yet_Another_Dictionary

# There is another way to loop through a dictionary, which is by using the enumerate keyword

for index, key in enumerate(My_Dictionary): # Enumerating just the dictionary by itself will get an index and the key. Note here, dictionaries CANNOT be indexed because they are unhashable
    print(f"Key: {index}, Value: {key}")

My_Dictionary.clear()
Another_Dictionary.clear()

del My_Dictionary
del Another_Dictionary