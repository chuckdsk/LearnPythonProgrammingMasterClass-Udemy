# Sequence operators demonstration - operations that work on sequences like strings
# Sequences in Python include strings, lists, tuples, etc.

# String concatenation using the + operator
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

# Concatenate multiple strings using the + operator (requires explicit + between each string)
print(string1 + string2 + string3 + string4 + string5) # he's probably pining for the fjords

# Implicit string concatenation - Python automatically concatenates adjacent string literals
# This works only for literal strings, NOT for string variables
print("he's " "probably " "pining " "for the " "fjords") # he's probably pining for the fjords

# String repetition using the * operator
# "Hello " * 5 repeats the string 5 times
print("Hello " * 5) # Hello Hello Hello Hello Hello

# Type error demonstration - can't mix string repetition with integer addition directly
# This line would raise TypeError: can only concatenate str (not "int") to str
#print("Hello " * 5 + 4) # ERROR - trying to concatenate string with integer

# Correct way: use parentheses to control operator precedence
# (5 + 4) = 9, so "Hello " is repeated 9 times
print("Hello " * (5 + 4)) # Hello Hello Hello Hello Hello Hello Hello Hello Hello

# String repetition followed by string concatenation
# "Hello " * 5 produces "Hello Hello Hello Hello Hello ", then + "4" adds the string "4"
print("Hello " * 5 + "4") # Hello Hello Hello Hello Hello 4

# Membership testing - checking if a substring exists in a string
# The 'in' operator returns True or False
today = "friday"

# "day" is a substring of "friday" - found at the end
print("day" in today) # True

# "fri" is a substring of "friday" - found at the beginning
print("fri" in today) # True

# "thur" is NOT a substring of "friday"
print("thur" in today) # False

# "parrot" is NOT a substring of "fjord"
print("parrot" in "fjord") # False
