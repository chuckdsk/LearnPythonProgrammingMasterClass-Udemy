# Demonstrating different string literal styles in Python
# Strings can be enclosed in double quotes
print("Today is a good day to learn Python")

# Or in single quotes - both are equivalent
print('Python is fun')

# Can include apostrophes (contractions) within double-quoted strings
print("Python's string are easy to use")

# Can include double quotes within single-quoted strings
print('We can even include "quotes" in strings')

# String concatenation using the + operator
print("hello" + " world")

# Variable assignment - storing a string in a variable
greeting = "Hello"
#name = input("Please enter your name ")
name = "Tim"

# String concatenation using variables (no space between strings by default)
print(greeting + name)

# If we want a space between concatenated strings, we can add that too
print(greeting + ' ' + name)

# Integer variable assignment
age = 24

# Print the integer value
print(age)

# type() function shows the data type of a variable
# String types are shown as <class 'str'>
print(type(greeting))

# Integer types are shown as <class 'int'>
print(type(age))

# Another string variable (not used in output, but shows variable naming)
age_in_words = "2 years"

# Modern f-string formatting (f-prefix allows embedded expressions in braces)
# This concatenates the string with the value of age variable interpolated
print(name + f" is {age} years old")

# Verify the type of age variable (still an integer, not converted to string)
print(type(age))

# F-string with inline calculation and format specifier
# f"..." - f-string syntax allows expressions in braces
# {22 / 7:12.50f} - calculate 22/7, format as floating-point with width 12 and 50 decimal places
print(f"Pi is approximately {22 / 7:12.50f}")

# Store the Pi approximation in a variable
pi = 22 / 7

# F-string using the pi variable with the same format specifier
# {:12.50f} - width 12, floating-point format, 50 decimal places precision
# Shows that the same formatting can be applied to variables
print(f"Pi is approximately {pi:12.50f}")
