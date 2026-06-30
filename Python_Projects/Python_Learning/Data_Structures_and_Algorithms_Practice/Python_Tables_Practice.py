import typing

# There are four types of tables (what I call them in other programming languages), which are lists, tuples, sets, and dictonaries

My_List: list[typing.Any] = ["Tangerines", 50, 7.99, True] # To create a list, use the [] brackets to initialize one
# Lists can be of ANY types as well

print(type(My_List)) # Lists will have a class of list

Another_List: list[typing.Any] = list(("Apples", "Oranges", "Grapes", "Strawberries", "Blueberries")) # You can also use the list() constructor to convert another table data type into a list
# However, if you are making a new list using list() then you must put another brackets of paranthesis to tell Python what the list contains
# Outer () for list constructor and inner () for what the list is containing

# Characteristics of Lists: Ordered, Changeable, and allows duplicate members

# To access lists, you can index them using the [] brackets

print(My_List[0]) # This will print the first item inside of the list (Tangerines)
# To clear any confusion, tables start with the index of 0 so basically 0 is the first item, 1 is actually the second item, and so on.

# To get the last item of the list, you can index backwards
print(My_List[-1]) # This will index one but backwards, which will return the last item in the list, which is the boolean True

# You can even "slice" lists just like a for range function!
print(My_List[1:3]) # Syntax List[start (inclusive), end, (exclusive)]
# This will print 50 and 7.99 because it returned the 2nd item to the 4th item but the end is exclusive so it didn't include the 4th item

print(My_List[1:]) # This will print the 2nd item all the way to the end because if you don't include the end parameter when slicing a list then Python will default it to being the last item

print(50 in My_List) # You can even use the in keyword to check if an item is inside of a List!
# True because 50 is in My_List

print("Strawberries" in My_List) # False, Strawberries is not in My_List

# You can change an item in a list by indexing
My_List[1] = 30
print(My_List) # ['Tangerines', 30, 7.99, True]

# You can change multiple items in a list by slicing too
My_List[0:2] = ["Oranges", 10]
print(My_List) # ['Oranges', 10, 7.99, True]

# You can add items using the insert() function
# Syntax: List.insert(index, item)
My_List.insert(2, "hi")
print(My_List)

# If the index is greater than the size of the List then it will become the last item
My_List.insert(10, "thing")
print(My_List)

# You can also use append() to insert an item into a list and it will become the last item automatically
My_List.append("something_here_idk")
print(My_List)

# You can extend or add lists using the extend() function
Extend_1: list[typing.Any] = ["yeetus", "oh", "meh"]
Extend_2: list[typing.Any] = ["wow", "hmmmm", "lolol"]

# Syntax: List.extend(List)
Extend_1.extend(Extend_2)
print(Extend_1)
# This will add the elements from Extend_2 to Extend_1 - Extend_2 does NOT get modified, only Extend_1

# You can remove elements by using the remove() and pop() function
# The difference between them is that remove() uses a literal value inside of a list while pop() uses an index in the list

Extend_1.remove("lolol") # Removes the value lolol from list by specifying it
print(Extend_1)

Extend_1.pop(4) # Removes the value at index 4, which is "hmmmm"
print(Extend_1)

Extend_1.pop() # However, if you use pop and pass in no arguments, then it will remove the last value in the list by default
print(Extend_1)

# You can also use the del keyword to delete an element inside of a list
del Extend_1[0]
print(Extend_1)

# You can also delete the entire list itself
del Extend_1
# print(Extend_1) You can't print a deleted item though since it's deleted. Python will throw a NameError.

# If you want to clear an entire list then use the clear() function
Extend_2.clear()
print(Extend_2) # Will print [] with no elements inside of it 2

Completely_Random_List: list[typing.Any] = ["Watermelon", False, 15, 53.84, True]

# You can loop through a list!
for element in Completely_Random_List:
    print(element)

# If you rather want the index of a list then you can use the range and len function combined
for i in range(len(Completely_Random_List)):
    print(Completely_Random_List[i])

# You can loop through a list using a while loop

Index_Thingy = 0

while Index_Thingy < len(Completely_Random_List):
    print(Completely_Random_List[Index_Thingy])
    Index_Thingy += 1

