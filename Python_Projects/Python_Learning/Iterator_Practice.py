# An iterable is a object that can be iterated to go through its values
# An iterator is the object that now contains the separate values of the iterable so they can be iterated through
# My explaination is not very good so I will try to use examples below to help.

This_String: str = "Apples" # This is an iterable
Iterate_String = iter(This_String) # This is the iterator that will go through the iterable's values

print(next(Iterate_String)) # Use the next function go to the next value of the iterable (Starts with the very first value)
print(next(Iterate_String))
print(next(Iterate_String))
print(next(Iterate_String))
print(next(Iterate_String))
print(next(Iterate_String))
# print(next(Iterate_String)) # You will get to a point where you reach the end of the values and can't iterate anymore. Python will raise a StopIteration error.

# Tables are iterators (tuples, sets, dictionaries, and lists)
# You can use a for loop to iterate through a table
My_Tuple: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for number in My_Tuple:
    print(number)

# Apparently a for loop automatically creates an iterator
Longest_Word: str = "pneumonoultramicroscopicsilicovolcanoconiosis" # Strings are an iterable object

for i, character in enumerate(Longest_Word):
    print(character)

# You can use Object-Oriented Programming (OOP) to create a custom iterable class

class My_Iterable_Class:
    def __iter__(self):
        self.Starting_Number = 100
        return self # Apparently you have to return the class instance or object of itself?
    
    def __next__(self) -> int:
        if self.Starting_Number <= 0:
            raise StopIteration
        else:
            self.Starting_Number -= 1
            return self.Starting_Number
        
Iterable_Class = My_Iterable_Class()
Iterator_Class = iter(Iterable_Class)

for x in range(100):
    print(next(Iterable_Class))