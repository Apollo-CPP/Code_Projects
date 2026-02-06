# You can convert JSON to Python and Python to JSON

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x) # Apparently this json.loads(x) converts the value of x into Python

# the result is a Python dictionary:
print(y["age"])

# I copied the first part from w3schools because I didn't know anything about the value of x because it is in JSON

A_Random_Python_Dictionary: dict[str, int | str] = {
    "Name": "Dylan",
    "Age": 15,
    "Country": "China"
}

Converted_Dictionary = json.dumps(A_Random_Python_Dictionary) # Use json.dumps() to convert from Python to JSON
print(Converted_Dictionary)

Random_List: list[int] = [56, 1234, 897, 34, 1, 657, 234]
Convert_List = json.dumps(Random_List, indent=4, separators=(".", " = ")) # You can indent and put custom separators
print(Convert_List)

# JSON also has a keyword parameter called sort_keys= and expects a boolean to sort dictionary keys when being converted.