# You can use a list comprehension to make lists more readable and concise

meh_ok_list: list[int] = [] # Numbers from 0 to 9

for x in range(10):
    meh_ok_list.append(x)

print(meh_ok_list)

another_but_better_list: list[int] = [x for x in range(9)]
# Not only is this equivalent to the code above, this is just one line yet it is more readable and concise

numbered_list_thingy_idk: list[int] = [4, 7, 2, 7, 8, 2, 6, 8, 3, 9, 10, 46, 9, 23, 98, 54]
new_number_thing_list: list[str] = ["Even" if x % 2 == 0 else "Odd" for x in numbered_list_thingy_idk]
print(new_number_thing_list)
# You can put if statements inside of list comprehensions
# One if statement Syntax: Value, Expression, If-Statement
# If-else statement Syntax: Value, if statement, else statement, Value, Expression

# You can sort lists!
pls_sort_this_list_lol: list[int] = [4545, 434, 56, 87, 3447, 563, 78, 35, 78, 23, 89, 4547, 235, 89, 563, 8783, 679, 344]
pls_sort_this_list_lol.sort() # The sort() function will sort the list alphanumerically
print(pls_sort_this_list_lol)

pls_sort_but_string: list[str] = ["yea", "hm", "BOI", "REEEE", "oof", "aw"]
pls_sort_but_string.sort()
print(pls_sort_but_string)

# You can even reverse sort by using the keyword argument reverse and set it to True
pls_reverse_sort_lol: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pls_reverse_sort_lol.sort(reverse = True) # Will reverse the sorting
print(pls_reverse_sort_lol)

# You can create a function to custom sort your list
def Custom_Sort_Function(n: int):
    return abs(n - 50)

More_Numbers_lol: list[int] = [456, 345, 324, 6758, 3254, 576, 324, 658, 234]
More_Numbers_lol.sort(key = Custom_Sort_Function) # Just make sure the first keyword parameter is key and then your function name
print(More_Numbers_lol)

Capitals_and_Lowercases: list[str] = ["a", "F", "e", "Z", "y", "J"]
Capitals_and_Lowercases.sort(key = str.lower) # You can ignore case sensitive sorting by putting key = str.lower
print(Capitals_and_Lowercases)

# You can reverse a list using the reverse() function instead of sort(reverse = True)
Reverse_List_Again: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Reverse_List_Again.reverse()
print(Reverse_List_Again)

# You cannot set another list to another list because it will become a reference
# Meaning, whatever happens to one or the other will happen to one or the other

Reference_This_List: list[int] = [0, 1, 2, 3, 4, 5]
hehe_boi_reference: list[int] = Reference_This_List
hehe_boi_reference.remove(0)
print(Reference_This_List) # This also removed the first value from the copied list

# You can copy lists by using the copy() function
Copy_pls_lol: list[str] = ["meh", "erm", "huh", "mid"]
Ok_I_copy_you = Copy_pls_lol.copy()

Copy_again_ok: list[int] = [56, 34, 75, 324, 65, 234, 89, 4]
meh_ok_copy_that = list(Copy_again_ok) # You can use the list constructor and pass in the original list to copy it
print(meh_ok_copy_that)

Copy_BOI: list[int] = [436, 876, 324, 567, 56, 2, 546, 46]
bruh_ok_list = Copy_BOI[:] # You can slice with no parameters because by default Python will put the first parameter as the staring value and the second parameter as the last value if there are no arguments passed in
print(bruh_ok_list)

# I guess you can use a for loop for copying?
COPY_MOREEEEE_YEEEHAW: list[int] = [1, 2, 3]
OK_BRUH: list[int] = [4, 5, 6]

for element in OK_BRUH:
    COPY_MOREEEEE_YEEEHAW.append(element)

print(COPY_MOREEEEE_YEEEHAW)

# You can use the extend() function to copy a list too
NOW_EXTEND: list[int] = [6, 8, 2, 67, 4]
EXTEND_TIME: list[int] = [45, 1, 78, 32]

NOW_EXTEND.extend(EXTEND_TIME)
print(NOW_EXTEND)

