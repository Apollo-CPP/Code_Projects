import re

# re.findall() returns a list containing all matches
# re.search() returns a match object if there is a match anywhere in the string
# re.split() returns a list where the string has been split at each match
# re.sub() replaces one or many matches with a string

# MetaCharacters (need to be escaped)
# . ^ $ * + ?  { } [ ] \ | ( )

# . - Any Character except new line
# \d - Digits (0 - 9)
# \D - Not a digit (0 - 9)
# \w - Word character (a-z, A-Z, 0-9, _)
# \W - Not a word character
# \s - Whitespace (space, tab, newline)
# \S - Not a whitespace

# \b - Word Boundary
# \B - Not a Word Boundary
# ^ - Beginning of a string
# $ - End of a string

# [] - Matches characters in brackets
# [^ ] - Matches characters NOT in brackets
# | - Either Or
# ( ) - Group

# Quantifiers:
# * - 0 or More
# + - 1 or More
# ? - 0 or One
# {3} - Exact Number
# {3,4} - Range of Numbers (Minimum, Maximum)

print("\tTab") # Tabs a literal tab and then prints tab
print(r"\tTab") # A raw string, prints literally "\tTab"

The_Alphabet_Lowercase: str = "abcdefghijklmnopqrstuvwxyz"
The_Alphabet_Uppercase: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

Chess_Website: str = "https://www.chess.com"

pattern = re.compile(r"ABC") # It is also case sensitive
matches = pattern.finditer(The_Alphabet_Uppercase)

Random_Digits: str = "66584837478695734637586897874739"
Random_Letters: str = "klejghearig"

More_Letters: str = "Me Oof aAAaAaAaaAAAa"
Ooga_Booga: str = "rthjttys erggetr ythst efef uykk"

Sentence: str = "Start a sentence and then bring it to an end"

Random_Phone_Number: str = "123-456-7890"
Another_Phone_Number: str = "573.265-7824"
More_Numbers_In_String: str = "800-200-700"

for match in matches:
    print(match)

Rhyming_Words: str = """

Mat
Cat
Bat
Sat

"""

Random_Names: str = """

Mr T
Mr. Jones
Mr. Guy

Ms. Williams
Ms Nancy
Ms. Cahill

"""

Random_Emails: str = """

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

"""

More_Emails: str = """

https://www.google.com
https://youtube.com
http://coreyms.com
https://www.nasa.gov

"""

# Output: <re.Match object; span=(0, 3), match='ABC'>
# Span is the start index (0) to the end index (3) of where it found the pattern
# 0 is inclusive and 3 is exclusive so basically 0 - 2
# Returned is a Match object

print(The_Alphabet_Uppercase[0:3]) # To confirm, slice the string with the span

Another_Pattern = re.compile(r".") # . is a special character but if you want to search for a literal period then escape it using the backslash \
more_matches = Another_Pattern.finditer(Chess_Website)

More_Letters: str = "yeaaaa uhh no yees"

for match in more_matches:
    print(more_matches)

print("------------------------------------------------")

Number_Pattern = re.compile(r"\d") # Finds digits from 0 - 9
number_matches = Number_Pattern.finditer(Random_Digits)

for match in number_matches:
    print(match)

print("------------------------------------------------")

Not_Number_Pattern = re.compile(r"\D") # Finds non-digits
not_number_matches = Not_Number_Pattern.finditer(Random_Letters)

for match in not_number_matches:
    print(match)

print("------------------------------------------------")

Boundary_Pattern = re.compile(r"\b") # Finds word boundaries
Boundary_Matches = Boundary_Pattern.finditer(More_Letters)

for match in Boundary_Matches:
    print(match)

print("------------------------------------------------")

Not_boundary_pattern = re.compile(r"\B") # Finds non word boundaries
Not_boundary_matches = Not_boundary_pattern.finditer(Ooga_Booga)

for match in Not_boundary_matches:
    print(match)

print("------------------------------------------------")

