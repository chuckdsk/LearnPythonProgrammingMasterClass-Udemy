# Demonstrating escape sequences in Python strings
# Escape sequences allow special characters to be included in strings

# \n - newline escape sequence (moves to next line)
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# \t - tab escape sequence (horizontal tab character)
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# Escaping quotes within strings
# Single quotes inside single-quoted strings need to be escaped with \'
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')

# Alternative: use double quotes to contain single quotes without escaping
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

# Triple-quoted strings can span multiple lines and include quotes without escaping
# The backslash \ at the end of the first line is a line continuation character
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")

# Another example of triple-quoted strings with line continuation
anotherSplitString = """This string has been \
split over \
several \
lines"""

print(anotherSplitString)

# Escaping backslashes in file paths
# \\ - escaped backslash (each \ needs to be doubled)
print("C:\\Users\\timbuchalka\\notes.txt")

# Raw strings (r"") treat backslashes literally - no escaping needed
# Useful for file paths and regular expressions
print(r"C:\Users\timbuchalka\notes.txt")