# Tuples are ordered, unchangeable, and allows duplicates
Me_is_tuple_boi: tuple[int, int, int] = (1, 2, 3) # Note to myself, tuples are extremely explicit in type checking. I must put the amount of elements in the type annotation as well as in the tuple itself
TUPLE_BOI: tuple[int, ...] = (4, 5, 6) # Or just use elipsis
Another_Tuple: tuple[int] = (1,) # If there is only one element in the tuple left then I have to put a , to tell Pylance that this is a tuple

# You can use the tuple constructor to create a tuple
Tuple_Constructor_thingy: tuple[int, ...] = tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Notes: There are 2 rounded brackets. One for the tuple constructor and one of the tuple's items

# You can't change a tuple but there are work arounds such as converting it into a list and changing it back to a tuple
# Also tuple doesn't have an append() method
Me_Stronk_Tuple: tuple[int, ...] = (1, 2, 3, 4)
me_now_list: list[int] = list(Me_Stronk_Tuple)
me_now_list.append(5)
Me_Stronk_Tuple = tuple(me_now_list)

# You can add tuples to tuples as well
More_Tuple_lololol: tuple[int, ...] = (1, 2, 3, 4, 5)
More_additional_tuple_thing: tuple[int, ...] = (6, 7, 8, 9, 10)

More_Tuple_lololol += More_additional_tuple_thing
print(More_Tuple_lololol)

# To remove an element, you can convert it to a list and then turn it right back to a tuple!
REEEEEEEEEEE_tuple: tuple[int, ...] = (56, 345, 2, 7, 32, 67, 2, 89, 34)
yeet_list: list[int] = list(REEEEEEEEEEE_tuple)
yeet_list.remove(89)
REEEEEEEEEEE_tuple = tuple(yeet_list)
print(REEEEEEEEEEE_tuple)

# You can completely delete the tuple using the del keyword lol
pls_no_Delete_pls_sire: tuple[int, ...] = (1, 2, 3)
del pls_no_Delete_pls_sire
# print(pls_no_Delete_pls_sire) # Python will raise a NameError because the tuple does not exist anymore

# This is a packaged tuple
Packaged_Tuple: tuple[str, ...] = ("Apple", "Lemons", "Coconuts", "Berries")

# To unpack a tuple, you simply put values in tuple form and set it to the Packaged Tuple
(Red, Yellow, Brown, Blue) = Packaged_Tuple
print(Red, Yellow, Brown, Blue)

# You can use the asterisk to store more than one value inside of the element
Another_Packaged_Tuple: tuple[str, ...] = ("Lemons", "Coconuts", "Strawberries", "Apples", "Cherries")
(Yellow, Brown, *Red) = Another_Packaged_Tuple # Red becomes a list containing Strawberries, Apples, and Cherries
print(Yellow, Brown, Red)

# You can add an asterisk anywhere but if you have an variables that you don't want to include in the asterisk then you need to make new values after it
MORE_PACKAGED_TUPLE_YEEEE: tuple[str, ...] = ("Feather", "Dumbbells", "Pull-Ups", "Variant Push Ups")
(Easy, *Medium, Hard) = MORE_PACKAGED_TUPLE_YEEEE
print(Easy, Medium, Hard)

# You can multiply tuples together and all it does is just double and append the extra values
Multiply_Pls: tuple[int, ...] = (1, 2, 3, 4)
yeet_idk = Multiply_Pls * 2
print(yeet_idk)

# You can use the count() function to check how many times a value appears in the table. List also has this method available. Sects and dictionaries don't.
yeah_hmm: tuple[int, ...] = (34, 698, 34, 7, 8, 34, 67, 34)
print(yeah_hmm.count(34)) # Output is 4 because 34 appeared 4 times

# You can use the index function to see what the index of a specific value is
INDEX_THIS_BOI: tuple[str, ...] = ("hi", "wat", "wow", "hm", "yesh")
print(INDEX_THIS_BOI.index("hi")) # 0 - "hi" is the first element in the tuple

# Sets are unordered, unchangeable, and unindexed also it does NOT allow duplicates. (I think of it as literal chaos or negative)
My_Set: set[str] = {"Me boi", "REEEEE", "yeah", "hmmm", "yeah", "yeah"} # To create a set, use the {} brackets
print(My_Set) # Only one "yeah" appears - Confirmation of no duplicates