yeehaw_pattern = re.compile("^Start") # Looks for start of a string
rawwww = yeehaw_pattern.finditer(Sentence)

for match in rawwww:
    print(match)

print("------------------------------------------------")

im_ded_pattern = re.compile("end$") # Finds the end of a string
bruh_matches = im_ded_pattern.finditer(Sentence)

for match in bruh_matches:
    print(match)

print("------------------------------------------------")

Phone_Pattern = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") # Looks for 3 digits, - , 3 digits, - , and lastly 4 digits in a string
Phone_Matches = Phone_Pattern.finditer(Random_Phone_Number)

for match in Phone_Matches:
    print(match)

print("------------------------------------------------")

Set_Phone_Pattern = re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d") # Looks for 3 digits and then a dash or a dot (inside of a set) and repeat until end
Set_Phone_Matches = Set_Phone_Pattern.finditer(Another_Phone_Number)

for match in Set_Phone_Matches:
    print(match)

print("------------------------------------------------")

Another_Number_Pattern = re.compile(r"[827]00[-.][827]00[-.][827]00") # Find a character that's an 8, 2, or 7, followed by a - or a . and repeat
Another_Number_Match = Another_Number_Pattern.finditer(More_Numbers_In_String)

for match in Another_Number_Match:
    print(match)

print("------------------------------------------------")

Alphabetical_Pattern = re.compile(r"[a-zA-Z]") # Put [a-zA-Z] back to back to look for characters that are lowercase / uppercase in the alphabet
Alphabetical_Match = Alphabetical_Pattern.finditer(More_Letters)

for match in Alphabetical_Match:
    print(match)

print("------------------------------------------------")

Rhyming_Pattern = re.compile(r"[a-zA-Z]at") # Find any letter that is followed by "at"
Rhyming_Matches = Rhyming_Pattern.finditer(Rhyming_Words)

for match in Rhyming_Matches:
    print(match)

print("------------------------------------------------")

Simplified_Phone_Number_Pattern = re.compile(r"\d{3}[-.]\d{3}[-.]\d{4}") # Look for 3 digits, then a - or . , look for another 3 digits, then a - or . , then look for 4 digits
Simplified_Phone_Number_Matches = Simplified_Phone_Number_Pattern.finditer(Another_Phone_Number)

for match in Simplified_Phone_Number_Matches:
    print(match)

print("------------------------------------------------")

Name_Pattern = re.compile(r"M(r | s | rs)\.?\s[A-Z]\w*") # Look for an uppercase "M" letter, then look for a r, or s, or rs after that, then look for a . (Zero or more occurences), followed by a capital letter, and then word characters that have 0 or more occurences
Name_Matches = Name_Pattern.finditer(Random_Names)

for match in Name_Matches:
    print(match)

print("------------------------------------------------")

Email_Pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)")
# Look for an uppercase or lowercase letter or a number from 0 - 9, followed by a - with 1 or More occurences follwowed by an "@", followed by an uppercase / lowercase letter followed by a - with one or more occurences until a "." that ends with com or edu or net
Email_Matches = Email_Pattern.finditer(Random_Emails)

for match in Email_Matches:
    print(match)

print("------------------------------------------------")

More_Email_Pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
# Find an http (the s is optional), followed by a ://, group the www with the . escaped for a literal . and make it optional, then group any word chaacters with one or more occurences, then group a literal "." followed by word characters with one or more occurences

More_Email_Matches = More_Email_Pattern.finditer(More_Emails)

All_Email_Matches = More_Email_Pattern.findall(More_Emails) # Returns all matches in a list and puts groups in tuples
print(All_Email_Matches)

for match in More_Email_Matches:
    print(match.group(0)) # Entire match
    print(match.group(1)) # First group
    print(match.group(2)) # Second group
    print(match.group(3)) # Third group

Another_Sentence_Pattern = re.compile(r"start", re.IGNORECASE) # A flag that ignores case-sensitivity, there are much more flags
Another_Sentece_Matches = Another_Sentence_Pattern.match(Sentence)
print(Another_Sentece_Matches)