# True and 1 and False and 0 are considered the same value
Boolean_Set: set[bool | int] = {True, 1, False, 0}
print(Boolean_Set)

# You can also use the set() constructor to create a set
MORE_SET: set[str] = set(("ye", "wat", "hm", "yeetus", "RAAA"))
print(MORE_SET)

# Unlike other data types of tables, Set cannot be accessed by index since everything is unordered
# print(MORE_SET[1]) # Python will throw a TypeError

# To check if an element is in a list use the in keyword
print("ye" in MORE_SET)

# To add an item into a Set, there's no append() but it has an add() function
MORE_SET.add("bruh")
print(MORE_SET)

# To combine tables (can be any data type), use the update() function
Another_Set_idk_bruh: set[str] = {"rererere", "oof", "ded"}
MORE_SET.update(Another_Set_idk_bruh)
print(MORE_SET)

# To remove an element, you can use the remove() function or the discard() function. You cannot use pop because sets are unindexed.
MORE_SET.remove("oof")
print(MORE_SET)

MORE_SET.discard("ded")
print(MORE_SET)

# The difference between remove() and discard() is that remove() will raise an error if the value does not exist but discard() won't
MORE_SET.discard("rtdrthrth")
print(MORE_SET)

# MORE_SET.remove("kjsdhg") # Python will raise a KeyError
# print(MORE_SET)

# If you want to be random then use the pop() method. Don't pass in any arguments though. Just pop(). It will remove a completely random element from the set.
MORE_SET.pop()
print(MORE_SET)

# To join sets, use the union() or update() method
SET_BOIIII: set[int] = {1, 2, 3}
MORE_SET_REE: set[int] = {4, 5, 6}

# Union returns another set with all elments in each set combined
ANOTHER_MORE_SET = SET_BOIIII.union(MORE_SET_REE)
print(ANOTHER_MORE_SET)

# You can also the use | operator to union sets
GIMMIE_MORE_SETS_REEEEEEEEEEE: set[int] = {1, 2, 3, 4, 5}
OKAY_BOIIIII: set[int] = {6, 7, 8, 9, 10}

COMBINE_MORE_SET = GIMMIE_MORE_SETS_REEEEEEEEEEE | OKAY_BOIIIII
print(COMBINE_MORE_SET)

# Update changes the current set by adding the elements from the other table and adds it on to the original set
Oh_wow_a_tuple: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
GAAAAAAAAAAAAA_MORE_SETTTTTTTTTS: set[int] = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
GAAAAAAAAAAAAA_MORE_SETTTTTTTTTS.update(Oh_wow_a_tuple)
print(GAAAAAAAAAAAAA_MORE_SETTTTTTTTTS)

# If you want to keep only duplicates (values that are found in both sets) then use the intersection() method or the & operator
# However, & can only intersect sets and not other table data types

# Intersection will return a new set btw
Fruits_Set: set[str] = {"Apples", "Cherries", "Blueberries"}
More_Fruits_lol: set[str] = {"Apples", "Strawberries", "Banannas"}

Intersected_Fruits = Fruits_Set.intersection(More_Fruits_lol)
print(Intersected_Fruits) # {'Apples'}

# But if you don't want a new set but just update the original set with duplicates only then use the intersection_update() method
Fruits_Set.intersection_update(More_Fruits_lol)
print(Fruits_Set) # {'Apples'}

# However, if you want the values that are in the first set and not in the second set, then use the difference() method or the "-" operator
Random_Numbers: set[int] = {5, 6, 1, 9, 3}
More_random_numbers: set[int] = {5, 8, 4, 11, 3}

Unique_Random_Numbers = Random_Numbers.difference(More_random_numbers)
print(Unique_Random_Numbers)

# You can also use the difference_update() method, which works just like intersection_update() but keeps only the values that are present in the first set
Random_Numbers.difference_update(More_random_numbers)
print(Random_Numbers)

# If you want the values that are not present in both sets then use the symmetric_differene() method or the ^ operator
RANDOMIZER_BOIII: set[int] = {6, 7, 8, 9, 10}
MORE_RANDOMIZE: set[int] = {1, 2, 3, 4, 5}

Unique_Randomized_Numbers = Random_Numbers.symmetric_difference(MORE_RANDOMIZE)
print(Unique_Randomized_Numbers)

# Use symmetric_difference_update() to update the original list
RANDOMIZER_BOIII.symmetric_difference_update(MORE_RANDOMIZE)
print(RANDOMIZER_BOIII)

# A frozenset is a type of set that is unique, unordered, and unchangeable
# You cannot add or remove elements from a frozenset
# Use the frozenset() function to create a frozenset

wow_is_cold: frozenset[int] = frozenset({1, 2, 3, 4, 5})
print(wow_is_cold)
print(type(wow_is_cold))

# Dictioanries are used to store key, value pairs just like an actual dictionary where a word has a definition
# They are ordered, changeable, and do not allow duplicates

# To create a dictionary, use the {} brackets and "expand" them
My_Dictionary: dict[str, int] = {
    "Apples": 5, # Use : to separate key from values
    "Banannas": 3,
    "Strawberries": 10
}

print(My_Dictionary)

# To print values in a Dictionary, do <Dictionary_Name>["<Key_Name>"]
print(My_Dictionary["Apples"])

Another_Dictionary: dict[str, int] = {
    "A_Number": 6,
    "Another_Number": 5,
    "Hmmm": 8,
    "Hmmm": 9 # This value will overwrite the original value
}

print(Another_Dictionary["Hmmm"])

# You can also create a dictionary but use the dict constructor
More_Dictionary = dict(Name = "Dylan", Age = 15)

# You can also use the get() method to access values
print(My_Dictionary.get("Apples"))

# To get the keys, use the keys() function
print(My_Dictionary.keys())

# To get the values, use the values() function
print(My_Dictionary.values())

# To update an item in a dictionary, you can index it using the specified key name or use the update() method

Dictionary_REEEEE: dict[str, int] = {
    "Strawberries": 10,
    "Tangerines": 8,
    "Blueberries": 6
}

# Change by indexing
Dictionary_REEEEE["Blueberries"] = 5
print(Dictionary_REEEEE)

# Change by update() function
# Put {} brackets inside of the () brackets, followed by the Key Name, put a colon: then the value you want to set it to
Dictionary_REEEEE.update({"Strawberries": 9})

# To add new values, you can use the index and update() method to also add values
Dictionary_REEEEE["Oranges"] = 5
print(Dictionary_REEEEE)

Dictionary_REEEEE.update({"Coconuts": 4})
print(Dictionary_REEEEE)

# To remove an item, use the pop() method and pass in the key name, use the popitem() method (This removes the last inserted item), or use the del keyword
Dictionary_REEEEE.pop("Oranges")
print(Dictionary_REEEEE)

Dictionary_REEEEE.popitem()
print(Dictionary_REEEEE)

del Dictionary_REEEEE["Strawberries"]
print(Dictionary_REEEEE)

# To loop through a dictionary, you can use the keys(), values(), and items() method

for x in My_Dictionary.keys():
    print(x)

for x in My_Dictionary.values():
    print(x)

# However, for items() you need two variables. One for the key and the other for the value.
for x, y in My_Dictionary.items():
    print(x, y)

# To copy a dictionary, you can use the copy() function or the dict() constructor and pass in the dictionary
Copied_Dictionary = My_Dictionary.copy()
print(Copied_Dictionary)

Another_Copied_Dictionary = dict(My_Dictionary)
print(Another_Copied_Dictionary)

# This is a nested dictionary, which contains dictionaries
Popular_Fruits: dict[str, dict[str, int | bool]] = {
    "Apples": {
        "Delicious": True,
        "Amount": 10
    },

    "Blueberries": {
        "Delicious": True,
        "Amount": 40
    }
}

# To access an item in a nested dictionary, you can index them
print(Popular_Fruits["Apples"]["Amount"])

# You can still also use the get() function to access nested items
print(Popular_Fruits.get("Apples").get("Amount"))

for fruits, attributes in Popular_Fruits.items():
    for attribute in attributes:
        print(f"{attribute}: {attributes[attribute]}")